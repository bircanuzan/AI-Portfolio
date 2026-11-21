# 01 — Business Case, Product Ownership & Delivery Backlog

## Fictional client requirements
**Organisation:** Gulf Horizons Group (synthetic multi-entity holding company). **Sponsor:** D&T leadership. **Product owner:** AI Solutions Manager. **Scope:** corporate functions, customer experience, learning/communications and subsidiary teams.

### Baseline problem / decision
No reliable central AI inventory; overlapping AI subscriptions; inconsistent risk reviews; unclear access/renewals; fragmented adoption/training; no defensible usage and ROI reporting. A central AI product and delivery operating model should accelerate safe adoption while retaining local business accountability.

## Objectives and acceptance criteria
| Business objective | Proposed deliverable | Pilot acceptance gate |
|---|---|---|
| Visibility | Enterprise AI tool register | 100% pilot tools assigned owner, use case and renewal date |
| Safety | Approval workflow | 100% pilot tools receive applicable Security/Legal/DPO decisions before production |
| Delivery | Governed project plans | Sponsor-approved scope, acceptance tests and rollback |
| Adoption | Training and champions | Pilot users complete onboarding; usage measured after 30 days |
| Value | Finance review | Costs reconciled, benefit assumptions evidenced and validated |
| Resilience | Support & escalation | Priority 1 incident path tested and vendor SLA owner identified |

**Targets are proposed pilot thresholds, not achieved outcomes.**

## Product management workflow
Discovery interview → use-case entry → feasibility/risk triage → weighted prioritisation → vendor comparison → benefit/cost forecast → pilot charter → procurement and data review → release/UAT → product adoption → benefits review → renewal/retire decision.

## Prioritisation rubric
Score each on 1–5: strategic alignment 25%, business value 25%, readiness 15%, user impact 15%, risk reduction 10%, speed to deploy 10%. Separately classify regulatory/security blockers as **non-compensating gates**—high commercial benefit cannot override a failed safety control.

## Example product backlog (synthetic)
| ID | User story | Success test | Priority |
|---|---|---|---|
| AI-01 | As a subsidiary lead I can request an approved AI tool | Intake has business owner, purpose, data class and budget | P0 |
| AI-02 | As D&T I see a single tool register | Tool, owner, cost, access, renewal, risk gate and status populated | P0 |
| AI-03 | As Procurement I receive timely renewal decisions | 90/60/30-day workflow and approval record | P0 |
| AI-04 | As IT Security I can block unapproved data flows | No provisioning without relevant approval | P0 |
| AI-05 | As a business champion I can onboard users | Guide, office hour and completion record available | P1 |
| AI-06 | As Finance I can review tool value | Licence/spend reconciliation and benefits assumptions visible | P1 |
| AI-07 | As Support I can escalate a tool outage | P1/P2 decision tree with named vendor contacts | P1 |
| AI-08 | As product owner I can assess new vendors | Weighted scorecard, risk gates and recommendation memo | P2 |

## Product ownership artifacts
- Quarterly portfolio roadmap including **pilot, scale, optimize, retire** decisions.
- Problem statements and functional/nonfunctional requirements, risk/assumption log, dependency map and change requests.
- Vendor decision record with alternatives, scope, commercial context and signoffs.
- Release readiness checklist with user acceptance tests, training and service support.
- Monthly product review: activation, value, incidents, licensing and next-step decisions.

## Illustrative 12-week release sequence
Weeks 1–2 inventory and discovery; 3–4 vendor/risk assessment; 5–6 legal/procurement approvals; 7–8 controlled pilot; 9–10 UAT and training; 11–12 scaling decision and leadership report. Sequence is adjustable; no rollout bypasses risk gates.

## Key assumptions and dependencies
Tool availability, lawful data processing, commercial budget, SSO/identity compatibility, API integration feasibility, and vendor security assurance are **unknown** until independently confirmed. Dependencies: D&T, business owners, Procurement, InfoSec, Legal, DPO, IAM, Finance and Support.
