# Low-code platform choices and secure approval workflows

> **Status: architecture / tool-selection evaluation only.** The project does not include live Zapier, Make, n8n or Retool instances, production APIs or authenticated service accounts. The implemented Python reference is entirely local and synthetic. A TypeScript normalization example sits in `typescript_webhook_adapter.ts`.

## Platform selection: n8n, Make, Zapier, Retool

| Tool | Best-fit role in mobility operations | Example proposed workflow | Risk / mitigation | Delivery evidence |
| --- | --- | --- | --- | --- |
| **n8n** | Multi-step, controlled integration orchestration; HTTP/webhooks, branching, retries | Signed event trigger -> allowlist schema -> call Python maker/checker -> switch on disposition -> create *draft* ticket or approval request -> record minimized audit | Require enterprise hosting/privacy assessment, secret management, scoped credentials, retries + DLQ, separation of approval and execution | `n8n_blueprint.md` is design only |
| **Make** | Alternative visual scenario builder for event mapping and operational notifications | Trigger case created -> JSON validation -> HRIS metadata lookup -> approval routing via controlled API -> exception handler | Prevent personal documents in scenario logs, avoid unscoped service accounts, restrict action modules | Comparative proposal, not configured |
| **Zapier** | Lightweight non-sensitive triggers, reminders and stakeholder alerts | New sanitized status event -> draft reminder -> update low-risk service queue | Do not place identity/payroll data in unapproved SaaS connectors; forbid direct regulated changes | Comparative proposal, not configured |
| **Retool** | Internal human-review workspace and operational visibility | Reviewer sees minimized case summary, underlying evidence via authorized application, approves/rejects with reason -> audited approval reference | Enforce application and backend RBAC, tenant filters, MFA/SSO, anti-CSRF, immutable sign-off, maker/checker separation | UX/permissions design only |

## Proposed canonical n8n workflow

1. **Trigger:** verified webhook with `tenant_id`, `event_id`, `case_id` and category, with signed transport and replay protection at gateway.
2. **Schema gate:** reject all unexpected properties, size-limit inputs; no raw identity documents.
3. **Idempotency:** transactional `tenant_id:event_id` lock and versioned source record before any external side effect.
4. **Fetch scoped metadata:** read the minimum case/HRIS facts via scoped REST/OAuth2, not full employee records.
5. **Propose + check:** call Python checker API; treat it as recommendation only.
6. **Control route:** `internal_routing_only` -> low-risk queue/draft; `draft_only` -> approved FAQ draft; `human_approval_required` -> reviewer queue; unknown/failure -> manual escalation.
7. **Approval UI:** proposed Retool queue displays jurisdiction, change type, minimal evidence, policy ref, reviewer role, rationale and expiring approval request.
8. **Server-side authorization:** a separate executor validates qualified reviewer signature and current role, correct tenant, latest version, allowed action and event idempotency. The agent cannot approve itself.
9. **Audit & alerting:** append sanitized structured result; alert on denied actions, retries, stale approvals, audit or policy drift.
10. **Fallback:** route timeouts, bad signatures, no policy citation or conflicting data to protected human queue; prohibit automatic payroll/immigration changes.

## Retool review workspace — permissions design

| User role | Can view | Can approve | Must not do |
| --- | --- | --- | --- |
| Mobility Operations | Assigned case summary; approved policy metadata | Routine, non-regulated service drafts within scope | Modify payroll; approve immigration outcome |
| HRIS Analyst | Authorized data-quality discrepancy | HRIS correction proposal when policy permits | Change identity without verification |
| Payroll Reviewer | Payroll-related mismatch with authorized underlying details | Payroll handoff approval according to segregation of duties | Self-approve own maker proposal |
| Legal / Immigration | Scoped immigration case and source evidence | Required legal or immigration review | Delegate regulated decision to agent |
| Security / Privacy | Incident metadata, access logs, control alerts | Privacy/security release gates | Broaden case access without justification |
| Automation Service Account | Minimized metadata only | **Never** a human approval | Read passports or run unrestricted writes |

## Webhook and scripting patterns

- **Python:** `src/mobility_pipeline.py` contains local rule-based intake, independent checking, idempotency and minimized audit output.
- **TypeScript:** `integration/typescript_webhook_adapter.ts` contains a pure typed event normalizer and privacy dispatch gate. It is not an HTTP service; caller must supply authentication, authorization and signature verification before invoking it.
- **REST + JSON:** use versioned schemas, explicit content types, request/trace IDs, structured error codes and contract tests.
- **API security:** OAuth2 scoped tokens, signed webhooks, private network routes, centralized secret vault, token rotation and tenant-aware authorization; not implemented in this demo.
- **Operational controls:** 429/5xx retry with exponential backoff, dead-letter queue, independent duplicate reconciliation, circuit breaker and manual fallback; production patterns to build and test.

## Technical learning and validation backlog

1. Compile and run TypeScript normalization and rejection unit tests using a pinned TS toolchain.
2. Import a synthetic workflow into a controlled n8n sandbox (do not send live HR records).
3. Compare Make and Zapier scenario portability and logging behavior using only dummy data.
4. Prototype Retool approval screens connected to synthetic case records, with backend-enforced roles.
5. Test API timeout, invalid webhook signature, duplicate `event_id`, cross-tenant access, excessive permissions and document-based prompt injection.
6. Produce evidence of test execution, versioned CI results and approvals before describing any component as deployed.

## Project status and evidence boundary

The folder documents **technical selection and design**, not professional or production usage of these low-code products. Any personal job-application claim about previously *using or implementing* a given platform needs separately verified firsthand experience; comparing it here does not establish that experience.
