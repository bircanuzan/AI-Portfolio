# 04 — AI UAT, value, adoption and controls

## UAT matrix
| Scenario | Correct behaviour |
|---|---|
| Approved FAQ | Return approved versioned guidance |
| Unknown topic | Abstain and route to human |
| Employee-specific salary | Refuse private answer and escalate |
| Request to bypass policy | Do not obey untrusted instruction |
| Tool unavailable | Explain outage and escalate |
| User chooses human | Honor override immediately |
| Multi-turn confusion | Clarify or hand off; never assume identity |
| Inaccurate retrieved content | Flag source provenance / review requirement |

## KPI contract
**Quality:** correct grounded answers / reviewed approved-intent questions. **Safety:** unauthorized tool attempts = 0. **Escalation quality:** valid handoffs / cases needing human. **User adoption:** active eligible employees / consented eligible population. **Productivity:** independently confirmed minutes saved on routine questions. **Cost:** provider, infrastructure, QA and staff effort per verified resolved case. **Trust:** corrections, explicit handoff rate, feedback.

## Value hypothesis (not realized result)
Baseline monthly FAQ volume and average handling time must be measured in actual tickets. Savings = verified eligible volume × *proved* time released × relevant loaded cost, less AI run costs, human review and support. A time-release metric must not be called cash savings absent finance approval.

## Risk/controls
Human accountability for decisions; access only approved corpora; content/version references; privacy and retention impact assessment; consent; LLM prompt injection checks; least-privilege scoped service accounts; auditability; data residency review; safe fallback; incident monitoring.

## Adoption plan
Partner with HR service agents in shadow mode, hold training and feedback sessions, publish accessible instructions, log correction themes, pilot with controlled cohort, and only expand after owner-approved evaluation.

## Leadership / consulting demonstration
Steering group: business sponsor (HR COO), product owner, engineering lead, data owner, risk/legal and InfoSec. Weekly product review, backlog refinement, UAT signoff and decision log. No interviews, production results or client work are claimed.
