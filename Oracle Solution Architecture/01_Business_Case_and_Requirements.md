# 01 - Business case, discovery and requirements

## Fictional client / problem

A six-subsidiary diversified GCC enterprise processes worker transfers, joiners and leavers across disconnected HCM, spreadsheet and finance workflows. Risk: delayed cost allocation, rework, inconsistent master data, incomplete approval trails and difficult executive reporting. All figures below are **illustrative hypotheses**.

## Discovery plan: stakeholders and questions

| Stakeholder | Discovery prompts | Intended output |
|---|---|---|
| CHRO / HR operations | Who approves worker/assignment changes? Which events require controls? | HR ownership + process map |
| Group CFO / financial control | How are cost centers mastered? Who owns financial journals and reconciliations? | Finance ownership + control matrix |
| Enterprise architect | Which licensed Oracle modules, environments and design standards apply? | Architecture constraints / solution options |
| Data/analytics owner | Which fields are trusted, available and reportable? | Data contracts + KPI definitions |
| Cyber / privacy / legal | What is lawful to share, retain and log? Are cross-border transfers involved? | Data/privacy risk decisions |
| Subsidiary process owners | What differs among operating companies? | Standard vs justified local variation |
| Change & training leads | What role-based enablement will users need? | Adoption and support plan |

## Capability and process view

Current state: HR creates assignment change -> local email/spreadsheet -> finance manually rekeys -> reconciliation later -> exceptions unmanaged.

Target state: governed HR request -> validated reference data and role approval -> integration event -> finance-controlled posting / accounting action -> reconciliation evidence -> exception owner -> aggregated dashboard.

**Workflow must differentiate** hiring, transfer, leave and termination; not all events produce finance transactions.

## Requirements traceability (sample)

| ID | Requirement | Design response | Acceptance test |
|---|---|---|---|
| BR-01 | Group-wide canonical worker/assignment change | HCM-owned worker ID + event envelope | UAT-01, UAT-02 |
| BR-02 | Finance controls cost center eligibility | Finance-owned reference and validation API/table | UAT-03 |
| BR-03 | No unapproved changes leave staging | Approval gate and segregation of duties | UAT-04 |
| BR-04 | Duplicate events never double-post | Unique event_id + idempotency store | UAT-05 |
| BR-05 | Exceptions are owned and recoverable | Queue, SLA, replay and escalation | UAT-06 |
| BR-06 | No unnecessary employee PII in analytics | Restricted datasets, pseudonyms, aggregated views | UAT-07 |
| BR-07 | Reconciliation is independently reviewable | HCM/ERP count and financial control totals | UAT-08 |
| BR-08 | Subsidiary-specific rules are governed | Common data model + approved variations | UAT-09 |

## Non-functional requirements (targets to validate)

- Availability, throughput, batch windows and recovery objectives: **TBD at discovery**, not fabricated.
- Encryption in transit/at rest; service accounts least privilege; access and audit logs retained under approved policy.
- Deterministic retry/dead-letter process; replay protection and immutable event IDs.
- Data quality: mandatory IDs, effective dates, reference integrity, duplicate detection, documented reconciliations.
- Documentation: architecture decision records, runbooks, incident ownership, release and rollback criteria.

## Value hypothesis / business case

Establish actual current-state **baselines** before any ROI claims: per-month changes, manual touch time, correction rate, reconciliation cycle time, finance close exceptions and overdue actions.

Hypotheses to test (not outcomes): fewer rekeying errors, faster intercompany change reconciliation, shorter exception cycle times and reduced manual HR/Finance hours. Measure actual results by a named finance or HR benefit owner.

## Solution option tradeoff

- **A / HCM-native workflow with supported integration:** Preferred design hypothesis when Fusion HCM and ERP are both licensed and operational.
- **B / Hybrid legacy finance interface:** Transitional choice if subsidiaries have multiple ERPs; higher mapping and support complexity.
- **C / Spreadsheet-only standardization:** Fast interim governance but does not meet automated reconciliation objectives.

Decision gates: licensing, ERP/HCM module scope, security, data residency, OIC / API fit, integration cost, operational support, change readiness.
