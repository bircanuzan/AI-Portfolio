# Oracle HCM security, testing and operational handover

## Risk-based UAT (planned)
| Case | Risk | Expected behaviour |
|---|---|---|
| ORC-01 | Unapproved hire | Hold, record issue and human owner |
| ORC-02 | Duplicate event/version | Rejected or quarantined; no duplicate publish |
| ORC-03 | Invalid effective date | Reject with explicit data quality reason |
| ORC-04 | Unsupported action | Reject, preserve raw input separately in secure staging only |
| ORC-05 | Unauthorized HCM resource | Access denied and audited |
| ORC-06 | Integration endpoint unavailable | Backoff, bounded retry, alert and dead-letter handling |
| ORC-07 | Bulk extract mismatch | Hold release, reconcile source/target control totals |
| ORC-08 | Retroactive worker transfer | Explicit effective-date and superseded-version handling |

## Security model
System-to-system identity and least-privilege scope; separate HRIS steward, HR approver, Payroll approver, IT operator, integration administrator and audit reviewer roles. No medical, bank or unnecessary personal attributes in events or logs. Avoid broad "integration specialist" privileges where a more constrained role is supported.

## Cutover and hypercare plan
Dry-run payload validation -> signed mapping -> security review -> documented UAT evidence -> migration/snapshot reconciliation -> named go/no-go -> observability check -> 2-4 week controlled hypercare -> formal runbook ownership and escalation.

## Evidence to capture if later using a real licensed tenant
Object/field metadata, redacted request/response, execution ID, role/permission signoff, audit log, retry trace, batch reconciliation, defect register and dated business acceptance. Never publish credentials or employee data.

**Current status:** UAT specifications authored; no Oracle execution or vendor configuration performed.
