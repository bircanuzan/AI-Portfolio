# Architecture, data controls and threat model

## Boundaries and responsibilities
- **Case/event source:** HRIS, employee portal, case-management queue, or mobility team uploads; source credentials never pass into an LLM prompt.
- **Ingress:** API gateway/webhook validates source signature, request size, schema, explicit tenant context, and `event_id` idempotency.
- **Data guard:** purpose limitation and strict allowlist for fields before any agent; redact and tokenize personal data, never log passport/identity numbers, compensation, visa documents, phone or email addresses.
- **Router/maker:** determines queue and creates a **proposal**, not an external mutation.
- **Independent checker:** verifies risk classification, jurisdiction, evidence, permission scope and action allowlist; fails closed on unknown inputs.
- **Human reviewer:** Mobility/Legal/HR/Payroll actor within a segregated authority matrix explicitly approves regulated/financial actions.
- **Execution:** separate service identity with narrowly scoped write permissions; execution only after policy gate + recorded human approval.
- **Observability:** encrypted per-tenant metrics and immutable audit event references, scrubbed payloads, retention schedule; SIEM alerts for denied actions and elevated error rates.

## Target interface contracts (illustrative, not integrated)

```json
{
  "event_id": "evt-demo-0001",
  "tenant_id": "synthetic-tenant",
  "case_id": "MOB-101",
  "category": "payroll_mismatch",
  "jurisdiction": "AE",
  "source": "case_management",
  "effective_date_mismatch": true,
  "contains_sensitive_data": false
}
```

**Never** transmit raw identity documents via an unapproved third-party AI provider. Document review should use approved encrypted storage and a restricted document classifier; only sanitized field-level results may reach the routing agent.

## Maker/checker design
1. Validate event and source permission.
2. Maker proposes a limited action (`route_to_team`, `request_documents`, `create_discrepancy_ticket`, `draft_policy_response`).
3. Checker re-evaluates from the original permitted facts and an independently defined control table; ignore maker's claimed confidence as proof.
4. Unknown/ambiguous case types, missing jurisdiction, unsupported policy evidence or failed control = escalate without side effect.
5. Human approval is mandatory for immigration outcome, employment status, payroll mutation, financial transfers and identity changes.
6. All writes require a second, server-side policy check; an LLM response cannot authorize its own execution.

## Privacy and security design
- GDPR and local employment/privacy obligations assessed by counsel **per jurisdiction**; do not conflate EMEA countries with one legal rule.
- RBAC and tenant isolation on every query. ABAC on country, region, case sensitivity, service account and need-to-know purpose.
- Encrypt in transit and at rest; keys through a managed vault; secrets never committed to GitHub.
- Access is removed on role changes; privileged changes use two-person approval and break-glass trace.
- Retention policy, DSAR handling, deletion requests and incident response established before live use.
- Explicit consent/legal basis assessment where required; DPIA when processing creates elevated privacy risk.
- Safeguards against prompt injection from uploaded documents and knowledge articles: treat external content as data; never allow content to rewrite routing or security rules.

## Retry, fallback, observability
- 429 and transient 5xx: exponential backoff, capped attempts, jitter; dead-letter queue thereafter.
- Side-effect endpoints: idempotency key per event/action, version guard, reconciliation to avoid duplicate payroll/case writes.
- Irrecoverable API errors, stale rules, low-confidence results and missing citations: hold for human review.
- Trace record: `trace_id`, `event_id`, `case_id`, maker decision, checker result, policy version, disposition, reviewer reference, model/ruleset version, timestamp, durations and outcome code.
- No personal data in trace, dashboards, test fixtures or debugging logs. Structured audit events retained by policy.

## Risk register
| Risk | Control | Owner |
| --- | --- | --- |
| LLM hallucinates immigration guidance | Approved knowledge sources, jurisdiction and citation gate, human advice | Legal/Mobility |
| Wrong payroll effective date | Cross-system comparison, checker, required Payroll approval, dry run | Payroll |
| Privacy leakage to observability | Explicit field allowlist, redaction tests, restricted access | Security |
| Event replays / duplicate cases | Idempotency store, dedupe check, immutable event ID | Engineering |
| Tool permissions too broad | Agent cannot write production; scoped executor identity | IT Security |
| Broken HRIS/payroll connector | Versioned contracts, API mocks, canary and rollback | Integration Lead |
| Unequal routing quality across countries | Stratified evaluation and sampling, localized expert review | Mobility Ops |
| Automation accepted but not used | Champion cohort, feedback, training, service metrics | Change Lead |

## Deployment principles
Use a canary rollout by jurisdiction and task type, feature flag by tenant, kill switch, versioned policy and reproducible test suites. No production deployment before data protection and employment-regulatory sign-off.
