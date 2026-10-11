import gzip, json, os
from evalplus.data import get_human_eval_plus

TASKS = ["HumanEval/0", "HumanEval/1", "HumanEval/2", "HumanEval/116", "HumanEval/132", "HumanEval/91", "HumanEval/129", "HumanEval/32", "HumanEval/127", "HumanEval/140", "HumanEval/75", "HumanEval/151", "HumanEval/137", "HumanEval/145", "HumanEval/130", "HumanEval/163"]
INSTR = ("Complete the following Python function. Do not ask any questions or generate any extra text. "
         "Return the complete function in a single Python code block.\n\n")

problems = get_human_eval_plus()
os.makedirs("prompts", exist_ok=True)
with gzip.open("subset.jsonl.gz", "wt") as f:
    for tid in TASKS:
        p = problems[tid]
        f.write(json.dumps(p) + "\n")
        with open(f"prompts/{tid.replace('/', '_')}.txt", "w", encoding="utf-8") as out:
            out.write(INSTR + p["prompt"])