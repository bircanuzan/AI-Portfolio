# Governance, compliance, risk-control mapping and UAT

## Role accountability
- **HR Operations Lead (A):** HRMS employee master integrity, people process policy, HR release recommendation.
- **Finance/Payroll Controller (A for payments):** reconciliations, salary disbursement authorisation and ledger evidence.
- **Compliance/Legal (A for interpretation):** labour regime, WPS applicability, savings/EOS rules, privacy obligations.
- **IT/InfoSec (R):** integration identity/access, backup, logging, secrets, incident containment and recovery.
- **HR Data/BI Owner (R):** approved semantic models, restricted dashboard access and data-quality refresh.
- **Managers/Employees (C/I):** source requests, consent/notice processes as applicable, service feedback.

## Risk register — initial case study assumptions
| Risk ID | Scenario | Impact | Key control | Evidence |
|---|---|---|---|---|
| R01 | Wrong entity or employee paid | High | Reconcile employee ID/entity against HRMS | Batch validation exceptions |
| R02 | Payroll net variance | High | Amount reconciliation and dual approval | Approved pay components |
| R03 | Payment to exited employee | High | Status/effective-date gate, EOS handoff | Exit workflow and expert review |
| R04 | WPS applicability assumed incorrectly | High | Legal/regulatory determination per entity | Signed legal memo and scope matrix |
| R05 | Sensitive records disclosed through BI/AI | High | Minimisation, access policy, logging, DLP | Access test, DPIA if applicable |
| R06 | Unauthorised salary master change | High | Maker-checker and audit log | HRMS change ticket |
| R07 | Employee service SLA failure | Medium | Ticket owner, reminder, escalation | Service event log |
| R08 | Model/automation initiates payment | Critical | No transfer credential; human-only release | Architecture/security test |

## UAT traceability
| Test | Trigger | Expected |
|---|---|---|
| UAT-01 | Duplicate employee line for period | Blocking duplicate flag |
| UAT-02 | Proposed amount mismatches approved components | Blocking monetary variance |
| UAT-03 | Pending approval | Blocking approval flag |
| UAT-04 | Missing bank reference | Blocking payment-data check |
| UAT-05 | Exited employee with pending EOS | Hold and route to qualified reviewer |
| UAT-06 | Unverified WPS applicability | Compliance review; no automatic exemption |
| UAT-07 | Employee does not exist in master | Hold the line and investigate |
| UAT-08 | Clean sample pay line | No demo exceptions; still human-reviewed |
| UAT-09 | User without payroll role opens detailed dashboard | Access denied, logged |
| UAT-10 | HR helpdesk AI asked for legal entitlement | Refuse automatic decision, escalate |
| UAT-11 | Payroll feed duplicated / integration retried | Idempotent key prevents repeat release |
| UAT-12 | Payment batch bank/GL totals mismatch | Reconciliation prevents release |

## Go-live sign-off
Obtain named signoffs from HR, Finance, IT Security and Compliance/Legal; document intended jurisdiction and WPS status; pass all high/critical UAT cases; evidence payroll-to-ledger reconciliation; complete RBAC/privacy reviews; maintain rollback and incident response; train HR and manager users; monitor first two cycles with enhanced human review.

UAE personal data framework reference: https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws — operational legal obligations require current professional assessment.

**Evidence limitation:** This design contains no real client records, no actual employer control test, and no regulator attestation.