# Offline HRIS cross-platform master-data validation lab

All records are **synthetic**. The files simulate a legacy export and business-side pre-migration quality checks, **not** actual Oracle Fusion HCM, Workday, SuccessFactors or payroll data.

Run on Python 3.10+:
```bash
python validate_hcm.py
python -m unittest -v test_validate_hcm.py
```

The validator checks duplicate employee IDs per legal entity, unparseable effective dates, missing manager references, unsupported employment state, missing employing entity and unapproved pay-change records. Flagged records are routed to human review rather than automatically corrected.

No calls to vendor APIs, no actual migration and no pay disbursement.