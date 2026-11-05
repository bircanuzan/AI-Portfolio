# Project 15 | AI / DevOps Technical Trainer - portfolio case study

**Scope and integrity:** Original technical-education sample with executable local Python demonstration. No claim of operating Linux fleets, Kubernetes clusters, live CI/CD, cloud infrastructure or production DevOps. No actual LLM API integration or agent execution; those are learning topics and safety designs.

## Teaching objective
Help engineers safely use AI coding assistants and agents to diagnose CI failures and *propose* infrastructure changes, while preserving evidence, credential safety, review and human approval.

| Section | Learning outcome | Evidence |
| --- | --- | --- |
| Diagnose CI failures | Distinguish observations from hypotheses; cite logs; spot prompt injection | Log triage worksheet |
| AI workflow safety | Redact secrets, constrain prompts, verify proposed fixes with tests | Bounded prompt and review |
| Delivery controls | Explain Docker/Kubernetes and CI/CD, IaC plan/review/approve/rollback | Risk and approval checklist |

Designed for 8 micro-lessons of about six minutes, a 60-minute safe-lab demonstration and an assessment. The lab team provisions environments; technical SME reviews validity; editor approves clarity; production owns actual video editing and publishing.

## Repository files
- src/triage.py: deterministic, local log failure classifier (NOT an AI agent).
- tests/test_triage.py: unit tests for failures and adversarial instructions.
- ai_devops_course_lab.md: complete lab build specification, sample presentation script, AI prompt guardrails, CI/CD/IaC review, Kubernetes demo and scoring.
- .github/workflows/ci.yml: a sample CI workflow, not a deployment.
- deploy/k8s_example.yaml: inert illustrative manifest; fake image, never applied.
Run python src/triage.py; run python -m unittest discover -s tests. No dependencies, network access or credentials required.

## Transfer to production
Out of scope. Working DevOps engineers must independently approve access, architecture, security, infrastructure rollout and observability. This course portfolio shows teaching design and educational code only.
