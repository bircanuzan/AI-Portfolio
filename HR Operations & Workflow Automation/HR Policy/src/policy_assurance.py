#!/usr/bin/env python3
"""Offline synthetic policy-release checker and illustrative cost model.

This is an administrative/document-control demonstration, NOT legal review.
Boolean "approvals" in the fixture are fictional test signals.
Python standard library only.
"""
from __future__ import annotations

import argparse
from datetime import date
from decimal import Decimal
import json
from pathlib import Path
import re
from typing import Any


def iso_date(value: str) -> date:
    """Require full ISO date; raise ValueError for invalid dates."""
    return date.fromisoformat(value)


def assess_policy(record: dict[str, Any], as_of: date) -> list[str]:
    """Return deterministic document-control blockers, not legal conclusions."""
    problems: list[str] = []
    if not record.get("policy_id"):
        problems.append("MISSING_POLICY_ID")
    if not re.fullmatch(r"v\d+\.\d+", str(record.get("version", ""))):
        problems.append("INVALID_VERSION")
    if record.get("status") != "APPROVED":
        problems.append("NOT_APPROVED_STATUS")
    if not record.get("local_addendum_attached"):
        problems.append("MISSING_COUNTRY_ADDENDUM")
    legal = record.get("legal_approval") or {}
    if not (legal.get("simulated_signed_off") and legal.get("reviewer") and legal.get("approved_on")):
        problems.append("MISSING_SIMULATED_COUNTRY_LEGAL_SIGNOFF")
    else:
        try:
            approved = iso_date(str(legal["approved_on"]))
            if approved > as_of:
                problems.append("LEGAL_APPROVAL_FUTURE_DATED")
        except (ValueError, TypeError):
            problems.append("INVALID_LEGAL_APPROVAL_DATE")
    if record.get("payroll_impact") and not record.get("payroll_approved"):
        problems.append("PAYROLL_CONTROL_NOT_APPROVED")
    if record.get("hris_impact") and not record.get("hris_approved"):
        problems.append("HRIS_UAT_NOT_APPROVED")
    if not record.get("employee_notice_approved"):
        problems.append("EMPLOYEE_NOTICE_NOT_APPROVED")
    for field, error_code in (
        ("effective_date", "INVALID_EFFECTIVE_DATE"),
        ("next_review", "INVALID_REVIEW_DATE"),
    ):
        try:
            parsed = iso_date(str(record.get(field, "")))
            if field == "next_review" and parsed < as_of:
                problems.append("REVIEW_OVERDUE")
        except (ValueError, TypeError):
            problems.append(error_code)
    return problems


def finance_case(inputs: dict[str, Any]) -> dict[str, str | None]:
    """Illustrative capacity value, correction avoidance and simple payback.

    This calculation does not distinguish cash savings from repurposed capacity;
    that classification requires Finance validation in any real project.
    """
    def d(key: str) -> Decimal:
        return Decimal(str(inputs[key]))

    hours_saved = d("hours_before") - d("hours_after")
    avoided_corrections = d("corrections_before") - d("corrections_after")
    capacity_value = hours_saved * d("hourly_loaded_cost_aed")
    correction_value = avoided_corrections * d("cost_per_correction_aed")
    recurring_value = capacity_value + correction_value
    initial_cost = d("one_time_implementation_aed")
    net_year_one = recurring_value - initial_cost
    payback_months = (initial_cost / recurring_value * 12) if recurring_value > 0 else None

    def money(value: Decimal) -> str:
        return str(value.quantize(Decimal("0.01")))

    return {
        "capacity_value_aed": money(capacity_value),
        "correction_cost_avoided_aed": money(correction_value),
        "recurring_annual_value_aed": money(recurring_value),
        "year_one_net_aed": money(net_year_one),
        "simple_payback_months": money(payback_months) if payback_months is not None else None,
    }


def run(document: dict[str, Any], as_of: date) -> dict[str, Any]:
    items = []
    for record in document.get("policies", []):
        blockers = assess_policy(record, as_of)
        items.append({
            "policy_id": record.get("policy_id"),
            "country": record.get("country"),
            "document_control_readiness": "PASS_SYNTHETIC" if not blockers else "HOLD",
            "blockers": blockers,
        })
    return {
        "disclaimer": "FICTIONAL RECORDS; gates do not assess employment law or confer approval",
        "as_of": as_of.isoformat(),
        "policies_checked": len(items),
        "document_control_results": items,
        "illustrative_financial_model": finance_case(document["financial_scenario"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("register", type=Path, help="Path to synthetic_policy_register.json")
    parser.add_argument("--as-of", default=date.today().isoformat(), help="ISO date YYYY-MM-DD")
    args = parser.parse_args()
    try:
        as_of = iso_date(args.as_of)
    except ValueError:
        parser.error("--as-of requires YYYY-MM-DD")
    with args.register.open(encoding="utf-8") as handle:
        data = json.load(handle)
    print(json.dumps(run(data, as_of), indent=2))


if __name__ == "__main__":
    main()
