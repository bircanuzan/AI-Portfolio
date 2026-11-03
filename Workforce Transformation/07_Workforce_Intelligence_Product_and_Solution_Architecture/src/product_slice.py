"""Pure-Python hypothetical use-case gate and backlog generator. No SaaS, model or API."""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "use_cases.json"

def triage(case):
    required = ("id", "title", "business_owner", "value", "readiness", "effort", "risk")
    if any(k not in case or case[k] in ("", None) for k in required):
        return {"id": case.get("id", "?"), "decision": "HOLD", "reason": "INCOMPLETE",
                "score": None, "human_approval_required": True, "action_executed": False}
    if case["risk"] not in ("low", "medium", "high") or any(
        type(case[k]) is not int or not 1 <= case[k] <= 5 for k in ("value", "readiness", "effort")
    ):
        return {"id": case["id"], "decision": "HOLD", "reason": "INVALID_INPUT",
                "score": None, "human_approval_required": True, "action_executed": False}
    if case["risk"] == "high" or case.get("impact_on_employment", True):
        return {"id": case["id"], "decision": "HOLD", "reason": "HUMAN_IMPACT_RISK",
                "score": None, "human_approval_required": True, "action_executed": False}
    # Transparency rather than false scientific precision: illustrative triage weights only.
    score = 3 * case["value"] + 2 * case["readiness"] - case["effort"]
    return {"id": case["id"], "decision": "DISCUSS", "reason": "HUMAN_REVIEW_NEXT",
            "score": score, "human_approval_required": True, "action_executed": False}

def backlog_card(case):
    result = triage(case)
    return {"epic_id": case.get("id", "?"), "user_problem": case.get("title", "Missing problem"),
            "business_owner": case.get("business_owner", "Unassigned"),
            "triage": result, "definition_of_done": [
                "Validated business baseline", "Data and source owner approval",
                "HR/privacy/security review", "Independent acceptance and safety tests",
                "Named human go/no-go decision"]}

def run(path=DATA):
    cases = json.loads(Path(path).read_text(encoding="utf-8"))
    return [backlog_card(case) for case in cases]

if __name__ == "__main__":
    for card in run():
        print(json.dumps(card, indent=2))
    print("Synthetic discovery slice only; no product deployment, AI inference or HR action.")