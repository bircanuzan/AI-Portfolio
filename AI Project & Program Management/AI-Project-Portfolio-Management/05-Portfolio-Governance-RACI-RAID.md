# 05 | Portfolio Governance, DARB, RACI & RAID
**Status:** demonstration of governance operating discipline; no real reviews/approvals performed.

## Governance cadence
| Cadence | Forum | Outputs |
|---|---|---|
| Weekly | AI Champions + portfolio delivery | Action/decision log, milestone tracking, RAID |
| Biweekly | Business + Engineering + Data + Security | Design tradeoffs, capacity and blockers |
| Monthly | Head of AI / Portfolio Steering | RAG health, benefits, funding decisions, escalations |
| At gates | DARB / Architecture / InfoSec / Risk / Legal / Compliance / Procurement | Formal approvals and conditions |

## DARB / InfoSec / Risk submission pack checklist
- [ ] Business owner and AI Champion identified.
- [ ] Business problem and BRD accepted; alternatives evaluated.
- [ ] Architecture diagram, APIs, environments and integration dependencies.
- [ ] Data source ownership, lineage, classification, access, retention, masking and residency.
- [ ] Model behavior specification, human-in-the-loop design and audit trails.
- [ ] Security threat assessment including prompt injection and access misuse.
- [ ] Risk, Legal, Compliance, Procurement and vendor due diligence where applicable.
- [ ] Testing plan, pass/fail criteria, operational fallback, incident handling.
- [ ] Reusable AI Factory component request and production support owner.
- [ ] Approvers, decisions, conditions and evidence stored in a controlled register.

## RACI (simplified)
| Activity | Portfolio Lead | Sponsor | AI Champion | Forward Deployed AI Lead | Data Scientist | Architecture/InfoSec/Risk |
|---|---|---|---|---|---|---|
| Intake and pipeline | A/R | C | R | C | C | I |
| Business value & process requirements | R | A | R | C | C | C |
| Technical solution quality | C | I | C | A/R | R | C |
| Security / model risk approvals | C | I | C | R | R | A/R |
| UAT business signoff | R | A | R | C | C | C |
| Portfolio steering/reporting | A/R | C | C | C | C | C |
| Production operational acceptance | R | A | C | R | C | R |

**RACI note:** This is an indicative structure; actual accountable owners must follow corporate policy. No portfolio lead substitutes for risk / security approval.

## RAID log - illustrative
| ID | Type | Owner | Severity | Impact | Mitigation / next action | Escalate |
|---|---|---|---|---|---|---|
| R-01 | Risk | Security Lead | High | Confidential data exposure | Enforce synthetic/redacted-only prototype data; security review | Before any live-data use |
| I-02 | Issue | Policy Owner | Medium | Outdated content versions | Produce approved versioned corpus | Weekly meeting |
| D-03 | Dependency | Enterprise Architect | High | API design not agreed | Sandbox read-only interface review | DARB |
| A-04 | Assumption | Operations Sponsor | Medium | Handling-time baseline unverified | Sample 50 historical cases | Prior to benefit claim |
| R-05 | Risk | Model QA Owner | High | Unsupported KYC advice | Abstention and mandatory reviewer | Model-risk gate |

## Escalation and decision rights
Portfolio lead maintains an evidence-based blocker register, assigns owners and target dates, and escalates overdue high-severity issues to Head of AI or relevant approval forum. Stakeholder disagreement is documented with options, recommendation, impact and a decision date. Blocked governance gates cannot be silently waived.

## Quality standards
**Definitions:** accepted / at-risk / blocked; next-milestone owner; last evidence date; action due date. **Confidence** must include evidence from data/controls/capacity, not presentation polish.
