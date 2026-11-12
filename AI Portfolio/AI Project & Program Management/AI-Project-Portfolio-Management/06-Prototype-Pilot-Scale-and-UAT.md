# 06 | Stage-Gate Delivery: Discovery → Prototype → Pilot → Production Scale
Synthetic governance playbook with clear technical and business handoffs.

| Stage | Evidence required | Decision maker | Exit criteria |
|---|---|---|---|
| Intake | Named problem, sponsor, baseline, qualified AI Champion | Portfolio triage | Prioritization/feasibility + gating |
| Discovery | As-is / to-be process, user journey, BRD, preliminary ROI | Business owner / Head of AI | Requirements accepted |
| Prototype | Synthetic/redacted data; architecture and sandbox; baseline test set | Architecture + Sponsor | Demonstrable utility; no critical control breaches |
| Pilot | DARB/InfoSec/Risk approvals; UAT plan; user onboarding; support path | Business UAT lead + control forums | Agreed accuracy/adoption/incident threshold |
| Scale | Release/rollback plan, performance & security tests, cost, monitoring, handover | Production change authority | All mandatory gate signoffs |
| Benefits | KPI reporting, change adoption, incident review and improvement backlog | Business benefit owner | Evidence of sustained business value |

## Example integrated delivery plan (AI-001)
- Week 1: discovery workshop; operational baseline; policy source mapping.
- Week 2: complete BRD, architecture option and data classification.
- Weeks 3–4: sandbox retrieval prototype with redacted synthetic materials.
- Weeks 5–6: evaluation + security review + supervised staff UAT (if approvals obtained).
- Week 7: sponsor/architecture/risk decision on constrained pilot; **production is not assumed**.

## UAT traceability matrix
| Test | Requirement | Scenario | Expected result | Owner | Evidence |
|---|---|---|---|---|---|
| UAT-01 | FR-02/03 | Current approved policy | Cited, versioned answer | Operations lead | Output + source IDs |
| UAT-02 | FR-04 | Missing data | Abstain; highlight missing item | SME | Screen capture |
| UAT-03 | FR-01 | Unauthorized access | Access denied, logged | InfoSec | Security test log |
| UAT-04 | FR-04 | Conflicting guidance | Escalate, do not speculate | Compliance | Decision record |
| UAT-05 | NFR-Sec | Prompt injection in document | Model ignores external tool instructions | AI QA/InfoSec | Adversarial case |
| UAT-06 | FR-05/06 | Reviewer rejects draft | No workflow bypass; correction logged | UAT lead | Audit evidence |
All above are **planned** cases, not executed or passed tests.

## Production readiness
- **Data:** ownership, masking, lineage, retention, approvals.
- **Platform:** identity, secrets, APIs, capacity, observability, uptime/SLO and cost.
- **Security:** pentest/threat-model outcomes, prompt injection, fallback and incident plan.
- **Quality:** performance, consistency, model evaluation and regression benchmarks.
- **Business:** UAT sign-off, role training, SOP update, support owner, benefits baseline.
- **Release:** change approval, deployment/rollback plan, version control, post-release monitoring.

## Operational handover template
Service owner; technical owner; approved business scope; supported models/data; on-call route; failure modes; manual fallback; escalation contacts; data retention; monitoring/alerts; KPI reviews; post-implementation review due date.

## Continuous improvement
Lessons-learned retrospective after each gate, reusable acceptance tests and standardized evidence packs, updated from real deployment observations only after authorized validation.
