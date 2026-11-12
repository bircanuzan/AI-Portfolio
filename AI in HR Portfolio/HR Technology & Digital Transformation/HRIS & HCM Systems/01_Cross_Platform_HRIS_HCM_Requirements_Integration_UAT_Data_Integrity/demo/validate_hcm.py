"""Synthetic cross-platform HRIS pre-migration validations (not production integration)."""
from __future__ import annotations
import csv
import json
from collections import Counter
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
REQUIRED = ("employee_id", "legal_entity", "effective_start")
STATES = {"active", "inactive", "exited", "leave"}

def validate(rows: list[dict[str, str]]) -> dict:
    counts = Counter((r["legal_entity"], r["employee_id"]) for r in rows)
    ids = {(r["legal_entity"], r["employee_id"]) for r in rows}
    flags = []
    for index, row in enumerate(rows, start=2):
        ref = {"source_line": index, "employee_id": row["employee_id"],
               "legal_entity": row["legal_entity"]}
        def flag(code: str, action: str) -> None:
            flags.append({**ref, "code": code, "action": action})
        if any(not row.get(c, "").strip() for c in REQUIRED):
            flag("MISSING_REQUIRED_FIELD", "Hold for HRMS data owner")
        if counts[(row["legal_entity"], row["employee_id"])] > 1:
            flag("DUPLICATE_EMPLOYEE_ENTITY_KEY", "Quarantine duplicate source row")
        try:
            date.fromisoformat(row["effective_start"])
        except (ValueError, TypeError):
            flag("INVALID_EFFECTIVE_DATE", "Correct and revalidate source date")
        if row["manager_employee_id"] and (row["legal_entity"], row["manager_employee_id"]) not in ids:
            flag("UNMAPPED_MANAGER", "Confirm legitimate cross-entity or missing manager mapping")
        if row["employment_status"] not in STATES:
            flag("INVALID_EMPLOYMENT_STATUS", "Map to approved status code")
        if row["pay_change"] == "Y" and row["change_approved"] != "Y":
            flag("UNAPPROVED_PAY_CHANGE", "Do not send to payroll; request authorised approval")
    return {"record_count": len(rows), "flag_count": len(flags),
            "release_status": "HOLD_FOR_HUMAN_REVIEW" if flags else "READY_FOR_HUMAN_SIGNOFF",
            "flags": flags}

def main() -> None:
    with (HERE / "source_employees.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    print(json.dumps(validate(rows), indent=2))

if __name__ == "__main__":
    main()
