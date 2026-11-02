#!/usr/bin/env python3
"""Project 44: deterministic AI governance gate for SYNTHETIC declarations only.

This is NOT an AI model, actual technical validation, a legal compliance checker,
or a substitute for independent evidence review. GO is a simulated rule outcome.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

VALID_TIERS = {"T1", "T2", "T3", "T4"}
BASE = {
    "inventory_complete": "AI inventory",
    "impact_complete": "impact assessment",
    "privacy_approved": "privacy approval",
    "security_approved": "security approval",
    "model_card_complete": "model/system card",
    "monitoring_plan": "monitoring plan",
    "evidence_verified": "verified evidence",
}
MODERATE = {
    "uat_passed": "user acceptance testing",
    "oversight_documented": "human oversight design",
}
HIGH = {
    "independent_qa_passed": "independent assurance",
    "fairness_review_completed": "fairness review",
    "committee_approved": "governance committee decision",
    "human_final_decision": "mandatory human final decision",
    "red_team_passed": "red-team testing",
}


def assess(case):
    """Return one fail-closed status and explicit reasons for a fictional case."""
    case_id = str(case.get("case_id") or "UNSPECIFIED")
    tier = case.get("tier")
    if tier not in VALID_TIERS:
        return {"case_id": case_id, "decision": "NO_GO", "reasons": ["Invalid or missing risk tier"]}
    if not case.get("owner"):
        return {"case_id": case_id, "decision": "NO_GO", "reasons": ["No accountable business owner"]}
    if tier == "T4" or case.get("prohibited_use"):
        return {"case_id": case_id, "decision": "NO_GO", "reasons": ["Prohibited use under sample policy"]}
    if case.get("autonomous_adverse_decision"):
        return {"case_id": case_id, "decision": "NO_GO", "reasons": ["Autonomous consequential adverse decision"]}
    if case.get("unapproved_sensitive_export"):
        return {"case_id": case_id, "decision": "NO_GO", "reasons": ["Unapproved sensitive-data export"]}
    if case.get("critical_findings", 0) > 0:
        return {"case_id": case_id, "decision": "NO_GO", "reasons": ["Unresolved critical assurance finding"]}

    required = dict(BASE)
    if tier in ("T2", "T3"):
        required.update(MODERATE)
    if tier == "T3":
        required.update(HIGH)
    if case.get("vendor_used"):
        required["vendor_reviewed"] = "third-party vendor review"
    if case.get("genai_used"):
        required["genai_security_tested"] = "GenAI security testing"
    if case.get("material_change"):
        required["change_revalidated"] = "material-change revalidation"

    missing = [label for key, label in required.items() if case.get(key) is not True]
    if missing:
        return {"case_id": case_id, "decision": "HOLD", "reasons": ["Missing: " + ", ".join(missing)]}
    return {
        "case_id": case_id,
        "decision": "GO",
        "reasons": ["All synthetic declared controls are true; independently verify real-world evidence before any launch"],
    }


def assess_all(cases):
    return [assess(case) for case in cases]


def main():
    parser = argparse.ArgumentParser(description="SampleCo synthetic AI governance gate")
    parser.add_argument("cases", help="Path to synthetic JSON array")
    parser.add_argument("--output", help="Optional path for results JSON")
    args = parser.parse_args()
    data = json.loads(Path(args.cases).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        parser.error("cases input must be a JSON list")
    output = assess_all(data)
    for row in output:
        print("{} | {:5} | {}".format(row["case_id"], row["decision"], "; ".join(row["reasons"])))
    summary = Counter(x["decision"] for x in output)
    print("SYNTHETIC RESULTS ONLY: {}".format(dict(summary)))
    if args.output:
        Path(args.output).write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
