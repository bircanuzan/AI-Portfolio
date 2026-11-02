# 01 — Program Charter and Integrated Delivery Plan

**Scope:** Govern simultaneous fictional financial-risk SaaS integrations for Atlas Bank and Beacon FinTech.

## Outcomes and boundaries
Each client has an accepted interface contract, controlled sandbox evidence, business-owned UAT, data/security review, recorded release approvals and monitored handover. The program **excludes** actual financial decisions, real personal data, live fraud model training and any representation that the vendor's proprietary API has been implemented.

| Workstream | Atlas Bank (fictional) | Beacon FinTech (fictional) |
| --- | --- | --- |
| Business goal | Feed risk event data into a human review workflow | Deliver alerts reliably to a client review system |
| Critical technical dependency | Signed device and timestamp field mapping | Replay-safe webhook receiver |
| Business acceptance | Client Head of Risk | Client Product Owner |
| Technical acceptance | Client Integration Lead | Client Platform Lead |
| Proposed release target | 20 Nov 2026 | 18 Nov 2026 |
| Current constraint | Mapping approval past planned date | P1 duplicate-event blocker |

## Integrated work breakdown
1. Discovery: stakeholders, outcomes, scope and acceptance criteria.
2. Technical contracting: API/event schemas, security, data minimization, monitoring, retry model.
3. Sandbox: connectivity, payload mapping, response/error handling and negative-path test evidence.
4. UAT: business scenarios, human approval routing, observability, evidence and defect closure.
5. Go/No-Go: signed engineering, risk/security, client business and sponsor decisions.
6. Hypercare: monitoring, owner handoff, incident procedure and exit evidence.

## Quality, time and decision gates
| Gate | Exit evidence | Accountable role |
| --- | --- | --- |
| G0 scope baseline | Signed scope + exclusions | Client Sponsor |
| G1 interface contract | Agreed version/schema, authentication and data handling | Client Technical Lead |
| G2 sandbox readiness | Synthetic payloads, error-path tests, replay/reconciliation | Integration Engineering |
| G3 UAT | Business test pack, defects disposition, signoff | Client Product Owner |
| G4 launch approval | Zero open P1 issues, rollback rehearsal, recorded go/no-go | Client Sponsor |
| G5 hypercare exit | Runbook, incident contacts, monitored stability, BAU ownership | Operations Lead |

**Escalation:** A security/data integrity P1 triggers immediate same-day review; critical-path signoff late by >2 business days requires a formal mitigation owner and reforecast; release plans cannot be silently re-baselined. Scope changes must include Product, Engineering and sponsor decisions.

The [structured milestone register](../data/milestones.csv) captures baseline versus actual and explicit dependencies.
