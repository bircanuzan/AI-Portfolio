# 03 | BRD, UAT, CBUAE Controls, Adoption and Audit

## Representative business requirements (synthetic)
- **BR-001:** Extract trade-finance fields into a review interface with source-document evidence.
- **BR-002:** Any low-confidence amount, beneficiary or date is flagged for authorised manual review.
- **BR-003:** No autonomous payment, credit or market execution is permitted.
- **BR-004:** Log model version, input document reference, exceptions, human approval and access events.
- **BR-005:** Require bank-authorised security classification, data retention and access controls.

## UAT cases and release criteria
| Case | Test | Expected | Release gate |
|---|---|---|---|
| UAT-01 | Normal synthetic document | Correct extract and traceable source | Business QA pass |
| UAT-02 | Beneficiary/amount mismatch | Escalate with no transaction | Critical control |
| UAT-03 | Unauthorised user requests file | Reject and log | Security |
| UAT-04 | Integration unavailable | Manual fallback, no silent loss | Business continuity |
| UAT-05 | Model uncertainty | Human review queue, no auto decision | Model risk |

Release requires traceability BRD -> UAT -> defects -> sign-off, unresolved critical defect count = 0, approved change impact, evidence of controls, rollback plan and owner acceptance.

## Control and audit register (illustrative, NOT a compliance certification)
**CBUAE alignment:** applicable obligations must be validated against current rules by the bank's Compliance/Legal teams. Consider outsourcing and third-party risk, information security, privacy, model risk, operational resilience and internal controls. Do not claim formal CBUAE endorsement.

| Risk | Proposed preventive/detective control | Evidence owner |
|---|---|---|
| Confidential wholesale client data exposed to AI service | Classification, minimisation, environment isolation, least privilege, retention controls | Privacy / InfoSec |
| Hallucinated or incorrect financial interpretation | Source evidence, offline challenge set, manual approval, drift monitoring | Business / Model Risk |
| Unrecorded override | Versioned immutable decision/override logs | Technology / Operations |
| Third-party data processing | Due diligence, contractual control schedule, restricted keys and access review | Procurement / Legal / InfoSec |
| Unclosed audit issue | Action owner, deadline, tested remediation evidence, independent validation | Action Owner / Internal Audit |

## Change impact and adoption
Audience: Relationship Managers, transaction operations, treasury SMEs, risk/control teams and IT support. Conduct role-impact workshops, readiness baseline, approved AI-use and escalation training, champions network, go-live communications and 30/60/90-day adoption reviews. Track eligible-user activation, task accuracy, workload, incident frequency, SOP deviations and realised business value.

**Confidentiality:** No actual CBD, HSBC, customer or third-party bank data appears in this repository.
