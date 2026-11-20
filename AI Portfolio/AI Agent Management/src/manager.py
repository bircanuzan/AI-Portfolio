"""Offline operational agent control-plane demonstration; no live LLM calls."""
import hashlib
import json
import re
from pathlib import Path

ALLOWED = {"extract_document", "route_workflow", "schedule_review", "compliance_check"}


class AgentManager:
    def __init__(self):
        self.completed = set()
        self.audit = []

    def record(self, task_id, status, reason, attempts=0, result=None):
        event = {"task_id": task_id, "status": status, "reason": reason,
                 "attempts": attempts, "result": result,
                 "previous_hash": self.audit[-1]["hash"] if self.audit else "GENESIS"}
        event["hash"] = hashlib.sha256(json.dumps(event, sort_keys=True).encode()).hexdigest()
        self.audit.append(event)
        return event

    def run(self, task):
        """Validate untrusted task data; never execute document instructions."""
        task_id = task.get("id", "missing-id")
        if not isinstance(task_id, str) or not task_id.strip():
            return self.record("invalid-id", "rejected", "invalid_id")
        if task_id in self.completed:
            return self.record(task_id, "duplicate", "idempotency_guard")
        if task.get("action") not in ALLOWED:
            return self.record(task_id, "rejected", "tool_not_allowed")
        document = task.get("document", "")
        if not isinstance(document, str) or not document.strip():
            return self.record(task_id, "rejected", "missing_document")
        # Demonstrates known attack fixtures only; not a general injection detector.
        if re.search(r"ignore\s+(all\s+)?previous|reveal\s+secret|disable\s+audit", document, re.I):
            return self.record(task_id, "quarantined", "suspicious_document")
        if not isinstance(task.get("confidence"), (int, float)) or isinstance(task.get("confidence"), bool):
            return self.record(task_id, "rejected", "invalid_confidence")
        confidence = task["confidence"]
        if not 0 <= confidence <= 1:
            return self.record(task_id, "rejected", "invalid_confidence")
        if confidence < .85 or task.get("risk") != "low":
            # An approval flag in a task is never accepted as trusted authorization.
            return self.record(task_id, "review", "human_approval_required")
        failures = task.get("simulated_failures", 0)
        if not isinstance(failures, int) or isinstance(failures, bool) or failures < 0:
            return self.record(task_id, "rejected", "invalid_retry_fixture")
        for attempt in range(1, 4):
            if attempt <= failures:
                continue
            if task["action"] == "extract_document":
                match = re.search(r"REF-\d{4}", document)
                if not match:
                    return self.record(task_id, "review", "missing_reference", attempt)
                result = {"reference": match.group(0)}
            elif task["action"] == "route_workflow":
                result = {"queue": "exceptions" if "exception" in document.lower() else "operations"}
            elif task["action"] == "schedule_review":
                result = {"proposal": "next_available_review_slot", "external_write": False}
            else:
                result = {"check": "reference_present" if "REF-" in document else "reference_absent"}
            self.completed.add(task_id)
            return self.record(task_id, "completed", "local_simulation", attempt, result)
        return self.record(task_id, "failed", "retry_budget_exhausted", 3)


def evaluate(cases):
    manager = AgentManager()
    matches = []
    for case in cases:
        event = manager.run(case["task"])
        matches.append(event["status"] == case["expected_status"] and
                       event["result"] == case.get("expected_result"))
    counts = {s: sum(e["status"] == s for e in manager.audit)
              for s in ("completed", "review", "rejected", "quarantined", "failed", "duplicate")}
    metrics = {"dataset": "synthetic offline fixtures", "cases": len(cases),
               "outcome_and_output_matches": sum(matches),
               "outcome_and_output_accuracy": sum(matches) / len(cases) if cases else None,
               "status_counts": counts,
               "completion_rate": counts["completed"] / len(cases) if cases else None,
               "total_simulated_attempts": sum(e["attempts"] for e in manager.audit),
               "live_model_calls": 0, "external_writes": 0,
               "business_savings": "not measured"}
    return metrics, manager.audit


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    cases = json.loads((root / "data/cases.json").read_text())
    metrics, audit = evaluate(cases)
    (root / "reports").mkdir(exist_ok=True)
    (root / "reports/metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    (root / "reports/audit.json").write_text(json.dumps(audit, indent=2) + "\n")
    print(json.dumps(metrics, indent=2))
