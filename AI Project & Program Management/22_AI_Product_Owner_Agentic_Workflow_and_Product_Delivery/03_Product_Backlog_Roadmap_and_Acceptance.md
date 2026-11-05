# 03 — Product backlog, release priorities and acceptance

| Priority | Epic/story | Acceptance criterion |
|---|---|---|
| P0 | Public HR FAQ lookup | Approved source returned, no invented rule |
| P0 | Sensitive query detection | Payroll or identity-specific queries always escalate |
| P0 | Explicit human request | Always support human override/handoff |
| P0 | Prompt injection and unsafe tool denial | Never follow embedded instructions to access secrets |
| P0 | Tool/API failure | Safe abstention + support handoff |
| P1 | Versioned RAG knowledge prototype | Grounded source/version evidence and citation evaluation |
| P1 | User correction flow | Acknowledge uncertainty, record safe feedback |
| P1 | Analytics view | Quality, cost and human intervention with stable denominator |
| P2 | Regional language support | Qualified language-review and accessibility test |

## Delivery stages
**Sprint 0:** discovery, baselines, consent, risk and tool inventory. **Sprint 1:** deterministic secure MVP and tests. **Sprint 2:** user feedback, evaluated retrieval option, usability and negative tests. **Sprint 3:** bounded stakeholder UAT and operations support design. **Release gate:** security/legal/HR owner sign-offs, accessibility, audit, runbook and revert plan.

## Definition of ready
Problem framed; target user and measurable KPI clear; authorized data available; acceptance tests written; permission and failure state defined; engineer estimate reviewed.

## Definition of done
Executable tests pass; UAT and exceptions documented; human override works; logging and incident ownership signed; data governance approved; product owner accepts behavior using evidence. Repo simulator is *not* a production release.
