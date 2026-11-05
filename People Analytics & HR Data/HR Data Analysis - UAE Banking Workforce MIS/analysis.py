"""Synthetic month-end HR MIS and workforce planning example.

Offline standard-library demo. NOT ADIB/CBUAE data or a regulatory submission.
No real employee details or production access are involved.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
CUTOFF = "2026-10-31"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def number(row: dict, field: str) -> float:
    try:
        v = float(row[field])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid numeric {field}: {row}") from exc
    if not math.isfinite(v) or v < 0:
        raise ValueError(f"negative or nonfinite {field}: {row}")
    return v


def check_unique(rows: list[dict], key: str, label: str) -> None:
    values = [r.get(key, "") for r in rows]
    if any(not x for x in values) or len(values) != len(set(values)):
        raise ValueError(f"missing or duplicate {label} key: {key}")


def validate(employees: list[dict], positions: list[dict],
             requisitions: list[dict], cutoff: str) -> None:
    if not positions:
        raise ValueError("funded positions plan must not be empty")
    check_unique(employees, "employee_id", "employee")
    check_unique(positions, "division", "position")
    check_unique(requisitions, "req_id", "requisition")
    divs = {p["division"] for p in positions}
    for label, rows in (("HRMS", employees), ("position", positions), ("requisition", requisitions)):
        for row in rows:
            if row.get("as_of") != cutoff:
                raise ValueError(f"{label} inconsistent reporting cutoff")
            if row.get("division") not in divs:
                raise ValueError(f"{label} unmapped division")
    for r in employees:
        if r.get("status") not in {"Active", "Inactive"}:
            raise ValueError("unmapped HRMS employee status")
        if r.get("emiratisation_group") not in {"Emirati", "Other"}:
            raise ValueError("unmapped employee classification")
        fte = number(r, "fte")
        if fte > 1:
            raise ValueError("worker FTE above simplified valid range")
        number(r, "annual_cost_aed")
    for r in positions:
        if r.get("approval_status") != "Approved":
            raise ValueError("funded plan contains unapproved allocation")
        number(r, "funded_fte")
        number(r, "budget_annual_aed")
        target = number(r, "illustrative_target_pct")
        if target > 100:
            raise ValueError("target must be in 0..100")
    for r in requisitions:
        if r.get("approval_status") not in {"Approved", "Pending", "Rejected"}:
            raise ValueError("unknown requisition approval state")
        number(r, "requested_fte")
        number(r, "expected_annual_cost_aed")


def summarise(employees: list[dict], positions: list[dict],
              requisitions: list[dict], cutoff: str = CUTOFF) -> dict:
    """Return auditable group/division MIS calculations from fictional inputs."""
    validate(employees, positions, requisitions, cutoff)
    active = [r for r in employees if r["status"] == "Active"]
    results = []
    for p in sorted(positions, key=lambda x: x["division"]):
        div = p["division"]
        staff = [r for r in active if r["division"] == div]
        fte = sum(number(r, "fte") for r in staff)
        emirati_fte = sum(number(r, "fte") for r in staff if r["emiratisation_group"] == "Emirati")
        cost = sum(number(r, "annual_cost_aed") for r in staff)
        funded = number(p, "funded_fte")
        budget = number(p, "budget_annual_aed")
        target = number(p, "illustrative_target_pct")
        approved_requests = sum(number(r, "requested_fte") for r in requisitions
                                if r["division"] == div and r["approval_status"] == "Approved")
        pending_requests = sum(number(r, "requested_fte") for r in requisitions
                               if r["division"] == div and r["approval_status"] == "Pending")
        open_funded = max(0.0, funded - fte)
        # Synthetic target-gap denominator: funded capacity, not an official legal basis.
        target_gap = max(0, math.ceil(funded * target / 100 - emirati_fte - 1e-9))
        results.append({
            "division": div, "actual_headcount": len(staff),
            "actual_fte": round(fte, 2), "funded_fte": round(funded, 2),
            "vacancy_fte": round(open_funded, 2),
            "signed_capacity_gap_fte": round(funded - fte, 2),
            "annualized_actual_cost_aed": round(cost, 2),
            "annual_budget_aed": round(budget, 2),
            "cost_variance_aed": round(cost - budget, 2),
            "emirati_fte": round(emirati_fte, 2),
            "emirati_fte_share_pct": round(100 * emirati_fte / fte, 2) if fte else None,
            "illustrative_target_pct": target,
            "illustrative_target_gap_fte": target_gap,
            "approved_requisitions_fte": round(approved_requests, 2),
            "pending_requisitions_fte": round(pending_requests, 2),
            "scenario_fte_after_approved_hires": round(fte + min(approved_requests, open_funded), 2),
            "capacity_exception": "active_over_funded" if fte > funded else None,
        })
    actual = sum(r["actual_fte"] for r in results)
    emirati = sum(r["emirati_fte"] for r in results)
    return {
        "report_cutoff": cutoff,
        "classification": "FICTIONAL_SYNTHETIC_DEMONSTRATION",
        "group": {
            "actual_headcount": sum(r["actual_headcount"] for r in results),
            "actual_fte": round(actual, 2),
            "funded_fte": round(sum(r["funded_fte"] for r in results), 2),
            "vacancy_fte": round(sum(r["vacancy_fte"] for r in results), 2),
            "annualized_actual_cost_aed": round(sum(r["annualized_actual_cost_aed"] for r in results), 2),
            "annual_budget_aed": round(sum(r["annual_budget_aed"] for r in results), 2),
            "cost_variance_aed": round(sum(r["cost_variance_aed"] for r in results), 2),
            "emirati_fte": round(emirati, 2),
            "emirati_fte_share_pct": round(100 * emirati / actual, 2) if actual else None,
            "approved_requisitions_fte": round(sum(r["approved_requisitions_fte"] for r in results), 2),
            "pending_requisitions_fte": round(sum(r["pending_requisitions_fte"] for r in results), 2),
            "scenario_fte_after_approved_hires": round(sum(r["scenario_fte_after_approved_hires"] for r in results), 2),
        },
        "divisions": results,
        "reporting_warning": "All divisions, costs, targets and metrics are fictional. No legal or regulatory compliance determination. Approved requests are not completed hires.",
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Run fictional month-end HR data analyst MIS demo")
    ap.add_argument("--cutoff", default=CUTOFF)
    args = ap.parse_args()
    out = summarise(
        read_csv(HERE / "data" / "employee_snapshot.csv"),
        read_csv(HERE / "data" / "funded_positions.csv"),
        read_csv(HERE / "data" / "requisitions.csv"),
        cutoff=args.cutoff,
    )
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
