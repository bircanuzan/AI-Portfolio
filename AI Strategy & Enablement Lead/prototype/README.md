# Synthetic KYB exception-routing prototype

A minimal, reproducible Python standard-library example for an **AI-ready** KYC/KYB workflow. It intentionally does not call live AI APIs or represent deployed norbloc functionality.

## What is real in this example
- Runs deterministic field validation against structured records using synthetic entities.
- Simulates a document extraction adapter with provided synthetic extracted fields.
- Detects missing identifiers, registry mismatches, stale evidence and inconsistent beneficial ownership totals.
- Routes **all cases to a human reviewer**, distinguishes ordinary from priority review, and creates a content hash for traceability.
- Includes unit tests and executable demo cases.

## What remains a product design, not implemented
OCR/LLM extraction, confidence calibration, MCP integration, live API access, identity verification, sanctions screening, secure storage, access controls, production auditing and model quality evaluation.

## Usage
Python >=3.9, no package installations:
```bash
python regtech_demo.py data/synthetic_cases.json
python -m unittest discover -s tests -v
```

Output JSON is illustrative. The `sha256` is a local evidence digest, not a tamper-proof audit ledger. Sensitive data should never be used in this public demo.

## Replacing mock extraction in a regulated pilot
Use a typed extractor boundary with page/field citations, model + prompt version, confidence/abstention, restricted processing endpoints, encryption, RBAC and human review. Treat OCR text as **untrusted data**. Re-run regression cases and security tests before release.
