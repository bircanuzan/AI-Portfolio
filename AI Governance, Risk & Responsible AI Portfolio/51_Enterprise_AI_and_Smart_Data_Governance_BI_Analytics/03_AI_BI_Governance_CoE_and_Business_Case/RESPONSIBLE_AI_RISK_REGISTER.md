# Responsible AI, data governance and controls — DESIGN REGISTER

**Context:** illustration for a fictional UAE insurer. No legal conclusion; applicable UAE privacy, insurance, cyber/security and AI guidance must be interpreted by qualified insurer counsel and regulator-facing compliance.

| ID | Risk | Required prevention / detection | Owner | Stop rule |
|---|---|---|---|---|
| R01 | PII leaked into training/BI | whitelist, classification, DLP, role access, privacy assessment | DPO + Data Owner | halt on unauthorized personal data |
| R02 | Unfair handling across customer segments | independent bias review using legally permitted relevant groups; do not substitute submission_channel | Model Risk | no customer-impacting use absent approval |
| R03 | Synthetic-label overfitting | external real-world validation, independent labels and calibration | Model Validation | no production use on toy metrics |
| R04 | Misleading auto-denial or fraud accusation | human adjudicator; no automated adverse outcomes | Claims Owner | immediate disable when routing exceeds authority |
| R05 | Data drift / stale policy | versioning, freshness checks, drift & recalibration alerts | Data Platform + Model Risk | route all to manual fallback |
| R06 | Hallucination in future LLM/OCR | claim-source citations, confidence gates and documented human verification | AI CoE + Claims | refuse unsupported extraction decisions |
| R07 | Azure/InsurTech supply-chain exposure | data processing terms, residency review, security tests, audit rights, exit plan | Security + Procurement | vendor go-live denied without sign-off |
| R08 | Model monitoring not actionable | KPI owner, alert thresholds, escalation matrix, incident drills and rollback | Operations | pause model recommendations |
| R09 | BI self-service data leakage | certified semantic layer, RLS, audited export, minimum group size | BI + DPO | revoke access pending investigation |

## Human-in-the-loop policy
- The AI may **recommend routing for staff inspection** only.
- All claim assessment, coverage, payment, complaints and fraud allegations remain with competent human decision-makers.
- Record timestamp, model version, score, recommendation, human decision, reason and any override **only in appropriately protected enterprise systems**.
- Give reviewers an override and escalation route; test fallback to full manual processing.
- Evaluate false negatives, review burden and customer impact before considering any regulated pilot.

## Validation specification
Data provenance, holdout/time-split design (not synthetic random split in production), leakage audit, calibration, uncertainty, segment outcomes, adversarial/OOD tests, operational trial, privacy/security approvals. No fairness or impact certification has been performed in this repository.
