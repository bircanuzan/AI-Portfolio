"""Synthetic HRMS-to-payroll pre-run exception report (not a payroll calculator)."""
from __future__ import annotations
import csv
import json
from collections import Counter
from pathlib import Path

DATA_FILE = Path(__file__).with_name('sample_hrms_payroll.csv')


def audit(rows: list[dict[str, str]]) -> dict:
    counts = Counter(row['employee_id'] for row in rows)
    exceptions = []
    for line, row in enumerate(rows, start=2):
        employee = row['employee_id']
        def flag(code: str, action: str):
            exceptions.append({'source_line': line, 'employee_id': employee,
                               'control': code, 'action': action})
        if counts[employee] > 1:
            flag('DUPLICATE_EMPLOYEE', 'Investigate duplicate; block payroll upload')
        if not row['bank_reference'].strip():
            flag('MISSING_BANK_REFERENCE', 'Obtain verified payment details; hold release')
        if row['approved_gross_aed'] != row['proposed_payment_aed']:
            flag('GROSS_PAYMENT_VARIANCE', 'Reconcile and obtain documented approval')
        if row['payroll_status'] != 'approved' and float(row['proposed_payment_aed']) > 0:
            flag('PAYMENT_NOT_APPROVED', 'Hold processing until authorised')
        if row['employment_status'] == 'exited' and row['eos_review'] != 'complete':
            flag('EOS_REVIEW_PENDING', 'Request UAE-law review by qualified HR/payroll specialist')
    by_control = dict(sorted(Counter(e['control'] for e in exceptions).items()))
    return {'scope': 'synthetic HRMS export; not UAE statutory calculations',
            'rows_checked': len(rows), 'unique_employee_ids': len(counts),
            'total_control_flags': len(exceptions), 'flags_by_control': by_control,
            'exceptions': exceptions, 'release_recommendation': 'HOLD if flags exist' if exceptions else 'Ready for authorised review'}


def main():
    with DATA_FILE.open(newline='', encoding='utf-8') as handle:
        rows = list(csv.DictReader(handle))
    print(json.dumps(audit(rows), indent=2))


if __name__ == '__main__':
    main()
