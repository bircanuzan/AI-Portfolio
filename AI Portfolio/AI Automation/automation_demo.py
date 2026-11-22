#!/usr/bin/env python3
"""Local, synthetic human-controlled workflow automation demo.

This is deterministic routing/drafting for education; NOT an LLM agent, live
service integration, autonomous action engine, or deployment.
"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALLOWED = {"support", "operations", "hr", "finance", "security"}
SENSITIVE = ("export all", "all user records", "delete all", "bulk download", "password database")
MANUAL = ("bank account", "refund", "payment", "screen candidates", "hiring decision", "salary")
LOW_RISK_DRAFTS = {
    "support": "Draft: Please refer to the approved self-service guide. A teammate can help if needed.",
    "operations": "Draft: I can prepare an internal task checklist; please confirm the details.",
}

def route(requests):
    seen = set()
    records = []
    for item in requests:
        ident = str(item.get("request_id", "")).strip()
        department = str(item.get("department", "")).strip().lower()
        prompt = str(item.get("request", "")).strip()
        errors = []
        if not ident:
            errors.append("missing_request_id")
        elif ident in seen:
            errors.append("duplicate_request_id")
        if department not in ALLOWED:
            errors.append("unsupported_department")
        if not prompt:
            errors.append("missing_request_text")
        if ident:
            seen.add(ident)
        if errors:
            records.append({"request_id": ident or "MISSING", "status": "invalid_input",
                            "reason": ",".join(errors), "draft": None})
            continue
        lower = prompt.lower()
        if any(x in lower for x in SENSITIVE):
            status, reason, draft = "blocked", "sensitive_data_or_destructive_action", None
        elif department in {"hr", "finance", "security"} or any(x in lower for x in MANUAL):
            status, reason, draft = "human_review", "sensitive_or_regulated_workflow", None
        else:
            status, reason = "draft_ready", "low_risk_draft_only"
            draft = LOW_RISK_DRAFTS.get(department, "Draft: Request noted; human validation required.")
        records.append({"request_id": ident, "department": department,
                        "status": status, "reason": reason, "draft": draft})
    return records

def summary(records):
    counts = Counter(row["status"] for row in records)
    return {"total": len(records), "draft_ready": counts["draft_ready"],
            "human_review": counts["human_review"], "blocked": counts["blocked"],
            "invalid_input": counts["invalid_input"],
            "external_actions_executed": 0,
            "note": "Synthetic demonstration; not an LLM evaluation or client result."}

def run(src=None, out=None):
    src = Path(src) if src else ROOT / "data" / "synthetic_requests.json"
    out = Path(out) if out else ROOT / "output"
    requests = json.loads(src.read_text(encoding="utf-8"))
    if not isinstance(requests, list):
        raise ValueError("Expected a JSON list")
    decisions = route(requests)
    out.mkdir(parents=True, exist_ok=True)
    (out / "decisions.json").write_text(json.dumps(decisions, indent=2) + "\n", encoding="utf-8")
    (out / "kpis.json").write_text(json.dumps(summary(decisions), indent=2) + "\n", encoding="utf-8")
    with (out / "audit.jsonl").open("w", encoding="utf-8") as f:
        for d in decisions:
            f.write(json.dumps({"id": d["request_id"], "decision": d["status"],
                                "reason": d["reason"]}) + "\n")
    return summary(decisions)

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
