# Operational problem -> automation requirements | skills evidence

> **Evidence boundary:** Independent portfolio reference implementation using synthetic data. The authoring, code and design artifacts in this repository demonstrate an approach to requirements analysis and prototyping. They do not establish that Zapier, Make, Retool, n8n, HRIS/payroll endpoints, or a production client system were deployed, nor that these specific automations were used at a previous employer.

## 1. Problem discovery and translation to implementable requirements

**Representative operational problem:** Global mobility requests enter through fragmented email, employee portals, HRIS notifications and EOR case queues. Staff manually classify cases and copy metadata, may miss duplicate requests, and need specialist approval for immigration, identity, payroll or employment changes.

| Operational pain point | Business requirement | System / automation specification | Acceptance criterion | Demonstrable evidence |
| --- | --- | --- | --- | --- |
| Unstructured intake and inconsistent routing | Route every approved case to an accountable owner | Versioned JSON schema; strict field allowlist; classify category, country, risk and permissible action | Known fixture routes deterministically; unknown category escalates | `src/mobility_pipeline.py`, `tests/test_mobility_pipeline.py` |
| Double processing from webhook retries | Prevent duplicate side effects | Deduplicate by `tenant_id:event_id`; production needs transactional storage and case versioning | Repeated synthetic event returns `duplicate_event` | Python pipeline and tests |
| Missing or conflicting payroll dates | Detect cross-system mismatch without auto-changing payroll | Map HRIS/case fields, propose discrepancy ticket, segregate Payroll sign-off | Mismatch yields `human_approval_required` and no payroll write | Python checker / synthetic scenario |
| Sensitive identity and visa records | Protect employee privacy and respect purpose | Ingress allowlist, quarantine flag, least-privilege service identity, no PII in logs | Sensitive flag blocks automatic routing; unexpected fields fail closed | Python validator, checker, security design |
| Approval gaps for regulated action | Human remains accountable for material decisions | Maker/checker pattern and explicit approval states; re-check before any actual write | No code path performs immigration, identity or payroll mutation | Python pipeline and architecture |
| Opaque decisions / difficult audits | Make every automated recommendation traceable | Structured minimized audit, reason code, policy version, UTC time; immutable store in production | Proposed action, disposition and policy version recorded without raw PII | Python audit record, SQL reference model |
| Manual SLA reporting | Prioritize service improvements using measurable data | SQL model for throughput, cycle time, backlog, escalation, duplicates and rework | Definitions and sample queries available; benefits only claimed after pilot | `sql/mobility_ops_metrics.sql` |
| Fragile integration across applications | Use reliable event-driven integration | Signed webhook, validation, REST/OAuth2, retries, DLQ, idempotency and reconciliation | Negative paths escalate; integration tests required before production | `integration/n8n_blueprint.md`, TypeScript adapter example |

### Example business requirement in implementation language

**User story:** As a Global Mobility Operations Lead, I need an incoming payroll mismatch to create a traceable discrepancy proposal for Payroll review, without updating payroll, so that processing speed improves without bypassing controls.

**Functional acceptance criteria**
1. Given a valid synthetic `payroll_mismatch` event, the system creates a recommendation with a reason code.
2. The checker sets `human_approval_required`.
3. No connector writes to a payroll system; the reference implementation is read-only.
4. A repeated `tenant_id:event_id` is marked duplicate.
5. Invalid or unapproved fields are rejected without echoing sensitive values.
6. Audit data is restricted to non-sensitive references, status and policy version.

**Non-functional requirements:** tenant isolation, RBAC/ABAC, authentication, data minimization, encryption, retention, audit immutability, observability, SLOs, graceful degradation, contract versioning, rollback and regional compliance assessment before deployment.

## 2. Low-code and integration tooling

The intended integration can be expressed using the following tools; **only the files explicitly identified as implemented are built in this project**:

| Tool | Role in proposed architecture | Current evidence/status |
| --- | --- | --- |
| **n8n** | Webhook ingest -> schema gate -> minimal HRIS lookup -> invoke Python checker -> safe routing or reviewer queue | Workflow blueprint only: `integration/n8n_blueprint.md` |
| **Make** | Alternative scenario orchestration with routers, HTTP modules, error handlers and approval integrations | Option analyzed, not configured here |
| **Zapier** | Alternative lightweight event notifications and low-risk case updates; never direct regulated decisions | Option analyzed, not configured here |
| **Retool** | Proposed internal dashboard/reviewer UI for case exception queue, approvals and SLA monitoring | UI/permissions concept, not deployed here |
| **Python 3** | Implemented deterministic maker/checker, validation, synthetic fixture runner, audit events and tests | `src/mobility_pipeline.py` and `tests/` |
| **TypeScript** | Typed webhook-boundary example for safe normalization and orchestration dispatch | Source example: `integration/typescript_webhook_adapter.ts`; no live server |
| **REST APIs, JSON, webhooks, OAuth2** | Integration patterns and data contracts | Contract/design examples only |
| **SQL** | Operational KPI / exception analytics | Reference queries, not connected to production data |

See `integration/platform_choices_and_approval_design.md` for platform choices and the proposed human-approval surface.

## 3. Handling sensitive personal data and compliance

- **Data classification:** employee names, passport/Emirates ID values, visas, compensation and personal contacts are never included in synthetic fixtures, LLM prompts, audit logs or analytics.
- **Access control:** proposed RBAC/ABAC separates Mobility, HRIS, Legal, Payroll, Security and privileged executor roles; use scoped OAuth2/service credentials and tenant filtering.
- **Auditability:** use reason codes, request IDs, policy versions, actor references, UTC timestamps, reviewer decision references and append-only retention-managed logs. A demo audit record is *not* proof of an immutable production log.
- **Compliance by jurisdiction:** assess GDPR and applicable national employment, privacy and immigration requirements with Legal/Privacy; record lawful basis and data-processing purposes; assess DPIA and cross-border transfer requirements when needed.
- **Human-in-the-loop:** payroll, identity, immigration status and employment actions require qualified review, documented authorization and a server-side execution gate.
- **Operational resilience:** idempotent retries, dead-letter routing, service-account secrets vault, monitored connector failures, audit access reviews, threat modelling and kill switch are production dependencies.

## 4. Self-directed technical development and learning

This self-directed prototype combines operational discovery, requirements engineering, Python coding, typed TypeScript integration design, SQL, REST/JSON contracts, n8n workflow design, AI-agent maker/checker evaluation and governance-by-design.

**Learning / engineering workflow:** define a testable operational problem -> break work into intake, routing, approvals and audits -> build minimal deterministic Python workflow -> create synthetic positive/negative fixtures -> write automated regression tests -> document low-code integration alternatives -> harden controls -> define measurable pilot success criteria.

These are **portfolio activities**, not a substitute for substantiating an application question about work implemented in a previous/current employed role.

## 5. Truthful use in interviews and applications

**Supported by this repository:** independent translation of a representative problem into functional/non-functional requirements; personally authored Python automation prototype; TypeScript source example; sensitive-data safeguards; audit architecture; n8n integration design.

**Not supported by this repository alone:** personally configuring Zapier/Make/Retool in a professional role; integrating real HRIS/payroll systems; shipping a production mobility agent; achieving measured time/cost savings; obtaining production privacy/regulatory sign-off.
