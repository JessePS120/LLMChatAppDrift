#!/usr/bin/env bash
# Runs EvalPlus base + plus tests on every model's solutions in a results folder.
# Expects a folder containing ChatGPT, Claude, and Gemini subfolders, each holding
# files named HumanEval_<task>_<run>.py (for example, HumanEval_140_3.py).
#
# For each model it builds an EvalPlus samples.jsonl and evaluates it using evalplus. 
# Output: <folder>/eval_summary.csv                        
#
# If a model is missing a folder it will be skipped. 
#
# Usage: ./run_evalplus.sh <folder> [dataset.jsonl.gz]
#   example: PYTHON=/path/to/python ./run_evalplus.sh Pilot_Results  

set -euo pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <folder> [dataset.jsonl.gz]" >&2
    exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
folder="$(cd "$1" && pwd)"
dataset="$(realpath "${2:-$script_dir/subset.jsonl.gz}")"
models=(ChatGPT Claude Gemini)

# Pick an interpreter: $PYTHON, then a Linux venv in the repo, then python3
if [[ -z "${PYTHON:-}" ]]; then
    for candidate in "$script_dir/evalplus-env/bin/python" "$script_dir/.venv/bin/python" "$script_dir/venv/bin/python"; do
        if [[ -x "$candidate" ]]; then PYTHON="$candidate"; break; fi
    done
    PYTHON="${PYTHON:-python3}"
fi

if ! "$PYTHON" -c "import evalplus" 2>/dev/null; then
    echo "evalplus is not installed for $PYTHON (pip install evalplus)" >&2
    exit 1
fi

# Evaluate only the tasks in the subset file instead of all of HumanEval+
export HUMANEVAL_OVERRIDE_PATH="$dataset"

eval_root="$folder/_eval"
evaluated=()

for model in "${models[@]}"; do
    model_dir="$folder/$model"
    echo
    echo "=== $model ==="

    if [[ ! -d "$model_dir" ]]; then
        echo "WARNING: Folder not found: $model_dir - skipping"
        continue
    fi

    if [[ -z "$(find "$model_dir" -maxdepth 1 -name 'HumanEval_*_*.py' -size +0c -print -quit)" ]]; then
        echo "WARNING: No non-empty solution files in $model_dir - skipping"
        continue
    fi

    out_dir="$eval_root/$model"
    mkdir -p "$out_dir"
    samples="$out_dir/samples.jsonl"
    results="$out_dir/samples_eval_results.json"

    # Build samples.jsonl ordered by task then run them so the completion_id EvalPlus
    # assigns within each task matches the run number order
    "$PYTHON" - "$model_dir" "$samples" <<'EOF'
import json, re, sys
from pathlib import Path

model_dir, samples = Path(sys.argv[1]), Path(sys.argv[2])
entries = []
for f in model_dir.glob("*.py"):
    m = re.fullmatch(r"HumanEval_(\d+)_(\d+)", f.stem)
    if not m:
        print(f"WARNING: Skipping unrecognized file name: {f.name}")
        continue
    entries.append((int(m[1]), int(m[2]), f))

with samples.open("w", encoding="utf-8") as out:
    for task, run, f in sorted(entries):
        out.write(json.dumps({"task_id": f"HumanEval/{task}",
                              "solution": f.read_text(encoding="utf-8")}) + "\n")
EOF

    # EvalPlus reuses an existing results file instead of re-running so we need to clear it before doing anything elsse. 
    rm -f "$results"

    if ! "$PYTHON" -m evalplus.evaluate --dataset humaneval --samples "$samples"; then
        echo "WARNING: EvalPlus failed for $model"
        continue
    fi
    evaluated+=("$model")
done

if [[ ${#evaluated[@]} -eq 0 ]]; then
    echo "WARNING: No models were evaluated."
    exit 0
fi

# Combine per-model results into one CSV with a row per solution file
"$PYTHON" - "$folder" "${evaluated[@]}" <<'EOF'
import csv, json, sys
from pathlib import Path

folder, models = Path(sys.argv[1]), sys.argv[2:]
rows = []
for model in models:
    out_dir = folder / "_eval" / model
    results = json.loads((out_dir / "samples_eval_results.json").read_text())["eval"]

    # Run numbers in the same order the samples were written
    runs = {}
    for line in (out_dir / "samples.jsonl").read_text(encoding="utf-8").splitlines():
        runs.setdefault(json.loads(line)["task_id"], [])
    for f in (folder / model).glob("HumanEval_*_*.py"):
        _, task, run = f.stem.split("_")
        if f"HumanEval/{task}" in runs:
            runs[f"HumanEval/{task}"].append(int(run))

    model_rows = []
    for task_id, task_runs in runs.items():
        for run, r in zip(sorted(task_runs), results[task_id]):
            model_rows.append({
                "Model": model,
                "Task": task_id,
                "Run": run,
                "File": f"{task_id.replace('/', '_')}_{run}.py",
                "Base": r["base_status"],
                "Plus": r["plus_status"],
                "PassedBoth": r["base_status"] == "pass" and r["plus_status"] == "pass",
            })
    n = len(model_rows)
    base = sum(r["Base"] == "pass" for r in model_rows)
    both = sum(r["PassedBoth"] for r in model_rows)
    print(f"{model}: base {base}/{n}, base+plus {both}/{n}")
    rows += model_rows

csv_path = folder / "eval_summary.csv"
with csv_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

print(f"\nSummary written to {csv_path}\n")
print(f"{'Model':<8} {'Task':<14} {'Run':>3}  {'Base':<6} {'Plus':<6}")
for r in rows:
    print(f"{r['Model']:<8} {r['Task']:<14} {r['Run']:>3}  {r['Base']:<6} {str(r['Plus']):<6}")
EOF
