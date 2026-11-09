"""Deterministic triage of synthetic model/test/grader verdicts."""
from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def classify(case: dict) -> str:
    """Environment failure takes priority; grader quality uses independent oracle."""
    required = {"case_id", "environment_ok", "oracle_pass", "grader_pass"}
    missing = required - case.keys()
    if missing:
        raise ValueError("missing required fields: " + ", ".join(sorted(missing)))
    for key in ("environment_ok", "oracle_pass", "grader_pass"):
        if type(case[key]) is not bool:
            raise TypeError(f"{key} must be boolean")
    if not case["environment_ok"]:
        return "environment_invalid"
    if case["oracle_pass"] and case["grader_pass"]:
        return "verified_pass"
    if not case["oracle_pass"] and not case["grader_pass"]:
        return "genuine_candidate_failure"
    if not case["oracle_pass"] and case["grader_pass"]:
        return "grader_false_positive"
    return "grader_false_negative"


def run(cases: list[dict]) -> dict:
    ids = [case["case_id"] for case in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate case_id")
    decisions = [{"case_id": case["case_id"], "classification": classify(case)}
                 for case in cases]
    return {"kind": "synthetic-evaluation-qa", "total": len(decisions),
            "counts": dict(sorted(Counter(item["classification"] for item in decisions).items())),
            "decisions": decisions}


if __name__ == "__main__":
    cases = json.loads((ROOT / "fixtures" / "judgments.json").read_text(encoding="utf-8"))
    print(json.dumps(run(cases), indent=2, sort_keys=True))
