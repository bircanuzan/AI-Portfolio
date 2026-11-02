# Test evidence — 2 November 2026

The files audit.py, test_audit.py and sample_hrms_payroll.csv were created as an independent offline synthetic prototype and executed locally using Python unittest.

Command:
\`\`\`
python -m unittest -v test_audit.py
\`\`\`

Observed test summary:
\`\`\`
test_clean_row_is_not_flagged ... ok
test_duplicate_and_eos ... ok
test_expected_sample_flags ... ok
Ran 3 tests
OK
\`\`\`

Observed sample output summary:
\`\`\`json
{
  "rows_checked": 7,
  "unique_employee_ids": 6,
  "total_control_flags": 6,
  "flags_by_control": {
    "DUPLICATE_EMPLOYEE": 2,
    "EOS_REVIEW_PENDING": 1,
    "GROSS_PAYMENT_VARIANCE": 1,
    "MISSING_BANK_REFERENCE": 1,
    "PAYMENT_NOT_APPROVED": 1
  },
  "release_recommendation": "HOLD if flags exist"
}
\`\`\`

**Interpretation:** these are six **control flags** (not necessarily six different employees) deliberately injected into the seven synthetic rows. The duplicate ID is flagged on both rows. This is not validation of payroll accuracy or UAE EOS calculations, and not a deployed HRMS payroll control.