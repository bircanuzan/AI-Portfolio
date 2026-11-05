# 03 — To-be workflow, automation, AI prioritization and acceptance

## Workflow redesign
**Trigger** customer asks to return -> query source transaction -> verify item/customer/payment -> apply versioned return and promotion policy -> run duplicate refund check -> route unresolved case to authorized reviewer -> approved refund request -> update OMS/WMS -> post finance -> CRM status -> reconcile -> emit dashboard event.

## AI vs simpler automation
- Rules-based: receipt lookup, return-window rules, deterministic refunds, reconciliation.
- RPA (UiPath / Automation Anywhere / Power Automate candidate): only for legacy UI where approved APIs unavailable; avoid brittle screen automation if possible.
- GenAI: optional support-agent summary of permitted case evidence with grounded citations and no autonomous refunds.
- ML: only after trusted history, consent and model evaluation, for exception risk ranking; humans decide outcomes.

## Functional requirements
| ID | Requirement | Acceptance |
|---|---|---|
| FR-01 | Read correct original sale and promotion version | Reference source and timestamp |
| FR-02 | Apply published return/refund rules | Refund calculation trace |
| FR-03 | Identify duplicate refund | Reject/hold duplicate idempotency key |
| FR-04 | Route exception | Manager receives context, can approve/reject with reason |
| FR-05 | Post stock and finance update | Transactions reconcile or queue for recovery |
| FR-06 | Audit user and automation actions | Logs include actor, time, rule version and outcome |

## Non-functional requirements
Access via least privilege and MFA where appropriate, protected payment data, encrypted transport, retry/backoff, idempotency, failure monitoring, accessibility, data residency verification, segregation of duties and approved rollback procedure.

## User story
"As a store supervisor, I need disputed promotional refunds to pause for review with all relevant evidence so customers receive consistent decisions and we avoid duplicate refunds."

**Acceptance tests:** successful routine return; missing receipt; promotion mismatch; inventory update timeout; duplicate payment request; invalid authorization; malformed customer data; escalation override with reason. No live deployment claimed.

## Prioritization (impact vs feasibility)
Start with deterministic POS/OMS/WMS policy validation and reconciliation, then automate approvals, then consider AI summaries. Human decision boundaries take precedence over speculative AI savings.
