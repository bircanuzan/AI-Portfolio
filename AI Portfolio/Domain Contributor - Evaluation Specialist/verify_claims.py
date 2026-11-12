import json
from pathlib import Path

def verify(case):
    missing = sorted(set(case["required_sources"]) - set(case["cited_sources"]))
    return {"id":case["id"], "source_complete":not missing,
            "missing_primary_evidence":missing, "rationale":case["expected_reasoning"],
            "human_fact_check_needed":True}

if __name__ == "__main__":
    cases=json.loads(Path(__file__).with_name("scenario_bank.json").read_text())
    print(json.dumps([verify(c) for c in cases],indent=2))
