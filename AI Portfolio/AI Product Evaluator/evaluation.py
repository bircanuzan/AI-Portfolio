import json
from pathlib import Path

def evaluate(task):
    requested = set(task["required_steps"])
    performed = set(task["observed_steps"])
    missing = sorted(requested - performed)
    unexpected = sorted(performed - requested)
    passed = not missing and task["claimed_complete"] == task["actually_complete"]
    return {
        "task_id": task["id"], "pass": passed,
        "missing": missing, "unexpected": unexpected,
        "false_completion_claim": task["claimed_complete"] and not task["actually_complete"],
        "human_review_required": True
    }

if __name__ == "__main__":
    tasks = json.loads(Path(__file__).with_name("tasks.json").read_text())
    print(json.dumps([evaluate(t) for t in tasks], indent=2))
