# End-to-end test scenarios — AI and automation quality gates

## Acceptance matrix
| ID | Scenario | Required result | Evidence |
|---|---|---|---|
| UAT-01 | Valid receipt + eligible item + matching promo | Approve eligible refund request exactly once | Receipt, decision log |
| UAT-02 | Same return submitted twice | Reject second request by idempotency key | Duplicate event |
| UAT-03 | Discount applied at time of original purchase | Use immutable original transaction amount, not today's list price | Source sale + promo version |
| UAT-04 | No receipt / customer-specific exception | Route to authorized store supervisor | Approval record |
| UAT-05 | Return falls outside published policy | Hold case; human exception review | Policy rule version |
| UAT-06 | WMS update fails | Keep reconciliation exception open; retry with backoff | Dead-letter/retry |
| UAT-07 | Finance posting fails | Flag refund/accounting difference for finance | Exception queue |
| UAT-08 | CRM notification cannot send | Retry/queue communication; no duplicate refund | Messaging status |
| UAT-09 | Prompt injection in customer message | Do not allow customer text to override policy or system rules | Safety test |
| UAT-10 | Permissioned override | Require named authority, reason and timestamp | Approval audit |

## Nonfunctional conditions
Role-based access; clear service ownership; transaction correlation IDs; no secrets in logs; resilience during POS offline recovery; privacy/compliance review; approved SLA targets; rollback/compensation; documented support handover.

## AI decision boundaries
Recommend only grounded **case summary** or **exception triage** with source references and human review. Refund decisions and accounting changes are deterministic business rules or approved managers, not unconstrained LLM decisions.

## Data collection plan
Baseline sample across stores, categories and different trading days. Quality assurance includes control comparison and rework sampling. Report true confidence intervals where sample size permits.
