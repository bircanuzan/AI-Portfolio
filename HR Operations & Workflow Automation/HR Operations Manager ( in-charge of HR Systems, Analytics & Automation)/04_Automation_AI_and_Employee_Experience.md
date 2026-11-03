# Workflow automation, responsible AI & employee experience

## Workflow A — employee pay-change request (design only)
1. HRMS event captured in approved request form; validate employment identity, entity and effective date.
2. Manager submits supporting details; HR verifies grade/band and contract implications.
3. Finance reviewer independently approves monetary impact (segregation of duties).
4. Integration queues approved record; Payroll reconciles effective-date changes against cutoff.
5. Publish only minimised status to employee portal; log every approval and exception.
6. If approval missing or data anomalous, **stop**; alert named human owner; no system-generated payment.

**Proposed tools:** Power Automate approval flow, SharePoint restricted list or enterprise ticketing, HRMS workflow API (subject to vendor capability), Teams notifications, Power BI for aggregate reporting. These tools are a deployment blueprint, not a live integration.

## Workflow B — HR helpdesk and self-service
- Employee submits request for leave, documentation, policy, benefits, pay query or offboarding.
- A rules-based triage layer uses structured categories and context-free priority logic; no sensitive inputs in prompts.
- A proposed LLM assistant may summarise *approved general policy articles* with citations, flag uncertainty and hand off to HR.
- Salary, grievance, medical, identity or bank information must never be sent to a generic external model without approved controls, legal basis and contractual safeguards.
- HR resolves and records outcome; employee sees progress and may appeal/escalate. AI does not interpret contract rights or make employment decisions.

## Failure modes & safeguards
| Risk | Design response |
|---|---|
| Hallucinated UAE payroll law | Approved reference knowledge base, source date, expert review |
| Wrong-employee data exposure | RBAC, least-privilege, masked identifiers, query isolation and logging |
| Unauthorised salary changes | Maker-checker, immutability of approval history, step-up verification |
| Duplicate automation retries | Idempotency key and reconciliation queue |
| Late/missed HR request | Time-based SLA reminders and designated substitute owner |
| Model drift or unsafe decisions | Test suite, change approval, human-in-the-loop, disable switch |

## Adoption / service KPI plan
Measure service first-contact resolution, average time to close, employee satisfaction, error rates, manual touches, and exceptions returned for rework. Build an opt-in feedback cycle for staff. No invented improvement percentages are claimed.