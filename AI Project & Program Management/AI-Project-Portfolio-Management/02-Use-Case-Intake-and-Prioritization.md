# 02 | AI Champions: Intake, Qualification, Prioritization & Roadmap
**Scenario:** fictional regulated payments firm. All prioritization numbers are illustrative.

## Standard 12-question intake
1. Problem statement in the language of the workflow owner, not AI tool preference.
2. Process map, current pain points, manual decisions and exceptions.
3. Named executive sponsor, AI Champion, service owner and users.
4. Business baseline: volume, cycle time, error rate, escalation frequency.
5. Economic model: cost to serve, benefit hypothesis, recurring run cost.
6. Outcome and adoption KPIs; risk and service-experience constraints.
7. Candidate pattern: RAG copilot, decision support, ML, automation, analytics or no AI.
8. Data owners, source systems, completeness, freshness, sensitivity and legal basis.
9. Identity, permissions, API/integration, cloud and infrastructure dependencies.
10. Harm scenarios, hallucinations, bias, privacy and human override requirements.
11. Prototype/pilot/scale stage gates, owner capacity, training and change impacts.
12. Approval route: Architecture/DARB, InfoSec, Risk, Legal, Compliance, Procurement.

## Weighted prioritization (out of 100)
| Dimension | Weight | Interpretation |
|---|---:|---|
| Strategic alignment | 25% | Supports approved enterprise priorities |
| Benefit magnitude | 25% | Evidence-backed value at realistic adoption |
| Delivery feasibility | 20% | Scope, team availability, integrations |
| Data readiness | 15% | Availability, quality, permissions |
| Risk manageability | 15% | Controllable legal/privacy/model/security risk |

**Formula:** Score = 20 × (0.25×Alignment + 0.25×Benefit + 0.20×Feasibility + 0.15×Data + 0.15×RiskManageability). Inputs are 0–5; numerical score **never overrides blocking security/legal stage gates**.

**Worked example AI-001:** 20×(0.25×5 + 0.25×4 + 0.20×4 + 0.15×3 + 0.15×4) = **82**.
**Worked example AI-002:** 20×(0.25×4 + 0.25×3 + 0.20×4 + 0.15×4 + 0.15×4) = **75** (rounding may differ from demonstration CSV's provisional 76; recalculate before reporting).
**Worked example AI-003:** 20×(0.25×5 + 0.25×5 + 0.20×2 + 0.15×1 + 0.15×1) = **64**; put on hold despite high potential value.

## Qualification and roadmap
**Now (0–30 days):** approve AI-001 use-case brief and security-limited prototype; complete AI-002 discovery.  
**Next (31–60):** AI-001 UAT and controlled pilot; AI-002 solution review and data QA.  
**Later (61–90):** review AI-001 scale only if gates pass; re-score AI-003 after model-risk and dataset work.  
Dependencies and capacity are tracked in portfolio register; plan is sample only.

## Sample business case
**AI-001:** current manual onboarding document review: 10,000 cases/year × 12 minutes/case = 2,000 hours. If assistive summarization saves 35% of this work, gross time saved = 700 hours/year. At illustrative AED 200 fully loaded hour, gross time value = AED 140,000/year; subtract governance, inference and platform costs and validate with live baseline before investment. No guaranteed FTE reduction; retain final human controls.

## Decision / accountability
**AI Champion:** evidence and workflow; **Head of AI:** portfolio tradeoffs and funding advice; **Architecture:** design viability; **Risk/Compliance:** policy interpretation; **InfoSec:** control signoff; **Engineering:** delivery feasibility. Portfolio lead documents tradeoffs and escalates; does not self-approve control gates.
