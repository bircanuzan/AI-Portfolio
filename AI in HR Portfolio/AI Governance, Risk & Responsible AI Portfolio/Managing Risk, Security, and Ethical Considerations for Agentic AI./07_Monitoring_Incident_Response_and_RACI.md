# 07 — Operating Controls, Incidents and Ownership

## Event log schema (designed; no production data)

| Field | Meaning |
|---|---|
| event_time | ISO 8601 timestamp |
| trace_id | Correlation across agent, tool and approval |
| agent_id/version | Unique deployed version |
| user_context_id | Authorized pseudonymous user context |
| business_purpose | Why the task was requested |
| tool/action | Requested API and operation |
| data_classification | Public/internal/confidential/restricted |
| policy_decision | ALLOW / APPROVAL REQUIRED / DENY |
| approval_id | External human approval reference, if any |
| outcome | success/denied/error/cancelled |
| incident_id | Link to incident record where relevant |

Do **not** log actual CVs, personal data, passwords or access tokens in plaintext.

## Example operational monitoring plan (not implemented)

| Signal | Possible trigger | Response |
|---|---|---|
| Denied external export attempts | Any unauthorized candidate data export | Block and investigate |
| Unapproved write calls | Any attempted ATS/rejection write without approval | Stop action and alert |
| Credential misuse | New unusual system/destination | Pause connector, rotate credential |
| Repeated prompt injection | Recurring malicious payloads | Review affected sources, retest |
| Cost or recursion anomaly | Beyond configured approved budget | Terminate run and triage |
| Critical incident | Confirmed/suspected severe harm | Activate kill switch and incident process |
| Model/tool change | Every material modification | Regression and risk reapproval |

Thresholds require local validation.

## Incident playbook

1. **Detect:** monitoring, user complaint or test identifies event.
2. **Contain:** suspend connector/action permissions; stop relevant agent.
3. **Preserve:** store lawful minimal trace/evidence with access control.
4. **Assess:** security, privacy, legal and business owners evaluate harm and notification duties.
5. **Remediate:** fix code/policy/identity/data boundary, rotate credentials if needed.
6. **Retest:** execute same and adjacent attack tests; document real results.
7. **Approve restore:** independent human authority signs off; agent cannot self-restore.
8. **Learn:** update risk register and controls.

## RACI (illustrative)

| Work | Executive | AI governance | Security | Legal/Privacy | HR process | Engineer |
|---|---|---|---|---|---|---|
| Risk appetite | A | R | C | C | C | I |
| Agent charter/authority | I | A | C | C | R | R |
| Tool permission enforcement | I | C | A | C | C | R |
| Personal data review | I | C | C | A/R | C | C |
| Fairness and human workflow | I | C | C | C | A/R | R |
| Adversarial testing | I | A | R | C | C | R |
| Go/hold decision | A | R | C | C | R | C |
| Incident response | I | C | A | C | C | R |

**R/A/C/I:** Responsible, Accountable, Consulted, Informed.

## 30 / 60 / 90-day roadmap

**Days 1–30:** agent inventory, permission boundaries, data map, legal review, system diagram and preliminary threat model.  
**Days 31–60:** implement policy gates in a restricted environment, write tests, validate human approval and kill switch design.  
**Days 61–90:** conduct properly authorized evaluations, fix issues, release only after sign-off, create ongoing monitoring and periodic reassessment.

Any sample KPI or suggested control in this file is design-only until evidenced by a live evaluation.