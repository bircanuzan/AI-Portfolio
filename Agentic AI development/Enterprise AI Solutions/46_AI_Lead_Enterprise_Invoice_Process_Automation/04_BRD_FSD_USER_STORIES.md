# B1 — Business Requirements Document (BRD), FSD and Agile User Stories

## BRD-01: Project charter
- **Sponsor (proposed):** Group CFO delegate and Director of AI; **process owner:** Group AP manager.
- **Objective:** reduce avoidable manual rekeying, strengthen auditability and ensure every invoice has accountable routing.
- **In scope:** intake validation, case IDs, proposed document extraction, human review, PO reconciliation, thresholds, exceptions, notifications, audit export, operational KPI timestamps.
- **Out of scope:** master-data bank updates, autonomous PO changes, autonomous supplier payments, legal/tax advice, production integration without ERP sign-off.
- **Constraints:** different legal entities, privacy-sensitive documents, segregation of duties, vendor onboarding dependencies, UAE retention and access requirements subject to legal assessment.

## Functional requirements and traceability
| Requirement | Priority | Specification | Acceptance / evidence |
|---|---|---|---|
| FR-01 | Must | Issue immutable case ID; log entity, received-at, channel and document fingerprint | no duplicate case IDs; event log |
| FR-02 | Must | Extract proposed vendor, invoice number, amount, VAT fields, PO number with per-field confidence and visible source | never auto-trust extraction; correctable review |
| FR-03 | Must | Flag duplicate invoice number per vendor/entity; flag hash duplicate | suspected duplicates HOLD |
| FR-04 | Must | Compare PO amount/vendor/receipt only from authorised ERP read-only interface | mismatch to exception |
| FR-05 | Must | Route supplier bank-detail changes to supplier-master-data team, not AI/AP auto-edit | hard-stop & dual control |
| FR-06 | Must | Apply entity-specific delegated approval limits and segregation of duties | actor cannot approve own submission |
| FR-07 | Must | Human approval required before posting; payments always outside automation scope | deny posting without authorisation |
| FR-08 | Must | Provide status queue, age, escalation due date, owner, audit trail | reconstruct entire decision history |
| FR-09 | Should | Notify vendor of missing fields using approved template | no confidential internal notes disclosed |
| FR-10 | Should | Publish daily workload and first-pass correctness scorecard | transparent numerator, denominator |
| FR-11 | Must | Fallback manual queue when OCR/integration fails | no silent case loss |
| FR-12 | Must | Retention, RBAC and DLP safeguards agreed before go-live | security and legal gate |

## Data dictionary (minimum)
`case_id` string unique; `entity_id` controlled category; `vendor_id` pseudonymous reference; `invoice_number` string; `amount_aed` decimal (ISO original currency also recorded); `po_present` boolean; `po_match` boolean; `duplicate_flag` boolean; `bank_change_flag` boolean; `vat_valid` boolean; `field_confidence` numeric 0–1; `approval_status` enum; `owner` role; `created_at` and `updated_at` UTC. No banking information in analytical exports.

## Business rules
| ID | Condition | Proposed decision | Owning team |
|---|---|---|---|
| BR-01 | mandatory values absent or invalid amount | NEED_INFO | AP intake |
| BR-02 | suspected duplicate | HOLD_DUPLICATE | AP + controls |
| BR-03 | bank-detail change flag | ESCALATE_BANK_CHANGE | Vendor master-data + fraud control |
| BR-04 | invalid VAT/tax markers | REVIEW_TAX | Tax/AP |
| BR-05 | low extraction confidence under 0.90 | REVIEW_EXTRACTION | AP |
| BR-06 | missing PO | MANUAL_PO_EXCEPTION | Procurement |
| BR-07 | PO mismatch | REVIEW_PO_MISMATCH | Procurement + business owner |
| BR-08 | amount above AED 25,000 | FINANCE_APPROVAL | Controller |
| BR-09 | matched <= AED 25,000 | BUSINESS_OWNER_APPROVAL | budget owner |
| BR-10 | *any* accepted invoice | human approval before posting | authorised approver |
| BR-11 | SLA elapsed for assigned category | escalate to role owner with timestamp | AP supervisor |
| BR-12 | connector/model service fails | fail closed to manual queue, no payment | IT ops |

**Thresholds are invented for modelling and MUST be replaced by approved delegation-of-authority per entity and amount/currency.** Priorities are illustrative; bank-change/duplicate hard stops take precedence over amount-based routing.

## User stories with explicit acceptance criteria
1. **As an AP clerk**, I want each invoice to have a unique case so no email disappears. **Given** a valid intake, **when** submitted, **then** a unique case is created, owned and timestamped.
2. **As an AP reviewer**, I need to see each proposed extraction with evidence. **Given** confidence below 0.90, **when** routed, **then** a human review task opens with original PDF and highlighted source.
3. **As a procurement officer**, I want unmatched POs isolated. **Given** mismatch, **when** checked, **then** no posting/automatic payment occurs.
4. **As a financial controller**, I want high-value cases escalated. **Given** AED >25k, **when** all checks pass, **then** controller review is requested and approval is audited.
5. **As a fraud control owner**, I want bank changes blocked. **Given** any bank change, **when** submitted, **then** the system blocks straight-through paths.
6. **As a business-unit owner**, I want visible ageing. **Given** a case near SLA, **when** threshold approaches, **then** the owner and supervisor see an alert.
7. **As IT operations**, I want safe failure. **Given** a connector timeout, **when** ingestion fails, **then** it is retryable and assigned to a monitored dead-letter queue.
8. **As the Director of AI**, I want measured adoption and benefits. **Given** a released pilot, **when** metrics are viewed, **then** actuals and baselines use identical definitions.

## Non-functional acceptance
- Access: role/least-privilege per legal entity; service principals scoped.
- Integrity: tamper-evident case history and repeatable mapping of statuses.
- Privacy: retention/deletion and data residency reviewed; no supplier banking data in LLM prompts by default.
- Availability/recovery: approved RTO/RPO and manual fallback before launch; no unsourced target.
- Performance: latency baseline and target to be agreed from sample workloads.
- Testing: trace every FR to UAT and audit evidence; no critical safety failures permitted.

## Vendor-neutral solution interfaces
1. Microsoft 365 / portal → controlled document store.
2. Optional AI Builder Document Processing / UiPath DU → extracted field candidates; provenance/confidence.
3. Power Automate / UiPath / internal orchestrator → case routing and approvals.
4. ERP read-only PO/vendor check → **separate** posting process after human authorization.
5. Power BI → derived status/benefit reporting with restricted access.

The repository implements **only** a local deterministic routing demonstration, not these platform interfaces.