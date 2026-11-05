# 02 — Stakeholder, Impact & Role Mapping and RACI

## Step 1: stakeholder segmentation
| Audience | Change impact | Likely concern | Required support |
|---|---|---|---|
| Employees (including mobile/non-desk) | High: new request channel and tracking | Digital access; privacy; language | Clear entry point, accessible alternatives, privacy FAQ |
| Line managers (90, fictional) | High: approvals move into workflow | Backlog, unfamiliar delegated authority | Approval map, manager job aids, escalation |
| HR services (25, fictional) | High: queues, ownership and new reporting | Increased initial workload and service exceptions | Case taxonomy, capacity coverage, clinic and support |
| HRBPs | Medium: employee exceptions and policy escalation | Inconsistent boundaries | Policy and escalation matrix |
| IT service management | Medium: identity/access and incident routing | Integration risk | UAT and incident ownership |
| Senior leadership | Medium: service quality and confidence | Disruption, cost and trust | Executive sponsor dashboard and decisions |
| Data privacy/legal | High on sensitive cases | Personal data exposure, unfair decisions | DPIA/contract/data-access approvals as appropriate |

## Step 2: current-state versus future-state
| Process | AS-IS | TO-BE proposed | Behaviour required |
|---|---|---|---|
| Employment letter | Email to HR; request buried in shared inbox | Portal request with case ID; HR checks entitlement and releases | Employee uses portal, HR tracks ownership |
| Routine HR FAQ | Multiple inconsistent email replies | Approved knowledge page + human escalation | Employee checks approved guidance; HR keeps it current |
| Manager approval | Ad-hoc email and unclear delegation | Explicit workflow approval by authorised manager | Manager monitors queue and follows decision rules |
| Sensitive HR concern | May be sent to generic mailbox | Dedicated confidential channel | Employees use protected route; no public self-service ticket |

### Impact scoring rubric (original)
**Severity:** 1 = minor communications only; 2 = new interface; 3 = changed responsibility/approval; 4 = major process and capability change. **Exposure:** number of affected people and locations; **risk:** low/medium/high based on ability to perform safely; consider accessibility and data protection.
See [synthetic impact register](data/synthetic_change_impacts.csv) for fictional example entries.

## RACI
R = executes; A = final accountability; C = consulted; I = informed.

| Activity | Sponsor | HR Ops | HR Change | IT | HRBP | Privacy |
|---|---|---|---|---|---|---|
| Approve new HR case policy | A | R | C | C | C | C |
| Map role impacts | I | C | A/R | C | R | C |
| Send change communications | I | C | A/R | I | C | C |
| Configure user access | I | C | I | A/R | C | C |
| Approve privacy safeguards | I | C | C | R | I | A |
| Sign off business pilot readiness | A | R | R | R | C | C |
| Accept ongoing HR service ownership | I | A/R | C | C | R | C |

### Role mapping safeguards
- Final job profiles, HR policy rights and system roles must be approved by HR and IT.
- No manager may gain permissions by merely being labelled a change champion.
- Employees with accessibility or device barriers require a non-digital alternate route.
- Technology access is not evidence that a user understands a workflow.

## Findings and decisions needed
A sample analysis would prioritise employees without regular desktop access and managers with approval delegation changes for early consultation. **This is a hypothesis; no interviews were conducted.**

**Project evidence:** reproducible impact categorisation and decision authority; not real employee observations.
