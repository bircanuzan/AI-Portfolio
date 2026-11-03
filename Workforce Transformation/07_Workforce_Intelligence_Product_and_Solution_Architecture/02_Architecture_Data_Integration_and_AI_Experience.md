# Workforce intelligence product — reference architecture

## Logical component design
~~~mermaid
flowchart LR
A[HRIS / Workday / Oracle HCM / SAP] --> B[Approved integration + access validation]
C[Service data + trusted official market sources] --> B
B --> D[Governed work / skills / workforce graph]
D --> E[Scenario service and value register]
D --> F[Agent and decision rights register]
E --> G[Role-based workforce intelligence UI]
F --> G
G --> H{Human review / approval required?}
H -->|Yes| I[Authorized executive / HR approver]
H -->|No, low-risk output| J[Read-only insight]
I --> K[Audit + measured outcomes]
J --> K
~~~

## Data objects
- **Outcome:** objective ID, owner, leading/lagging KPIs, baseline, accepted benefit.
- **Work task:** task ID, process, volume/time source, criticality, jurisdiction, decomposition version.
- **Role / skill:** role-family ID, required skill and proficiency, source system, effective dates.
- **Agent:** name, lifecycle status, purpose, owner, allowed tools/data, risk tier, last evaluation, expiry.
- **Decision:** requested change, alternatives, confidence limits, human reviewer, signoff, appeal.
- **Value:** assumptions, costs, review/rework, impact, realized evidence, verified owner.
- **Dataset:** source, permission, geography, date, quality status, privacy classification.

## Platform design options, NOT integrations proven here
| Layer | Candidate enterprise technology | Integration validation required |
|---|---|---|
| HRIS | Oracle Fusion Cloud HCM, Workday, SAP SuccessFactors | Tenant permissions, official APIs, modules and licensing |
| Skills/learning | Oracle Grow/Dynamic Skills, LMS/LXP; equivalent skill graphs | Taxonomy mapping, SSO, release readiness |
| Agent implementation | Microsoft Copilot Studio / Azure AI Foundry / approved LLM service | Evaluation, tool scopes, RAG, action permissions |
| Workflow | Power Automate / governed API gateway | Idempotency, error queues, identity and approvals |
| Analytics | Power BI / Tableau / Oracle Analytics | Row-level security, quality, metric governance |
| Infrastructure | OCI or Azure, dependent on client standards | Cloud topology, residency, encryption and cost |

Vendor references are potential options, not claims of configuration or experience in this project.

## Agent experience principles
- Explicit source citation, freshness, uncertainty and human review status.
- Never treat a language-model generated recommendation as authorization.
- No write actions on hiring, termination, compensation, employee appraisal or payments.
- Appeals and override feedback flow to a human; disagreement must be traceable.
- Use separate evaluation sets for grounded answers, unsafe requests, denied access, stale sources and accessibility.
- Telemetry distinguishes user adoption from true outcome/quality/value.

## Data / security threat model
Prompt injection from retrieved content; cross-subsidiary leakage; stale employee relationships; role/skill model bias; model output injected into finance; missing consent; incorrect currency assumptions; ambiguous user identity; agent access not revoked. Countermeasures require server-side enforcement, independent security assessment, least privilege, source versioning, segregated duties and incident rollback.

## REST contract and boundary
The [OpenAPI spec](spec/openapi.yaml) defines **only** a hypothetical, read-only use-case triage endpoint. This file is not proof of a running HTTP server or integration.

## Pilot exit evidence
Versioned benchmark with labeled expected outcomes, independent review, source/data rights, SLA and error rate, human escalation recall, employee impact assessment, stakeholder acceptance, measured adoption, cost-per-correct-outcome and rollback rehearsal. Avoid using synthetic scores as commercial claims.