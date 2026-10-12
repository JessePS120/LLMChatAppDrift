import gzip, json, os
from evalplus.data import get_human_eval_plus

TASKS = ["HumanEval/75", "HumanEval/127", "HumanEval/137", "HumanEval/1", "HumanEval/115", "HumanEval/129", "HumanEval/145", "HumanEval/163", "HumanEval/132", "HumanEval/151"]
INSTR = ("Complete the following Python function. Do not ask any questions or generate any extra text. " 
         "Return the complete function in a single Python code block. Do not write any comments. \n\n")

problems = get_human_eval_plus()
os.makedirs("prompts", exist_ok=True)
with gzip.open("subset.jsonl.gz", "wt") as f:
    for tid in TASKS:
        p = problems[tid]
        f.write(json.dumps(p) + "\n")
        with open(f"prompts/{tid.replace('/', '_')}.txt", "w", encoding="utf-8") as out:
            out.write(INSTR + p["prompt"])