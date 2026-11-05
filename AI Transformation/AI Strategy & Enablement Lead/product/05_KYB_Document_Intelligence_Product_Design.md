# Proposed KYB document intelligence: product concept

**Context:** Digital business onboarding and KYC/KYB data exchange where provenance, access rights and record versions matter. This is an independent reference design, **not an assertion about Fides, Sancus or Atlas internals**.

## User problem
Analysts reconcile registry documents, beneficial-ownership declarations and customer submissions. A wrong field or overlooked mismatch can delay onboarding or increase regulatory risk.

## Proposed value stream
1. Authorized client uploads evidence and grants scope-limited processing permissions.
2. System stores original encrypted document, version, issuer/source and hash.
3. OCR/document extraction creates candidate fields with page-level provenance and uncertainty.
4. Deterministic cross-checks compare registry IDs, legal entity names, jurisdictions, ownership totals, dates and document types.
5. Optional anomaly model **prioritizes** review with explanations; does not make an adverse decision.
6. Human analyst reviews source documents, corrects extraction, records rationale and signs off.
7. Versioned evidence, outputs and reviewer decision are logged and exportable under access controls.

## Sample target architecture
```text
Client portal / API
  -> secure evidence store + permission ledger
  -> document classifier / OCR / extraction adapter
  -> structured validation + anomaly signals
  -> analyst review queue (source highlighting, provenance)
  -> approved decision -> core onboarding workflow
  -> immutable/event-based audit trail + performance monitoring
```

## Data contract examples
`case_id, evidence_id, version_id, source_file_hash, extracted_field, normalized_value, confidence, source_page, model_id, model_version, prompt_version, validation_flags, reviewer_id, disposition, timestamp`

## Risk-aware evaluation
- Field-level precision/recall by document type, language, quality and jurisdiction.
- Mismatch detection sensitivity **and** false-positive cost.
- Case-handling time inclusive of manual corrections.
- Unsupported-field / hallucination rate, abstention rate, adverse subgroup variation.
- Security leakage, prompt-injection susceptibility, model drift and audit replayability.

## Release gates
No live customer PII in prototype. Before restricted deployment: legal/privacy/data-processing review; client consent/contract review; access controls; pen-testing; human override; rollback; evidence retention schedule; disaster recovery; minimum acceptable offline evaluation by cohort; and approved operational runbook.

## Prototype linked here
[Runnable synthetic KYB workflow](../prototype/README.md) demonstrates the **validation, exception routing and audit** layers only. Document extraction is mocked. It does **not** establish model extraction accuracy or production readiness.
