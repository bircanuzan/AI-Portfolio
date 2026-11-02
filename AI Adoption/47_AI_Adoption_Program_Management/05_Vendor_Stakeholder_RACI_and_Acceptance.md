# 05 — Vendor, stakeholder and workstream coordination

## RACI for a hypothetical university pilot
R = Responsible; A = Accountable; C = Consulted; I = Informed.

| Activity | Sponsor | Programme PMO | IT / Security | DPO / Legal | Business owner | Vendor | Champions |
|---|---|---|---|---|---|---|---|
| Prioritise use cases | A | R | C | C | R | I | C |
| Classify data / approve risk | I | C | R | A | C | C | I |
| Configure approved pilot | I | C | A | C | R | R | I |
| Approve UAT and go-live | I | R | C | C | A | R | C |
| User communications / support | I | A | C | C | R | C | R |
| Accept evidence of benefits | A | R | C | C | R | I | I |
| Respond to incidents | I | R | R | A* | R | R | I |

*DPO/Legal accountability applies to privacy/legal escalation in this illustration; security incident accountability may instead sit with InfoSec according to policy. Real organisational RACI must be approved.

## Vendor evaluation checklist
- Institution controls data, retention, subprocessors and training usage.
- Identity integration, permissions and audit logging are documented.
- Model and retrieval behaviour can be tested on realistic safe scenarios.
- Export, decommissioning and incident support paths exist.
- Human-in-the-loop controls cannot be bypassed by vendor automation.
- Contract includes uptime/support commitments, service ownership, security and exit terms.
- Vendor claims of ROI or quality are independently tested against institution baselines.

## Acceptance criteria example — staff policy assistant
| Test | Pass definition | Sign-off |
|---|---|---|
| Approved source grounding | Every policy claim linked to approved current policy | HR policy owner |
| Unknown question | Model abstains and directs to human help | Product owner |
| Role-based access | Unauthorised query cannot retrieve restricted content | IT/Security |
| Incorrect policy example | Reviewer logs and corrects issue before expansion | HR + PMO |
| Privacy/retention | Approved handling meets documented DPO expectations | DPO |
| User experience | Staff can locate escalation/contact details | Change lead |

## Operating cadence
- Weekly PMO checkpoint: owners, blockers, dependency log, decisions needed.
- Weekly vendor work package review: requirements, test evidence, changes.
- Fortnightly champions call: adoption issues and improvement opportunities.
- Monthly steering pack: status, exceptions, approved benefits and next gates.

No vendor implementation or procurement engagement occurred in this simulated case.
