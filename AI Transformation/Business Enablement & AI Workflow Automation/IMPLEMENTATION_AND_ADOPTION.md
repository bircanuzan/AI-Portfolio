# Business enablement implementation, change management and value tracking

## Discovery → implementation
1. Interview process owners, inventory workflows and tool permissions.
2. Establish baseline KPIs and consent/privacy constraints.
3. Prioritize fixes using frequency × impact × feasibility, with risk gate.
4. Design low-code automation and validate with representative sample briefs.
5. Configure an approved sandbox, log failures and safely simulate retries.
6. Review security, data access and ownership; obtain go/no-go and support owner sign-off.
7. Run facilitator-led workflow workshops for operations and analytics.
8. Capture adoption, error rate and cycle time at 30, 60 and 90 days.

## Pilot acceptance and failure modes
| Case | Expected behavior |
|---|---|
| Valid approved synthetic brief | Create **draft internal task** with trace |
| Missing campaign ID | Reject with validation explanation |
| Invalid status / no approval | No activation or external execution |
| Duplicate event key | Suppress duplicate task |
| Provider timeout | Keep draft, raise operational escalation, don't silently retry a non-idempotent write |
| Attribution event missing | Flag reconciliation gap, no fabricated conversions |

## Training workshop (45 minutes)
10 min process demo; 10 min create fictional brief; 10 min review validation and ownership; 10 min exception-handling exercise; 5 min short knowledge check. Measure: participant task success, post-training confidence and support tickets; outcomes pending.

## Dashboard logic
Use `data/synthetic_campaigns.csv` to calculate processed count, completion rate, validation pass rate and illustrative handling-time difference. These measures are **not** a operations_group result and cannot be marketed as savings. Use verified source records and baseline measurement before benefit claims.

## Technology map
n8n workflow JSON (draft import); equivalent Zapier/Make trigger/filter/action design; CRM/SaaS REST/OAuth concepts; Python CSV analysis; Excel/Power BI visualization pathway; Jira/Asana task ownership model; AI-powered classification requiring supervision. No actual live subscriptions or external automation are claimed.
