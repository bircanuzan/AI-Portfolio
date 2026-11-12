"""Synthetic workforce-cost, reward and payroll exception controls.

This is a portfolio demonstrator, NOT a production payroll system.
No UAE statutory pension, settlement, WPS, tax or labour-law rules are computed.
"""

import csv
import json
import sys
from collections import defaultdict
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SAMPLE = ROOT / "data" / "synthetic_workforce.csv"
CENTS = Decimal("0.01")


def amount(value):
    try:
        return Decimal(value or "0").quantize(CENTS, rounding=ROUND_HALF_UP)
    except InvalidOperation as exc:
        raise ValueError(f"Invalid numeric value: {value!r}") from exc


def issue(issues, eid, code, severity, explanation):
    issues.append(dict(employee_id=eid, control=code, severity=severity,
                       detail=explanation))


def analyze(records):
    """Return department/category cost summary plus item-level control exceptions."""
    issues = []
    groups = defaultdict(lambda: dict(count=0, payroll=Decimal("0"),
                                      finance=Decimal("0"), budget=Decimal("0")))
    seen = set()
    for row in records:
        eid = row["employee_id"].strip()
        if not eid or eid in seen:
            issue(issues, eid or "(missing)", "DATA-01", "High",
                  "Missing or duplicate employee ID")
        seen.add(eid)

        hris_base = amount(row["hris_base"])
        payroll_base = amount(row["payroll_base"])
        allowance = amount(row["payroll_allowances"])
        finance = amount(row["finance_monthly_total"])
        budget = amount(row["monthly_budget"])
        market_midpoint = amount(row["market_midpoint"])
        target = amount(row["sti_target_pct"])
        multiplier = amount(row["performance_multiplier"])
        sti_requested = amount(row["sti_requested"])
        actual = payroll_base + allowance
        key = (row["department"].strip(), row["category"].strip())
        totals = groups[key]
        totals["count"] += 1
        totals["payroll"] += actual
        totals["finance"] += finance
        totals["budget"] += budget

        if hris_base != payroll_base:
            issue(issues, eid, "RECON-01", "High",
                  f"HRIS base {hris_base} differs from payroll base {payroll_base}")
        if actual != finance:
            issue(issues, eid, "RECON-02", "High",
                  f"Payroll total {actual} differs from Finance total {finance}")
        if actual > budget:
            issue(issues, eid, "COST-01", "Medium",
                  f"Payroll exceeds monthly budget by {actual-budget}")

        # This band is a demo assumption, never an employer-approved pay policy.
        if market_midpoint <= 0:
            issue(issues, eid, "REWARD-01", "High", "Missing market midpoint")
        else:
            compa_ratio = payroll_base / market_midpoint
            if compa_ratio < Decimal("0.80") or compa_ratio > Decimal("1.20"):
                issue(issues, eid, "REWARD-01", "Review",
                      f"Compa-ratio {compa_ratio:.2f} outside synthetic review band")

        # Incentive illustration only: no eligibility, pension or legal rules here.
        sti_expected = (payroll_base * Decimal("12") * target *
                        multiplier).quantize(CENTS)
        if abs(sti_expected - sti_requested) > CENTS:
            issue(issues, eid, "STI-01", "Medium",
                  f"Illustrative STI {sti_expected} vs requested {sti_requested}")
        if sti_requested > 0 and row["sti_approved"].strip().lower() != "yes":
            issue(issues, eid, "DOA-01", "High",
                  "Incentive requested without recorded approval")
        approver = row["approved_by"].strip()
        preparer = row["prepared_by"].strip()
        if sti_requested > 0 and not approver:
            issue(issues, eid, "DOA-02", "High", "Missing approver")
        if sti_requested > 0 and preparer and preparer == approver:
            issue(issues, eid, "SOD-01", "High",
                  "Preparer is the same person as approver")
        if row["status"].strip() != "Active":
            issue(issues, eid, "DATA-02", "Review",
                  "Review status; validate settlements separately")

    summary = []
    for (department, category), total in sorted(groups.items()):
        summary.append(dict(
            department=department, category=category,
            employee_count=total["count"],
            monthly_payroll_aed=str(total["payroll"].quantize(CENTS)),
            monthly_finance_aed=str(total["finance"].quantize(CENTS)),
            monthly_budget_aed=str(total["budget"].quantize(CENTS)),
            budget_variance_aed=str((total["payroll"]-total["budget"]).quantize(CENTS)),
            indicative_annualized_payroll_aed=str((12*total["payroll"]).quantize(CENTS)),
        ))
    return summary, issues


def main(source=SAMPLE, output_dir=None):
    output_dir = Path(output_dir) if output_dir else ROOT / "outputs"
    output_dir.mkdir(exist_ok=True, parents=True)
    with Path(source).open(newline="", encoding="utf-8") as file:
        records = list(csv.DictReader(file))
    summaries, issues = analyze(records)
    if not summaries:
        raise ValueError("Empty workforce dataset")
    for filename, rows, headers in (
        ("department_workforce_costs.csv", summaries, list(summaries[0])),
        ("control_exceptions.csv", issues,
         ["employee_id", "control", "severity", "detail"]),
    ):
        with (output_dir / filename).open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps(dict(records=len(records), department_category_groups=len(summaries),
                          exceptions=len(issues), output_dir=str(output_dir)), indent=2))
    return summaries, issues


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else SAMPLE,
         sys.argv[2] if len(sys.argv) > 2 else None)
