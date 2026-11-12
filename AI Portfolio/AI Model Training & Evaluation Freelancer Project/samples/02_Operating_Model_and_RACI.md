# Target Operating Model — Customer Intake to Resolution

**As-is hypothesis:** request → intake triage → service queue → risk review → specialist resolution → response; duplicate entry and unclear escalation can occur.

**To-be design:** structured request capture → automated classification suggestion → intake human validates priority → service specialist resolves routine cases → Risk human decides exceptions → independent QA samples outputs → case closure with audit log.

| Activity/Decision | Intake Lead | Service Lead | Risk Owner | IT Owner | AI Assistant |
| --- | --- | --- | --- | --- | --- |
| Intake classification | A | C | I | C | R (suggestion only) |
| Routine case resolution | C | A/R | I | I | C |
| Exception authorization | C | C | A/R | I | I |
| Permissions configuration | I | C | C | A/R | I |
| Quality sample review | C | A/R | C | I | I |

A = Accountable (one for each row); R = Responsible; C = Consulted; I = Informed. AI 'R' is *draft execution only*, not legal or management accountability.

**Exception path:** confidence below threshold or protected data detected → queue human review → Risk owner makes explicit decision → logged disposition. No agent has final approval authority.

**KPIs:** response time, repeat data entry, exception rework, human override rate, audit completeness. Baselines to be gathered before reporting achieved benefits.

