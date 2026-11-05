# Agentic AI enterprise operating model and Center of Excellence (CoE)

## Federated operating model
- **Executive Steering Committee:** CTO/CIO/business sponsor and Finance accept scope, risks and value method.
- **Agentic AI Center of Excellence:** publishes use-case patterns, prompts, security standards, evaluation framework, developer enablement, telemetry definitions and change policy.
- **Engineering Teams:** select and validate eligible tasks, review code, operate tests and deployment approvals.
- **Security/Legal/Privacy:** assess source-code access, vendor retention, incident handling, supply-chain threats, data classification and contractual boundaries.
- **Transformation Manager:** drive program plan, partner account governance, benefits evidence, onboarding and escalations.
- **Delivery/Platform Team:** enterprise identity, network, repo integration, incident response, change management and usage reporting.

## Agent permissions and bounded autonomy
Agents may propose changes on a dedicated branch only where approved. They must not merge to protected branches, expose secrets, deploy to production, change financial/HR permissions or override security policies without explicit controls. Require independent CI/tests, human code review, transparent activity logs, workflow abort/recovery and role-specific access.

## RACI example
| Outcome | Accountable | Responsible | Consulted |
|---|---|---|---|
| Use-case success definition | Eng VP | Team leads, transformation | Finance |
| Access approvals | Security | Platform engineering | Legal, repository owners |
| Engineer onboarding | Head of Engineering | CoE / enablement | Cognition account delivery |
| Model/tool incident handling | Security + Platform | Named incident commander | Engineering |
| Value signoff | CFO | Transformation + Analytics | Engineering |
| Cross-account playbook | Program sponsor | CoE | Customer delivery teams |

## Reusable CoE artefacts
Use-case intake form, repo-readiness checklist, training/onboarding deck, threat model, prohibited tasks list, success/failure coding guide, rollout checklist, service desk runbook, manager enablement workshop and monthly sponsor readout.

## Responsible-AI quality gate
Pilot only when user consent, credentials, segregation of duties, code reviews, IP/confidentiality, measurable baseline, audit and rollback owners are documented. Agent output is proposed work product, not automatically reliable.
