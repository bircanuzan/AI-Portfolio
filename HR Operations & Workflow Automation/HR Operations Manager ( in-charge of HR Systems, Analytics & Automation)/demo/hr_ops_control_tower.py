"""Offline HRMS/payroll exception controls. Synthetic data, not payroll execution/legal calculation."""
from __future__ import annotations
import csv
import json
from collections import Counter
from decimal import Decimal, InvalidOperation
from pathlib import Path

HERE = Path(__file__).resolve().parent
BLOCKERS = {"UNKNOWN_EMPLOYEE", "DUPLICATE_EMPLOYEE_MASTER", "DUPLICATE_PAYROLL_ROW", "AMOUNT_VARIANCE",
            "MISSING_APPROVAL", "MISSING_BANK_REFERENCE", "EXITED_EMPLOYEE",
            "EOS_REVIEW_PENDING", "WPS_APPLICABILITY_REVIEW", "INVALID_AMOUNT"}

def money(value: str) -> Decimal:
    try:
        amount = Decimal(value)
        if not amount.is_finite() or amount < 0:
            raise ValueError("Non-finite or negative amount")
        return amount
    except (InvalidOperation, TypeError) as exc:
        raise ValueError("Malformed monetary input") from exc

def audit(employees: list[dict[str, str]], payroll: list[dict[str, str]]) -> dict:
    """Validate source rows and propose blocking exceptions; never approve a payment."""
    master_counts = Counter(r["employee_id"] for r in employees)
    master = {r["employee_id"]: r for r in employees}
    duplicates = Counter((r["period"], r["employee_id"]) for r in payroll)
    flags = []
    for line, row in enumerate(payroll, start=2):
        employee_id = row["employee_id"]
        period = row["period"]
        key = {"source_line": line, "period": period, "employee_id": employee_id}
        def add(code: str, reason: str):
            flags.append({**key, "code": code, "reason": reason, "is_blocking": code in BLOCKERS})
        if duplicates[(period, employee_id)] > 1:
            add("DUPLICATE_PAYROLL_ROW", "Repeated employee/period in payroll input")
        if master_counts[employee_id] > 1:
            add("DUPLICATE_EMPLOYEE_MASTER", "Employee master is not unique")
        employee = master.get(employee_id)
        if employee is None:
            add("UNKNOWN_EMPLOYEE", "Payroll employee absent from master")
        else:
            if employee["status"] == "exited":
                add("EXITED_EMPLOYEE", "Exited employee requires authorised final-pay review")
                if row["eos_review_status"] != "complete":
                    add("EOS_REVIEW_PENDING", "Specialist EOS assessment required; no automatic entitlement")
            if employee["wps_applicability"] not in ("applies", "not_applicable"):
                add("WPS_APPLICABILITY_REVIEW", "Compliance must verify actual legal-entity WPS scope")
            try:
                expected = (money(employee["basic_salary_aed"]) +
                            money(employee["allowances_aed"]) +
                            money(row["variable_pay_aed"]) -
                            money(row["deductions_aed"]))
                proposed = money(row["proposed_net_aed"])
                if expected < 0 or abs(expected - proposed) > Decimal("0.01"):
                    add("AMOUNT_VARIANCE", "Proposed amount does not match approved component arithmetic")
            except ValueError:
                add("INVALID_AMOUNT", "Invalid monetary input; manual investigation")
        if row["approval_status"] != "approved":
            add("MISSING_APPROVAL", "Payroll approver has not signed off")
        if not row["bank_reference"].strip():
            add("MISSING_BANK_REFERENCE", "Verified payment reference not provided")
    counts = dict(sorted(Counter(e["code"] for e in flags).items()))
    return {"scope": "fictional offline UAE financial-services HRMS/payroll controls",
            "employee_master_rows": len(employees),
            "payroll_rows": len(payroll),
            "total_flags": len(flags), "flags_by_code": counts,
            "release_gate": "HOLD_FOR_REVIEW" if flags else "HUMAN_REVIEW_REQUIRED",
            "flags": flags}

def load_csv(filename: str) -> list[dict[str, str]]:
    with (HERE / filename).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def main() -> None:
    result = audit(load_csv("employees.csv"), load_csv("payroll_batch.csv"))
    output = HERE / "output"
    output.mkdir(parents=True, exist_ok=True)
    with (output / "summary.json").open("w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    with (output / "exception_register.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["source_line", "period", "employee_id", "code", "reason", "is_blocking"])
        w.writeheader()
        w.writerows(result["flags"])
    print(json.dumps({k: v for k, v in result.items() if k != "flags"}, indent=2))

if __name__ == "__main__":
    main()
