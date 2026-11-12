# B3 — UAT Strategy, Acceptance Test Cases, Defect Triage and Business Sign-off

## Purpose and evidence levels
The GitHub script exercises 12 **deterministic routing scenarios** against **fictional pre-extracted fields**. That is a **local rules test**, not enterprise UAT. The broader UAT plan below is designed for a future sandbox using actual authorised connectors, real end users and reconciled approval logs. No UAT sign-off is represented as obtained.

## Traceability test matrix
| UAT ID | Requirement(s) | Scenario / synthetic input | Expected result | Evidence / planned approver | Status |
|---|---|---|---|---|---|
| UAT-01 | FR-01, FR-02 | complete invoice, confidence 0.98, matched PO, AED 7.5k | BUSINESS_OWNER_APPROVAL, case ID persisted | case history; AP | **Local rule tested only** |
| UAT-02 | FR-03 | suspected duplicate | HOLD_DUPLICATE; no posting | fingerprint trace; controls | **Local rule tested only** |
| UAT-03 | FR-05 | changed supplier banking instruction | ESCALATE_BANK_CHANGE, manual verification | flagged event; Finance | **Local rule tested only** |
| UAT-04 | FR-02 | extraction confidence 0.70 | REVIEW_EXTRACTION with source document | field evidence; AP | **Local rule tested only** |
| UAT-05 | FR-04 | missing PO | MANUAL_PO_EXCEPTION | case in procurement queue; procurement | **Local rule tested only** |
| UAT-06 | FR-04 | PO mismatch | REVIEW_PO_MISMATCH | reconciliation note; procurement | **Local rule tested only** |
| UAT-07 | FR-06 | matched AED 32k | FINANCE_APPROVAL | authority and segregation; controller | **Local rule tested only** |
| UAT-08 | FR-02, FR-09 | missing invoice number | NEED_INFO | supplier draft + request log; AP | **Local rule tested only** |
| UAT-09 | FR-08 | invoice nearing SLA | alert/escalation exactly once | notification trace; AP manager | Not executed |
| UAT-10 | FR-11 | OCR connection unavailable | manual queue, audit of failure | run history; IT | Not executed |
| UAT-11 | FR-06, FR-07 | initiator tries self-approval | deny permission and log | RBAC + actor trace; controller | Not executed |
| UAT-12 | FR-07, FR-12 | approved case requested for ERP posting | post only on authorised channel; no payment | ERP audit; Finance IT | Not executed |
| UAT-13 | FR-10 | daily cross-entity KPI refresh | numerator/denominator reconcile to source | BI/ERP reconcile; FP&A | Not executed |
| UAT-14 | FR-12 | another entity's user opens case | access denied; DLP policy honoured | IAM log; Security | Not executed |
| UAT-15 | FR-03 | same inbound message replayed twice | one active case, idempotent outcome | event IDs and matching hash; IT | Not executed |

**Separate reproducible local test:** `node test_routing_demo.js` checks every supplied synthetic routing outcome, precedence of bank/duplicate controls, amount boundary and input validation. For simulated run data and coverage see `demonstration_evidence.json`.

## UAT phases
1. **Preparation:** locked BRD and test data owner approval; scrub or synthesize supplier identifiers.
2. **System integration testing:** field extraction error handling, PO lookups, connector failures and access roles.
3. **Business UAT:** AP, Procurement and Finance execute happy, unhappy, override and rollback paths.
4. **Defect triage:** P0 (control bypass, unauthorized posting, data leak), P1 (lost invoice/incorrect routing), P2 (non-critical workflow/UX), P3 (cosmetic).
5. **Retest/regression:** rerun FR-specific scripts and verify audit evidence for each fixed defect.
6. **Decision gate:** AP owner, Finance controller, Security/IT and process sponsor review open defects, evidence, SOP readiness and fallback operation.

## Proposed exit criteria — NOT YET MET
- 100% critical P0/P1 controls pass; zero open P0/P1 defects.
- At least 95% agreed UAT coverage pass; 100% of core safety and no-payment cases pass.
- 100% invoice cases yield audit records; role access reviewed; backup manual queue rehearsal documented.
- Benefits baseline and sampling protocol approved by FP&A.
- Named approvers sign the decision record and pilot scope.

## Blank future sign-off record
| Field | Required value |
|---|---|
| Release/version | TBD |
| Test environment and evidence links | TBD |
| UAT cases executed / passed / failed | TBD |
| Security and controls exceptions | TBD |
| AP process owner signature/date | **PENDING** |
| Controller signature/date | **PENDING** |
| IT/Security approver/date | **PENDING** |
| Decision | **NOT AUTHORISED FOR PRODUCTION** |

No fictional signatories or falsely marked business tests.