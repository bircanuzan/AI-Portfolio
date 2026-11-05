"""Structured HR workflow benchmark scoring demonstration.

Evaluates HUMAN-ANNOTATED response fields, NOT free-form LLM text.
Business policy is fictional; this is not payroll processing or legal advice.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class UngradeableCase(ValueError):
    """A benchmark needs evidence repair before responses can be scored."""

def quality_gate(case):
    documents = case.get("documents", {})
    required = {"A", "B", "C", "D", "E"}
    missing = required - set(documents)
    if missing:
        raise UngradeableCase("Missing source(s): " + ", ".join(sorted(missing)))
    a, b, c, d, e = (documents[x] for x in "ABCDE")
    if not a.get("proration_denominator") or not a.get("monthly_base_aed"):
        raise UngradeableCase("Missing governing proration policy")
    if b.get("last_worked_day") is None or d.get("last_worked_day") is None:
        raise UngradeableCase("Missing signed or approved exit date")
    if b["last_worked_day"] != d["last_worked_day"]:
        raise UngradeableCase("Conflicting exit dates without tie-breaker")
    if c.get("approval_status") != "draft":
        raise UngradeableCase("Unexpected transaction status requires review")
    if e.get("allowance_status") is None:
        raise UngradeableCase("Missing allowance approval evidence")
    if e.get("allowance_status") not in {"pending", "approved", "rejected"}:
        raise UngradeableCase("Ambiguous allowance status")
    if case.get("requires_external_legal_interpretation", False):
        raise UngradeableCase("Outside legal interpretation required")
    return True

def grade(case, answer):
    """Return transparent 0-10 point rubric based on explicit annotated fields."""
    quality_gate(case)
    gold = case["gold_answer"]
    rubric = case["grading"]
    checks = {
        "date_rule": (answer.get("last_worked_day") == gold["last_worked_day"]
                      and answer.get("proration_denominator") == gold["proration_denominator"]),
        "base_calculation": answer.get("approved_base_aed") == gold["approved_base_aed"],
        "allowance_handling": (answer.get("pending_allowance_escalated") is True
                               and answer.get("allowance_in_approved_input_aed") == 0),
        "draft_variance": answer.get("draft_base_overstatement_aed") == gold["draft_base_overstatement_aed"],
        "sources": set(answer.get("cited_sources", [])) >= set(gold["cited_sources"]),
        "statutory_scope": answer.get("no_statutory_speculation") is True,
    }
    criterion_results = {
        key: {"awarded": rubric[key] if checks[key] else 0, "maximum": rubric[key],
              "passed": bool(checks[key])}
        for key in rubric
    }
    return {
        "case_id": case["case_id"],
        "total": sum(c["awarded"] for c in criterion_results.values()),
        "maximum": sum(rubric.values()),
        "criteria": criterion_results,
        "note": "Structured annotations only; free-text review and any disputes require human judgement.",
    }

def evaluate_samples(case, samples):
    return [
        {"sample_id": item["sample_id"], "expected_score": item["expected_score"],
         "result": grade(case, item["answer"])}
        for item in samples
    ]

if __name__ == "__main__":
    case = json.loads((ROOT / "data/benchmark_case.json").read_text(encoding="utf-8"))
    samples = json.loads((ROOT / "data/sample_answers.json").read_text(encoding="utf-8"))
    for item in evaluate_samples(case, samples):
        print(item["sample_id"], "score", item["result"]["total"],
              "/10; expected", item["expected_score"])
