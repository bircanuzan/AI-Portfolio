# 04 — Multi-Entity Rollout, Adoption & Service Management

## Rollout structure
Programme-level roadmap with subsidiary waves; each wave has a sponsor, business/product owner, D&T delivery lead, InfoSec/DPO/Legal decisions, Procurement agreement, IT service owner, training contact, budget code and reporting cadence.

| Phase | Output | Gate |
|---|---|---|
| 0 — Discover | Use-case interviews, data classification, register | Business sponsor |
| 1 — Assess | Vendor comparison, baseline KPI, data flows, risk reviews | Security, Legal, DPO |
| 2 — Prepare | Contract, service desk setup, user policy, training | Procurement/Finance/IT |
| 3 — Pilot | Sandbox/pilot, UAT evidence, issue log, use-case tests | Product owner + control owners |
| 4 — Scale | Entity-by-entity onboarding, champions and office hours | Steering decision |
| 5 — Optimise | Usage, cost, value, incidents and licence reallocation | Monthly review |

## UAT examples
- Positive case: authorised user gets a useful output for an approved, non-sensitive workflow.
- Negative case: unapproved user/tool request is denied and logged.
- Privacy case: restricted input is blocked or routed to human support.
- Reliability: model answer is reviewed for factuality, hallucination and policy adherence.
- Operations: SSO/offboarding, incident escalation, quota/limit notifications and vendor failure fallback.
- Adoption: target users can follow documentation and raise support requests.

## Adoption and change management
- Stakeholder map: executive sponsor, subsidiary champions, business managers, IT support, Legal, DPO, procurement, Finance.
- Change narrative: outcomes, allowed use cases, boundaries and employee/customer protections.
- Champion network: 1 lead per participating business unit (illustrative target).
- Learning: 30-minute live orientation; quick reference guides; responsible AI examples; role-based training.
- Office hours: twice per week during pilot, then weekly for the first month after launch.
- Feedback loop: user survey, service-desk themes, drop-off analysis, product backlog and continuous improvement.
- Communications: sponsor kick-off, FAQ, pilot results, weekly go-live update, monthly adoption scorecard.

## Support and escalation playbook
| Severity | Examples | First action | Escalation |
|---|---|---|---|
| P1 / critical | Suspected disclosure, severe outage impacting essential operations | Contain/disable exposure; invoke incident commander | IT Security, DPO/Legal, vendor, executive sponsor |
| P2 / high | Multi-user outage, significant licence/provisioning failure | Triage, workaround and vendor ticket | IT service owner + AI Manager |
| P3 / moderate | Single-user issue or noncritical degradation | Service desk ticket and guidance | Platform administrator / vendor support |
| P4 / request | Additional seats, feature idea, training query | Intake and prioritisation | Business owner / champions |

Actual resolution SLAs are contract-dependent; no fabricated response-time guarantees.

## RAID snapshot (synthetic)
| Type | Item | Owner | Treatment |
|---|---|---|---|
| Risk | Unknown cross-border data flow | DPO | Block pilot until reviewed |
| Assumption | SSO available in selected licence | IT | Confirm feature and test |
| Issue | Low attendance in one business unit | Champion | Add role-based sessions |
| Dependency | Procurement approval before licence order | Procurement | Track steering gate |

## Handover / closure checklist
User guides and acceptable-use policy, owner mapping, runbooks, vendor support numbers, incident rehearsals, support handover, spend tagging, dashboard ownership, renewal workflow and decision log.
