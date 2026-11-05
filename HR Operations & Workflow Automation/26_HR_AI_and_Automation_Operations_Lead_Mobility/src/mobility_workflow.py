"""Offline maker/checker routing demo for synthetic EOR mobility cases.

NOT legal advice, employment-status adjudication, LLM inference, or a live integration.
"""
import re
from dataclasses import dataclass

ROLES = {"mobility_ops", "senior_mobility"}
SENSITIVE = re.compile(r"(?i)(passport\s*(?:no|number|:)|\b[\w.+-]+@[\w.-]+\.[a-z]{2,}\b|national\s*id|iban\b|credit\s*card|password\s*:)")
INJECTION = re.compile(r"(?i)(ignore (all )?(previous|system) instructions|bypass (the )?(rules|policy)|reveal .*secret)")
HIGH_RISK = {"work_authorization", "visa_renewal", "residency_compliance", "payroll_effective_date"}

@dataclass(frozen=True)
class Case:
    case_id: str
    request_type: str
    region: str
    requester_role: str
    text: str = ""
    consent: bool = True
    source_available: bool = True

def process(case, processed_keys=frozenset()):
    """Generate metadata-only decision; no side effects or external calls."""
    if not isinstance(case, Case):
        raise TypeError("Expected Case")
    public = {"case_id": case.case_id, "region": case.region}
    if case.requester_role not in ROLES:
        return {**public, "state": "blocked", "route": "none", "reason": "rbac_denied"}
    if not case.case_id or not case.region:
        return {**public, "state": "blocked", "route": "none", "reason": "missing_metadata"}
    if case.case_id in processed_keys:
        return {**public, "state": "duplicate", "route": "none", "reason": "idempotency"}
    if not case.consent:
        return {**public, "state": "blocked", "route": "none", "reason": "consent_required"}
    if SENSITIVE.search(case.text):
        return {**public, "state": "hold", "route": "secure_intake", "reason": "sensitive_data_submitted"}
    if INJECTION.search(case.text):
        return {**public, "state": "hold", "route": "human_review", "reason": "unsafe_instruction"}
    if not case.source_available:
        return {**public, "state": "retry", "route": "queue", "reason": "dependency_unavailable"}
    if case.request_type in HIGH_RISK:
        return {**public, "state": "human_review", "route": "mobility_specialist", "reason": "regulated_decision"}
    if case.request_type == "generic_faq":
        return {**public, "state": "draft_only", "route": "approved_knowledge", "reason": "no_legal_decision"}
    return {**public, "state": "human_review", "route": "mobility_specialist", "reason": "unknown_intent"}

if __name__ == "__main__":
    for sample in [
        Case("CASE-001", "generic_faq", "AE", "mobility_ops"),
        Case("CASE-002", "visa_renewal", "AE", "mobility_ops")
    ]:
        print(process(sample))
