# 06 — Requirements, user stories, observability and UAT

## Functional and nonfunctional requirements
| ID | Requirement | Acceptance test |
|---|---|---|
| F1 | Authorized role for every event | Unauthorized role blocked |
| F2 | Only minimal synthetic non-PII fields accepted | Email/passport text rejected before logs |
| F3 | No duplicate side-effect request | Replay key marked duplicate |
| F4 | Maker assigns safe routing, never legal judgement | High-risk case sent to specialist |
| F5 | Checker validates route, scope and permissions | Never auto-approves legal/employment change |
| F6 | Human handoff available at any step | Escalation reason traceable |
| F7 | Dependency failure leaves recoverable state | Queued-for-retry status, no lost case |
| F8 | Dashboard supports decision-quality reporting | KPI denominators and period provenance |
| N1 | No unredacted sensitive logs | Only pseudonymous trace metadata |
| N2 | Explicit integration permission boundaries | Human approval for write actions |
| N3 | Case event audit and lineage | Version/correlation ID, status and reason |
| N4 | Scalability with idempotent queue | Under load, retry safe; owner monitors DLQ |

## User stories
"As a Mobility Operations specialist, I need sensitive immigration cases held for qualified review so the platform never presents an unverified eligibility determination."
"As a global employee, I want an accurate case status and clear human contact route without exposing private documents in other systems."
"As a platform engineer, I need stable event contracts, retries and RBAC decisions to debug safe failures without reading passport data."
"As a Senior Manager, I need SLA, exception and safe automation metrics linked to controls and customer experience."

## Negative and edge scenarios
No identity authorization; data-containing free text; prompt injection; duplicate request; jurisdiction-specific case; missing policy/source; dependency outage; permission downgrade; stale approved policy; conflicting effective dates; urgent request near expiry; case handed over across regions; inability to safely log payload. All legal cases fail closed into a specialist queue.

## Operational readiness
Product, Engineering, Security, HRIS, Privacy, Mobility and Payroll owners sign off on role policy, sandbox, API credentials, monitoring, incident runbooks, retries, human queue capacity, data retention and phased rollouts. Demonstration does not satisfy a real production gate.
