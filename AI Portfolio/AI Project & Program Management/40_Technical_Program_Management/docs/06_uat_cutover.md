# 06 — UAT, Launch Readiness and Hypercare

## Test traceability
| Test | Synthetic scenario | Acceptance proof | Owner |
| --- | --- | --- | --- |
| T01 | Valid risk event | Schema accept + audit correlation ID | Client Tech Lead |
| T02 | Required field missing | Rejection reason visible with no sensitive detail | Engineering QA |
| T03 | Unauthorized credential | Access denied, no data leakage | Security |
| T04 | Identical event ID replayed | One business action, duplicate recorded | Beacon Engineering |
| T05 | Timeout and out-of-order delivery | Event eventually reconciled or alarmed | SRE |
| T06 | High-risk event | Human review queue and auditable approval | Client Risk Operations |
| T07 | Rate limit/transient errors | Safe retries, no silent loss | Engineering QA |
| T08 | Audit trail request | Access-controlled and redacted event history | Compliance |

## Minimum go/no-go gate
Approved scope + interface contract; signed UAT; no open critical/P1 defects; security approval; monitoring and rollback evidence; owner contacts; documented sponsor decision.

**Illustrative 29 October decision: NO-GO for both clients.** Atlas mapping is unapproved; Beacon has an unresolved P1. The planned dates are targets, not approvals.

## Sample cutover timeline
T-5d: dependency, test and owner review. T-2d: freeze scoped changes. T-1d: rollback and incident rehearsal. T0: controlled rollout only after signed approval. T+1d: monitor exceptions and reconciliation. T+5d: formal hypercare exit and runbook transfer.

No real production cutover has been executed in this portfolio case.
