# Operating model, quarterly OKRs, process map and SOPs (synthetic)

## Team context / discovery
Sales receives creator-marketing campaign briefs; operations checks completeness; creator team matches profiles; brand lead approves shortlist; execution monitors delivery; finance/data team validates conversion attribution. This is a **generic synthetic scenario**, not MoonTech's proprietary operations.

Ask owners: Which campaign attributes are compulsory? Current CRM data quality? How are approvals logged? Who owns creator eligibility? Average time in each stage? Missing-brief and rework rates? Which attribution data can be independently verified? Are consumer and creator consent standards documented?

## Illustrative quarterly OKR tree (targets are hypotheses, not outcomes)
Objective O1: Improve cycle speed without reducing quality.
- KR1: 95% of new briefs pass validated-intake checks by quarter end.
- KR2: Reduce median handoff turnaround from **unknown actual baseline** to **agreed target after baseline study**.
- KR3: 100% of campaign launches have a recorded approver.

Objective O2: Build measurable, accountable workflows.
- KR1: 100% of critical handoffs have documented owner and SOP.
- KR2: 90% of eligible pilot cases follow the approved automation flow.
- KR3: 0 unapproved external data transfers in pilot.

Objective O3: Establish credible performance reporting.
- KR1: Reconcile 100% of test attribution events to source IDs.
- KR2: Publish weekly sample dashboard with run metadata and anomaly register.

**Cadence:** quarterly OKR planning; weekly owner check-ins; monthly process retrospective and prioritized backlog. RAG status derived from actual evidence, not subjective color coding alone.

## Process
AS-IS (hypothesis): email brief → spreadsheets → manual eligibility checks → messaging approvals → fragmented reports.
TO-BE (proposed): structured campaign intake → validation gate → draft tasks by owner → human creator/brand approval → approved-system update → event reconciliation → KPI dashboard.

## RACI
| Step | Accountable | Responsible | Consulted |
|---|---|---|---|
| Brief acceptance | Operations lead | Account coordinator | Sales |
| Creator matching | Creator lead | Creator manager | Brand/privacy |
| Launch authorization | Brand owner | Campaign manager | Legal/privacy |
| Data reconciliation | Analytics lead | Analyst | Finance |
| Automation change | Tool/product owner | Integration specialist | Security |

## SOP: campaign intake
1. Receive structured intake with campaign ID, client alias, dates, budget *band*, objectives and deliverables.
2. Validate required fields; reject incomplete requests with human-readable reason.
3. Route accepted intake to the designated internal team as a **draft**, not a real external action.
4. Require named brand owner approval before outreach or launch.
5. Assign trace ID and record any failed validation without sensitive data.
6. Close with evidence that campaign and attribution data were reconciled.

## SaaS/automation architecture (to be implemented)
CRM → authorized webhook → n8n/Make/Zapier trigger → validation and allowlisted AI classification → draft task → human approval → authorized CRM update → BI event stream. Use OAuth scopes, secure credentials, retries, idempotency keys, structured incident alerts, data minimization and privacy review before live use. Define tool owners and rollback before deployment.
