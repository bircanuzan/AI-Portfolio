# Cross-Platform HRIS/HCM Integration Solution Engineering Lab

**Working offline Python standard-library adapter | Synthetic Oracle- and SAP-shaped input | No real vendor connection**

## Unique engineering remit
This project contains the **only runnable vendor-neutral event adapter** in this set. Oracle and SAP architecture projects explain real-world interface selection, whereas this lab checks custom fictional data structures, normalizes them to a shared schema, flags invalid events, suppresses replays within a batch, and creates an auditable review outcome.

## Contents
- [Architecture and quality gates](ARCHITECTURE_AND_TEST_PLAN.md)
- [Python adapter](src/hcm_adapter.py) with Oracle and SAP-shaped **fictional source fields**
- [Synthetic input file](data/synthetic_events.json)
- [Offline unit tests](tests/test_hcm_adapter.py)
- [Evidence protocol](TEST_EVIDENCE.md)

## Run from the project root
```bash
python src/hcm_adapter.py
python -m unittest discover -s tests -v
```

No dependencies beyond Python 3.10+.

## Separation of concerns
- Oracle and SAP cases: product-specific **logical** architecture, technical documentation, integration method selection and operational governance.
- This lab: actual **offline** normalization and rejection logic.
- Existing [Cross-Platform HRIS/HCM Requirements & UAT](../01_Cross_Platform_HRIS_HCM_Requirements_Integration_UAT_Data_Integrity/) project: business requirements, migration data quality and HRIS process controls, not API-specific event normalization.

## Professional evidence boundary
Synthetic identifiers, no PII, API keys, runtime connector, HRMS login, enterprise integration, salary computation, employment decision or actual vendor API payload. A staged 'ACCEPT' means schema checks passed **locally**, not business approval, delivery or production publish.
