# Agentic AI Delivery — Agile/Scrum Engineering Simulation

**Project type:** Simulated engineering program with fictional stakeholders and backlog. **Status:** Delivery plan and measurement framework; not evidence of leading an employed software engineering team.

## Client requirement / business problem
A cross-functional enterprise team needs to plan and govern an internal AI assistant release, balancing user needs, AI risk, engineering dependencies, security approvals and measurable business outcomes.

## Agile delivery methodology
- **Product goal:** A human-governed assistant that retrieves policies and recommends actions with source evidence.
- **Roles:** Business product owner, Scrum Master/delivery lead, AI engineer, API engineer, QA/evaluation specialist, security reviewer, HR subject-matter expert.
- **Cadence:** Illustrative two-week sprints; planning, daily coordination, backlog refinement, demo/review, retrospective.
- **Definition of Ready:** User story, persona, risk classification, dependencies, testable acceptance criteria, data rules.
- **Definition of Done:** Code reviewed, test and eval gates passed, documentation updated, privacy/security checks complete, product owner accepts.

## Example sprint roadmap
| Sprint | Sprint goal | Key backlog items | Evidence |
|---|---|---|---|
| 0 | Discovery and risk boundary | Persona maps, success metrics, data contract, threat model | Approved scope and backlog |
| 1 | Knowledge retrieval MVP | Ingestion, citation schema, read API | Retrieval test suite |
| 2 | Agent workflow and approvals | Tool registry, HITL state machine, audit logging | Authorization tests |
| 3 | Quality and resilience | Red-team prompts, error states, observability | Defect and eval reports |
| 4 | Release readiness | UAT, security gate, training, rollback | Go/no-go checklist |

## Example user story
**As an HR case reviewer**, I want the assistant to cite the current policy and ask for approval before writing to a case system, **so that** decisions are traceable and remain human-controlled.

**Acceptance criteria:** citation includes version; unauthorized user sees no restricted content; write endpoint rejects calls without approval; failed writes can be safely retried; traces link to the decision.

## KPIs — proposed, not achieved
Sprint goal achievement, cycle time, throughput, escaped defects, build stability, evaluation pass rate, backlog age, change failure rate, human approval compliance and user acceptance. Establish baselines before setting goals.

## Proposed tools
Jira/Azure DevOps/GitHub Projects, GitHub Actions, Python test harnesses, Azure AI Foundry, Teams and simple analytics dashboards. Tools are recommendations, not claims of hands-on delivery in this simulation.

## Deliverables
Prioritized backlog, sprint artifacts, stakeholder RACI, RAID log, dependency map, quality gates, release-readiness template, retrospective actions.
