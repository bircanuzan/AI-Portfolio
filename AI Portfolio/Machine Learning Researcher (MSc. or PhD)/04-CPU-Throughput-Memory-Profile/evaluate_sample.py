"""Small, dependency-free synthetic protocol check for CPU Throughput & Memory Profile.
Demonstrates metadata validity only; does not evaluate live AI models.
"""
import json
from pathlib import Path

def assess(row):
    required=set(row["required_steps"])
    observed=set(row["performed_steps"])
    missing=sorted(required-observed)
    false_completion=bool(row["reported_complete"] and not row["actual_complete"])
    return {
      "run_id":row["run_id"],
      "required_coverage":round((len(required)-len(missing))/len(required),3) if required else 1.0,
      "missing_steps":missing,
      "false_completion":false_completion,
      "pass":not missing and not false_completion,
      "requires_human_domain_review":True,
    }

if __name__=="__main__":
    path=Path(__file__).with_name("sample_scenarios.json")
    data=json.loads(path.read_text(encoding="utf-8"))
    results=[assess(row) for row in data["observations"]]
    print(json.dumps({"project":data["project"],"synthetic_results":results},indent=2))
