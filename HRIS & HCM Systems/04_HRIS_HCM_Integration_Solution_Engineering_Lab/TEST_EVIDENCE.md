# Synthetic test evidence and truthfulness log

The repository includes deterministic unittest cases with no external services. Reproduce with:
```bash
python src/hcm_adapter.py
python -m unittest discover -s tests -v
```

Evidence is limited to **offline schema validation and mapping**. It does not prove Oracle HCM extraction, SuccessFactors replication, API authentication, production integration, data residency, vendor application configuration, employee-payroll accuracy or compliance.

A production readiness claim requires genuine versioned tenant evidence, signed end-to-end UAT, valid permissions, vendor documentation and operational logs.
