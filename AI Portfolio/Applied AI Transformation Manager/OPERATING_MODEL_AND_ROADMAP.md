# Client Problem, Human–Agent Organisation Chart and 90-day Delivery

## Fictional consulting brief

**Client:** Three synthetic UAE/KSA engineering cohorts spanning 3,600 eligible engineers. **Requirement:** identify valuable software-engineering workflows for AI agent assistance, establish a safe rollout to selected engineers, manage client and Cognition stakeholders and report conservative net capacity and verified business impact.

### Methodology

1. Identify executive sponsor, engineering bottlenecks, code quality, baseline task distributions and data access.
2. Define task taxonomy: documentation, test scaffolding, low-risk refactoring, debugging and exception response.
3. Allocate draft/test work to agents only in authorized sandbox contexts, keeping architecture, code review, merge and production release with humans.
4. Pilot with measured equivalent case mixes and independendent quality/security evaluation.
5. Onboard waves of engineering teams with champions, role-based learning, support, incident/rollback and owner dashboards.
6. Measure effective adoption and net hours including human review, rework, failed attempts, exceptions and oversight.
7. Finance certifies any *actual* value after a real baseline and realized spending change; do not convert hypothetical capacity to layoffs or cash automatically.

## Agent organisation chart and decision rights

Executive sponsor -> Programme director -> Engineering AI CoE (agent owner, platform/security lead, human review coordinator, analytics, learning/change lead and benefits owner). Engineering task agents report operationally to **human engineering team leads**. The customer security and risk function independently challenges decisions.

| Activity | Agent authority | Accountable human | Control |
|---|---|---|---|
| Draft tests or low-risk code proposals | Suggest only, in approved scope | Engineering team lead | Source/branch permissions, unit tests |
| Review candidate code changes | Evidence/suggestions only | Human code reviewer | No autonomous merge |
| Read project context | Only authorized repositories | Data/repository owner | Identity and source ACL |
| Approve production deployment | No authority | Engineering release owner | Signed human approval |
| Choose priorities, budget and staffing | No authority | Executive/Finance/HR | Decision and impact review |
| Handle incidents | Stop and escalate | Security and engineering on-call | Incident severity and rollback |

**Agent KPIs:** validated task success, defect rate, reviewer minutes, rework rate, exception handling, cost per accepted output, incident rate, trace coverage, active engineer adoption, measured quality and net human hours.

## 30 / 60 / 90-day plan

| Window | Delivery | Evidence and gate |
|---|---|---|
| 1–30 days | Executive requirements, task analysis, baseline time study, security/privacy/data/identity scoping, CoE, target metrics | Sponsor authorizes tightly scoped pilot; missing baseline = HOLD |
| 31–60 days | Onboard initial cohorts; engineering workshops/champions; sandbox agent configuration; UAT, security tests, run trace collection | Human review and independent quality gate required |
| 61–90 days | Wider cohorts only after validated outcomes; support playbook; finance and steering QBR; performance dashboards | Approved risk, human go/no-go and finance-verified business case |

## Evaluation and governance

Test accepted quality on held-out real tasks, prompt injection, unauthorized repository access, unsafe modifications, rework, reviewer capacity and cost ceilings. Changes must be reversible, observable and approved before external effects. These are proposed enterprise checks; the code in this project models synthetic capacity and does not execute a live tool-use agent.

## Outcome / results classification

The reproducible synthetic scenario calculator is **implemented and testable**. The operating model is **designed**. Enterprise rollout, live Devin use, integration, deployment and financial savings are **not implemented or measured**.
