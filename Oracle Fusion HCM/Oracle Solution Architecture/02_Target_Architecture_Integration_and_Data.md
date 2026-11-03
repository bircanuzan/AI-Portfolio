# 02 - Target solution architecture, integration and data

## Logical architecture (not vendor-validated deployment design)

**Presentation:** HR and Finance user experiences, role-based self-service, exception dashboard, executive KPIs.

**Business process:** HR worker/assignment controls, approvals, finance mapping/reconciliation, issue resolution and audit.

**Applications:** Oracle Fusion Cloud HCM; Oracle Fusion Cloud ERP Financials where adopted; other subsidiary source systems subject to inventory.

**Integration:** OIC candidate / supported Oracle APIs / FBDI or other file interfaces where documented; mapping and policy validation, retries, idempotency, reconciliation. Exact endpoints and supportability require tenant and product verification.

**Data and analytics:** Reference/master ownership, event contract, mapping tables, control totals and curated analytics layer.

**Cross-cutting:** IAM, encryption, logging, observability, security/privacy control assessment, release management and human control.

## Source-of-truth and ownership matrix

| Domain | Candidate system of record | Accountable owner | Privacy / approval boundary |
|---|---|---|---|
| Person / worker ID and employment status | Oracle Fusion HCM | HR master data | Limit personal identifiers to operational necessity |
| Assignment and effective date | Oracle Fusion HCM | HR operations | Change approval and audit trail |
| Legal entity and HR organization | HCM / governed enterprise reference | Group HR + Finance | Subsidiary mapping approval |
| GL cost center and chart of accounts | Oracle ERP / Finance master data | Group Finance | Finance-owned eligibility validation |
| Financial postings and ledger | Oracle ERP Financials | Finance controls | Never let an LLM approve/post |
| Integration delivery status | Integration/observability store | Group IT | Protected operational metadata |
| BI facts and executive dashboards | Curated reporting layer | Data governance / business metric owner | Aggregation and role-based access |

## Canonical illustrative event

```json
{
  "event_id": "EVT-001",
  "worker_id": "W-001",
  "event_type": "TRANSFER",
  "effective_date": "2026-11-03",
  "subsidiary": "SUB-A",
  "cost_center": "CC-100",
  "approved_by": "HR-MGR-1",
  "finance_reference_valid": true
}
```

Synthetic IDs; deliberately exclude names, identity numbers, medical, compensation and other unnecessary personal fields.

## Interface contract and controls

1. Capture HCM event only after configured HR approvals.
2. Validate schema, allowed event type, effective date, unique event ID, subsidiary and finance-owned cost-center reference.
3. Route invalid or unapproved records to an accountable exception owner with reason code. Never silently drop.
4. Translate canonical event into the **approved** finance-side representation; never assume an HCM change itself is an ERP posting.
5. Acknowledge delivery; record correlation ID, timestamp, version and processing status.
6. Reconcile source events, accepted outputs, rejected events and explicitly excluded types. Replays must be idempotent.
7. Expose role-appropriate reconciliation counts and exceptions to analytics without broad raw employee-data access.

**Failure modes:** timeouts, invalid reference, duplicate event, schema drift, late effective dates, disconnected subsidiaries, inaccessible target, missing approval and partial downstream acceptance.

**Operational controls:** bounded retry with backoff; dead-letter/exception queue; alert threshold; remediation owner; documented replay with audit record; change review for mapping and schema updates.

## Reporting design

- Workforce changes received / accepted / rejected by subsidiary and event type.
- Missing-approval rate and invalid cost-center rate.
- Median event-to-acknowledgment time **once measured**.
- Open exceptions by age and accountable owner.
- Cross-system reconciled / unreconciled counts; close exception backlog.
- Drill-down only for authorized users, with de-identified reporting defaults.

## Decisions still required

Oracle product licensing and platform topology, actual data/API availability, release cadence, integration throughput, data location, identity-provider ownership, privacy assessment, retention rules, group vs subsidiary control balance and disaster recovery needs.

This is an architecture *proposal*, not tested Oracle documentation or a certification of design supportability.
