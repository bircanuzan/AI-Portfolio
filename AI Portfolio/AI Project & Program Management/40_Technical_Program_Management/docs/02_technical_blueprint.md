# 02 — Vendor-Neutral Integration Blueprint

**Architecture note:** Illustrative design only; not an assertion about Sardine's actual interface capabilities.

## Logical event path
```text
Client source -> data minimization / validation -> authenticated API/event adapter
   -> hypothetical risk signal pipeline -> client rule/alert routing
   -> HUMAN REVIEW / disposition -> audit and monitoring

For outbound events: event queue -> signed webhook delivery
   -> client receiver (idempotency by event_id) -> reconciliation / alerts
```

## Engineering dependency and acceptance checklist
| Control | Practical dependency | Owner |
| --- | --- | --- |
| Schema agreement | Required/optional JSON fields, versions, malformed events | Client Technical Lead + Vendor Engineering |
| Authentication | Least privilege, token rotation, no stored secrets in test artifacts | Security |
| Privacy | Synthetic test data, purpose limitation, retention agreement | Client Compliance |
| Retry semantics | Document timeouts, retry windows and dead-letter queue | Product + Engineering |
| Idempotency | Duplicate event_id produces only one business action | Client Platform Lead |
| Traceability | Correlation IDs, delivery logs, exception dashboard | SRE |
| Quality gate | Negative-path coverage and business signoff | QA + Client Product Owner |
| Human oversight | High-risk case approvals auditable and not auto-finalized | Client Risk Operations |

## Atlas trade-off: missing mapping approval
Continue only mapping-independent engineering; freeze schema-dependent UAT rather than guess timestamp/device normalization. Request the client owner sign the mapping decision or re-baseline under formal change control. **Do not claim sandbox completion without approval.**

## Beacon trade-off: duplicate webhook alerts
An open P1 means no release endorsement. Engineering must verify receiver deduplication, replay, timeout, out-of-order event delivery and reconciliation using synthetic cases. Product owns any change to stated delivery semantics; client technical owner accepts the evidence.

## Constraints
No live banking data, no production authentication, no public claims of regulatory certification, and no vendor-proprietary API detail.
