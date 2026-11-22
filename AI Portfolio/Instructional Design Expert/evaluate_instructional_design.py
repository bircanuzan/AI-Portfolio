"""Deterministic instructional-design judgement fixture tests (no live LLM calls).

This checks authored structured responses against expert reference labels for
fictional scenarios; it is not a substitute for human pedagogical assessment,
WCAG auditing, legal review, or model evaluation on real outputs.
"""
from __future__ import annotations
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
FIELDS = (
    "objective_aligned", "assessment_valid", "accessibility_risk",
    "digital_delivery_fit", "evidence_supported", "needs_revision",
)
DOMAINS = {
    "learning_objective_alignment", "accessibility_captions",
    "unsupported_pedagogical_claims", "authentic_performance_assessment",
    "evaluation_design", "keyboard_accessibility", "digital_delivery",
    "universal_design_for_learning",
}
SEVERITY = {"low", "medium", "high", "critical"}


def read_cases(path: Path) -> list[dict]:
    rows = []
    seen = set()
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        case = json.loads(line)
        required = {"id", "domain", "scenario", "source_evidence", "reference",
                    "good_answer", "flawed_answer", "deliberately_wrong_field",
                    "corrected_action", "critical_error", "severity"}
        if not isinstance(case, dict) or not required.issubset(case):
            raise ValueError(f"Case {line_no} has missing required fields")
        if case["id"] in seen or case["domain"] not in DOMAINS or case["severity"] not in SEVERITY:
            raise ValueError(f"Duplicate or invalid domain/severity: {case['id']}")
        seen.add(case["id"])
        for key in ("reference", "good_answer", "flawed_answer"):
            answer = case[key]
            if not isinstance(answer, dict) or set(answer) != set(FIELDS):
                raise ValueError(f"{case['id']} {key}: incorrect response schema")
            if any(type(value) is not bool for value in answer.values()):
                raise ValueError(f"{case['id']} {key}: all outputs must be booleans")
        if case["deliberately_wrong_field"] not in FIELDS:
            raise ValueError(f"{case['id']}: wrong-field marker not recognized")
        rows.append(case)
    if not rows:
        raise ValueError("Empty evaluation dataset")
    return rows


def score_response(expected: dict, observed: dict) -> dict:
    if not isinstance(observed, dict):
        return {"schema_valid": False, "correct_fields": 0, "total_fields": len(FIELDS),
                "field_accuracy": 0, "field_errors": list(FIELDS)}
    schema_valid = set(observed) == set(FIELDS) and all(type(v) is bool for v in observed.values())
    errors = [key for key in FIELDS if type(observed.get(key)) is not bool or observed.get(key) != expected[key]]
    return {"schema_valid": schema_valid, "correct_fields": len(FIELDS)-len(errors),
            "total_fields": len(FIELDS),
            "field_accuracy": round((len(FIELDS)-len(errors))/len(FIELDS), 4),
            "field_errors": errors}


def audit(rows: list[dict]) -> dict:
    evaluations = []
    for case in rows:
        good = score_response(case["reference"], case["good_answer"])
        flawed = score_response(case["reference"], case["flawed_answer"])
        evaluations.append({
            "id": case["id"],
            "domain": case["domain"],
            "severity": case["severity"],
            "good_fixture": good,
            "flawed_fixture": flawed,
            "expected_deliberate_error_found": case["deliberately_wrong_field"] in flawed["field_errors"],
            "correction": case["corrected_action"],
            "rationale": case["source_evidence"],
        })
    return {
        "evidence_level": "synthetic manually authored fixtures; no actual AI model tested",
        "cases": len(evaluations),
        "domains": dict(Counter(case["domain"] for case in rows)),
        "correct_fixture_passed": sum(item["good_fixture"]["field_accuracy"] == 1 for item in evaluations),
        "deliberate_errors_detected": sum(item["expected_deliberate_error_found"] for item in evaluations),
        "needs_human_review": "All natural-language teaching-quality judgments, legal accessibility compliance, bias and interpretation",
        "evaluations": evaluations,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=str(ROOT/"data/evaluation_cases.jsonl"))
    parser.add_argument("--out", default=str(ROOT/"outputs/evaluation_report.json"))
    args = parser.parse_args()
    data = read_cases(Path(args.data))
    report = audit(data)
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    csvpath = destination.with_suffix(".csv")
    with csvpath.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["case_id", "domain", "severity", "good_fields_correct",
                         "flawed_fields_correct", "identified_failure", "corrected_action"])
        for x in report["evaluations"]:
            writer.writerow([x["id"], x["domain"], x["severity"],
                             x["good_fixture"]["correct_fields"],
                             x["flawed_fixture"]["correct_fields"],
                             ";".join(x["flawed_fixture"]["field_errors"]), x["correction"]])
    print(f"Synthetic scenario count: {report['cases']}")
    print(f"Authored correct fixtures passing: {report['correct_fixture_passed']}")
    print(f"Deliberate errors flagged: {report['deliberate_errors_detected']}")
    print(f"Written: {destination} and {csvpath}")
    print("These metrics describe fixtures, NOT measured LLM performance.")


if __name__ == "__main__":
    main()
