"""Deterministic, no-side-effect multi-agent routing *simulation*. No LLM, APIs or HRIS."""
import json
from pathlib import Path

SCENARIOS = Path(__file__).resolve().parents[1] / "data" / "request_scenarios.json"
ALLOWED_ROUTES = {"policy_faq": "A-POL", "aggregate_reporting": "A-RPT"}
HIGH_IMPACT = {"termination_decision", "candidate_selection", "salary_approval",
               "employee_rating", "financial_payment", "personal_hr_record"}

def route_request(request):
    if not isinstance(request, dict) or not isinstance(request.get("task"), str):
        return {"route": "HUMAN_REVIEW", "reason": "INVALID_REQUEST", "executed": False}
    if request["task"] in HIGH_IMPACT or request.get("sensitive", True):
        return {"route": "HUMAN_REVIEW", "reason": "HIGH_IMPACT_OR_SENSITIVE", "executed": False}
    if request.get("agent_status") not in ("PILOT", "ACTIVE"):
        return {"route": "HUMAN_REVIEW", "reason": "AGENT_NOT_APPROVED_FOR_ROUTING", "executed": False}
    if request.get("has_access") is not True:
        return {"route": "HUMAN_REVIEW", "reason": "ACCESS_DENIED", "executed": False}
    if request.get("policy_current") is not True:
        return {"route": "HUMAN_REVIEW", "reason": "SOURCE_NOT_CURRENT", "executed": False}
    role = ALLOWED_ROUTES.get(request["task"])
    if role is None:
        return {"route": "HUMAN_REVIEW", "reason": "OUT_OF_SCOPE", "executed": False}
    return {"route": role, "reason": "ELIGIBLE_FOR_SUPERVISED_DRAFT_ONLY", "executed": False}

def evaluate(path=SCENARIOS):
    cases = json.loads(Path(path).read_text(encoding="utf-8"))
    rows = [{"id": c["id"], "expected": c["expected_route"],
             "actual": route_request(c)["route"]} for c in cases]
    return rows, sum(row["expected"] == row["actual"] for row in rows)

if __name__ == "__main__":
    rows, passed = evaluate()
    for row in rows:
        print(row)
    print(f"Synthetic routing match: {passed}/{len(rows)}; 0 actions executed. No live agent.")