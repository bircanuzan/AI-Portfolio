# Discovery and Requirements — Employee Knowledge Assistant (Sample)
**Portfolio simulation — not a client implementation.**
## Business problem
A hypothetical 250-person services company receives repetitive employee questions about leave, travel and IT requests. HR wants a knowledge assistant that answers *only* from approved policies and routes unresolved queries to a human.
## Stakeholders and roles
- HR policy owner: approves policy content and wording
- IT/security lead: approves data access, retention and security
- AI delivery team: chooses model, builds integration, fixes technical defects
- Project documentation lead: captures requirements, decisions and user feedback
## User stories and acceptance conditions
| ID | Need | Acceptance criterion | Owner |
|---|---|---|---|
| R01 | Ask about annual leave | Answer references current approved leave policy and effective date | HR |
| R02 | Find travel reimbursement rules | Assistant links to approved expense policy; no invented amounts | Finance |
| R03 | Ask an unsupported question | Assistant states uncertainty and provides support route | HR |
| R04 | Request personal employee data | No private records disclosed without authorized access | IT |
| R05 | Contact human support | Escalation route displayed on unanswered or sensitive queries | HR |
## Boundaries
In scope: published policy FAQs, citations, user instructions, feedback log. Out of scope: payroll advice, employee-specific entitlements, HRIS writes, legal opinions and autonomous decisions.
## Dependencies
Approved policy version list; written data-use approval; escalation contacts; accessibility review.
## Open decisions
Who updates policy versions? What is the escalation SLA? Which channels are allowed? Which language variants are needed?
## Sign-off checklist
Policy owner approves source list and representative answers; security lead approves access; delivery team verifies technical behavior; business owner accepts handover.
