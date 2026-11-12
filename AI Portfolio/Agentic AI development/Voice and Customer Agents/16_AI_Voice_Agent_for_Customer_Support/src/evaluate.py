"""Evaluate deterministic routing using synthetic examples, not real agent calls."""
import json
from pathlib import Path
from agent import route

def evaluate(scenarios):
    if not scenarios:
        raise ValueError("At least one scenario is required")
    outcomes = []
    for s in scenarios:
        result = route(s["user_message"])
        passed = result["intent"] == s["expected_intent"] and result["escalate"] is s["expected_escalate"]
        outcomes.append({"id": s["id"], "passed": passed, "actual": result, "expected": s})
    return {"total": len(outcomes), "passed": sum(int(x["passed"]) for x in outcomes),
            "pass_rate": sum(int(x["passed"]) for x in outcomes) / len(outcomes),
            "cases": outcomes}

if __name__ == "__main__":
    scenarios = json.loads((Path(__file__).resolve().parents[1] / "data/scenarios.json").read_text(encoding="utf-8"))
    report = evaluate(scenarios)
    print("Cases:", report["total"], "Passed:", report["passed"], "Rate:", f"{report['pass_rate']:.0%}")
    for case in report["cases"]:
        print(case["id"], "PASS" if case["passed"] else "FAIL")
