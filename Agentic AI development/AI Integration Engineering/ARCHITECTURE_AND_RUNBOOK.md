# Agent to enterprise service — process, API contract and deployment runbook

## AS-IS / TO-BE
Manual desk triage → user asks policy agent → agent escalates when needed → user explicitly confirms ticket → adapter enforces category and idempotency → service desk returns a case ID → signed callback confirms status.

## Future REST contract (not deployed)
POST /v1/cases, JSON {category: policy_question|letter_request, safe_summary: text, confirmed: true}; Idempotency-Key request header; Authorization Bearer from trusted service identity. 201 {case_id, status}, 400 validation, 401 auth, 409 idempotency conflict, 429 throttling. Webhook X-Signature sha256=<HMAC SHA256 over raw body> + timestamp/replay window. Secrets in managed secret store.

## Threats and controls
- Prompt injection/agent privilege escalation: narrow tool allowlist, restricted service principal, human confirmation.
- Duplicate action on retry: durable idempotency key and payload-hash comparison.
- Forged callback: constant-time HMAC verification, timestamp/replay check (latter pending).
- Employee data leakage: no personal data in telemetry; privacy and residency review before real use.
- Downtime: bounded exponential backoff, dead-letter queue, manual fallback and reconciliation (planned).

## Operational acceptance
No write without confirmation; invalid category rejected; same key+payload same result; altered replay fails; forged signature fails; owner can reconcile uncertain submissions.

## Production checklist — ALL PENDING
[ ] Approved sandbox and test identities
[ ] OAuth2 service auth + scoped RBAC
[ ] API gateway/rate limiting
[ ] Persistent state/idempotency
[ ] Timestamped signed callbacks and replay protection
[ ] Integration and security tests
[ ] UAT sign-off, rollback, runbook owner
[ ] Observability, alerts, secure retention, data residency approval

Measure deployment success rate, time to resolution, API 4xx/5xx, retries, case duplication, escalations and P95 latency after real deployment. No measured claims yet.
