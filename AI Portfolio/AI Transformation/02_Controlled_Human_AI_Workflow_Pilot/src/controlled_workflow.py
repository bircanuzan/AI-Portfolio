"""Offline permission-aware workflow routing. Not an LLM or production security boundary."""
import json
from pathlib import Path

INPUT = Path(__file__).resolve().parents[1] / "data" / "synthetic_requests.json"
GRANTS = {
    "public": {"employee", "manager", "hr"},
    "internal": {"manager", "hr"},
    "restricted": {"hr"},
}
ACTIONS = {"draft_answer", "propose_case_update", "publish_external"}

def route(request):
    required = ("case_id", "actor_role", "classification", "source_approved", "action")
    if any(k not in request for k in required):
        return {"case_id": request.get("case_id", "missing"), "decision": "INVALID_INPUT"}
    audit = {"case_id": request["case_id"], "decision": "HOLD"}
    if request["classification"] not in GRANTS:
        audit["decision"] = "UNKNOWN_CLASSIFICATION"
    elif request["actor_role"] not in GRANTS[request["classification"]]:
        audit["decision"] = "DENY_ACCESS"
    elif request["source_approved"] is not True:
        audit["decision"] = "HOLD_SOURCE_VALIDATION"
    elif request["action"] not in ACTIONS:
        audit["decision"] = "BLOCK_UNSUPPORTED_ACTION"
    elif request["action"] == "publish_external":
        audit["decision"] = "BLOCK_EXTERNAL_SIDE_EFFECT"
    elif request["action"] == "propose_case_update":
        audit["decision"] = "HUMAN_APPROVAL_REQUIRED"
    else:
        audit["decision"] = "DRAFT_FOR_HUMAN_REVIEW"
    # No confidential content, inference, or execution is performed or logged.
    return audit

def run(path=INPUT):
    with open(path, encoding="utf-8") as handle:
        records = json.load(handle)
    return [route(x) for x in records]

if __name__ == "__main__":
    print(json.dumps({"status": "SYNTHETIC OFFLINE RULE ENGINE", "audit_events": run()}, indent=2))
