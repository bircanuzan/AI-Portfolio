#!/usr/bin/env python3
"""Synthetic AI training annotation operations audit; Python 3.10+, stdlib only."""
from __future__ import annotations
import argparse, csv, json, re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

LABELS = {"payroll", "benefits", "mobility", "recruitment", "privacy", "other"}
REQUIRED = ("case_id", "source_id", "text", "received_at", "due_at", "gold_label", "risk_tier")
REVIEW_REQUIRED = ("case_id", "annotator_a", "annotator_b", "a_minutes", "b_minutes", "exception_note")
TARGETS = {"agreement": 0.90, "gold_accuracy": 0.95, "qa_conflict_rate": 0.10, "missing_rate": 0.00}

def rows(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

def validate(cases, reviews):
    issues = []
    if not cases or not reviews:
        issues.append("Empty collection or review data")
        return issues
    for name, data, required in (("cases", cases, REQUIRED), ("reviews", reviews, REVIEW_REQUIRED)):
        missing_fields = set(required) - set(data[0])
        if missing_fields:
            issues.append(f"{name} missing fields: {sorted(missing_fields)}")
        ids = [x.get("case_id", "") for x in data]
        if len(ids) != len(set(ids)):
            issues.append(f"{name} duplicate case IDs")
    caseids = {x.get("case_id", "") for x in cases}
    reviewids = {x.get("case_id", "") for x in reviews}
    if caseids != reviewids:
        issues.append(f"Unmatched IDs; missing reviews={len(caseids-reviewids)}, orphan reviews={len(reviewids-caseids)}")
    for record in cases:
        if not all(record.get(field) for field in REQUIRED):
            issues.append(f"{record.get('case_id','unknown')}: empty mandatory field")
        if record.get("gold_label") not in LABELS:
            issues.append(f"{record.get('case_id','unknown')}: invalid gold label")
        # Simple high-risk PII check. Real projects need specialist detection and approved policies.
        if re.search(r"\b\d{3}-\d{2}-\d{4}\b",record.get("text","")):
            issues.append(f"{record.get('case_id','unknown')}: possible sensitive ID")
    for record in reviews:
        for field in ("annotator_a", "annotator_b"):
            if record.get(field) not in LABELS:
                issues.append(f"{record.get('case_id','unknown')}: invalid {field}")
        for field in ("a_minutes", "b_minutes"):
            try:
                if float(record.get(field, "")) < 0:
                    issues.append(f"{record.get('case_id')}: negative time")
            except ValueError:
                issues.append(f"{record.get('case_id')}: invalid duration in {field}")
    return issues

def cohen_kappa(a, b):
    if not a or len(a) != len(b):
        raise ValueError("Equal non-empty lists required")
    observed = sum(x == y for x, y in zip(a, b)) / len(a)
    ca, cb = Counter(a), Counter(b)
    expected = sum(ca[k]*cb[k] for k in LABELS) / (len(a)*len(a))
    return round((observed-expected)/(1-expected),4) if expected < 1 else (1.0 if observed==1 else 0.0)

def audit(cases, reviews):
    issues = validate(cases, reviews)
    case_map = {r["case_id"]:r for r in cases if r.get("case_id")}
    pairs = [r for r in reviews if r.get("case_id") in case_map and
             r.get("annotator_a") in LABELS and r.get("annotator_b") in LABELS]
    if not pairs:
        return {"decision":"HOLD","issues":issues + ["No valid paired reviews"]}
    a = [r["annotator_a"] for r in pairs]
    b = [r["annotator_b"] for r in pairs]
    agreements = sum(x == y for x,y in zip(a,b))
    conflicts = [r["case_id"] for r in pairs if r["annotator_a"] != r["annotator_b"]]
    gold_a = sum(r["annotator_a"]==case_map[r["case_id"]]["gold_label"] for r in pairs)
    gold_b = sum(r["annotator_b"]==case_map[r["case_id"]]["gold_label"] for r in pairs)
    durations = [float(r["a_minutes"])+float(r["b_minutes"]) for r in pairs]
    n=len(pairs)
    metrics={
        "collected":len(cases),
        "independently_reviewed":n,
        "completion_rate":round(n/len(cases),4) if cases else 0,
        "reviewer_agreement":round(agreements/n,4),
        "cohen_kappa":cohen_kappa(a,b),
        "gold_accuracy_a":round(gold_a/n,4),
        "gold_accuracy_b":round(gold_b/n,4),
        "conflict_rate":round(len(conflicts)/n,4),
        "average_dual_review_minutes":round(mean(durations),2),
        "reviewed_items_per_8hr_day":round(480/mean(durations),2),
        "mandatory_field_issue_count":len(issues)
    }
    gates={
        "schema_integrity":not bool(issues),
        "coverage":n==len(cases),
        "reviewer_agreement":metrics["reviewer_agreement"]>=TARGETS["agreement"],
        "gold_accuracy_b":metrics["gold_accuracy_b"]>=TARGETS["gold_accuracy"],
        "conflicts":metrics["conflict_rate"]<=TARGETS["qa_conflict_rate"]
    }
    return {"decision":"RELEASE" if all(gates.values()) else "HOLD",
            "metrics":metrics,"gates":gates,"issues":issues,"adjudication_queue":conflicts,
            "next_actions":[
              "Adjudicate discrepancies by human domain reviewer before any release",
              "Calibrate reviewers on recurring intent confusion and privacy cases",
              "Re-label targeted subset and re-run quality gates",
              "Validate downstream schema and provenance with ML engineering"
            ]}

def main():
    root=Path(__file__).resolve().parents[1]
    p=argparse.ArgumentParser()
    p.add_argument("--cases",default=str(root/"data"/"cases.csv"))
    p.add_argument("--reviews",default=str(root/"data"/"reviews.csv"))
    p.add_argument("--output",default=str(root/"reports"/"quality_report.json"))
    args=p.parse_args()
    report=audit(rows(args.cases),rows(args.reviews))
    output=Path(args.output); output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"decision":report["decision"],"metrics":report.get("metrics",{}),"gates":report.get("gates",{}),
                      "adjudication_queue":report.get("adjudication_queue",[])},indent=2))
    return 0 if report["decision"]=="RELEASE" else 2

if __name__=="__main__":
    raise SystemExit(main())
