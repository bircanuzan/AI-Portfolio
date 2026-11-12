# Human–AI work orchestration and safety runbook

## Design pattern: work allocation with a human endpoint
1. User submits an authenticated service request.
2. Intake classifier validates schema and access entitlement.
3. Risk gate identifies personal, protected or consequential requests.
4. Low-risk request may be routed to an **approved** bounded agent role.
5. Agent only drafts or reports within approved data/tool scope; no workplace action is executed.
6. Policy owner, user or independent reviewer verifies as required.
7. Escalated cases enter the named human service queue.
8. Every decision and error has a correlation ID, monitoring and a review owner.

## Allowed behaviors in prototype
- General HR policy question -> A-POL when in PILOT/ACTIVE with current policy version and permission.
- Aggregate approved KPI summary -> A-RPT with approved analytics scope and permission.
- Sensitive employee-specific case, adverse action, payment, or unapproved request -> **HUMAN_REVIEW** with zero automated action.
- Agent in SHADOW/RETIRED/SUSPENDED -> **HUMAN_REVIEW**.

The local demonstrator exercises routing decisions, **not model-generated answers or real approvals**.

## Technical reference architecture (proposed, not connected)
| Layer | Enterprise option | Critical control |
|---|---|---|
| Identity and permissions | Microsoft Entra ID / Oracle IAM | Least privilege, short-lived service identity |
| Approved enterprise knowledge | SharePoint, governed HCM policy source | Source version, redaction, document ACLs |
| Workflow/agent build | Copilot Studio / Azure AI Foundry / approved orchestration service | Read-only tools first; deny risky writes |
| Integration | Power Automate / governed APIs / queue adapters | Signed calls, retries, idempotency, trace IDs |
| Analytics and monitoring | Power BI / secured operational telemetry | Outcome vs baseline, disaggregated error rates |
| Governance | Human service owner, CISO, privacy, legal and risk committee | Testing, go/no-go, appeal, kill switch |

## Failure and abuse evaluation plan
- Prompt injection in retrieved text; direct access requests and bypass phrases.
- Personal data leakage attempts and incorrect cross-subsidiary access.
- Unsupported or conflicting policy; stale version; missing owner.
- Hallucinated confirmation of action; no actual side-effect tools exist in prototype.
- Unavailable model / integration / approval queue; must fail closed.
- Agent drift and increased human correction burden after versions change.

## Recorded output definition
Input/request class, authenticated user role, agent lifecycle state, policy version, selected route, reason, correlation ID, permitted/no-op classification, expected decision and observed decision. Maintain dated traces when executing real tests.

## Exit criteria for an actual pilot
No high-severity unauthorized actions, pre-agreed decision quality thresholds on independently labeled holdouts, tested human escalation, privacy/security approval, rollback rehearsal, training, business acceptance and budgeted oversight. **No universal threshold is claimed here.**

## Work division
Existing [Project 42](../42_Human-AI_Workforce_Design_and_Agent_Governance/) evaluates an HR service agent's competency and governance concepts. **This project** designs multiple agent identities and shared operational routing, with explicit enforcement of status, allowed task classes and owner escalation.