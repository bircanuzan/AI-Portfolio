# Release Gates, RACI and Escalation | Project 14

All gates below are **illustrative internal governance controls**, not Oracle-specific mandated approval steps.

## Seven release gates

| Gate | Evidence required | Accountable business owner | Decision |
|---|---|---|---|
| G0 Demand & scope | Business value, affected entities, module scope, estimated cost, sponsor | HR portfolio sponsor | Prioritize / defer |
| G1 Design readiness | Requirements, integrations/dependencies, privacy and security review, acceptance criteria | Process owner + IT architecture | Approve design assumptions |
| G2 Test readiness | Test cases mapped to requirements; testers; data controls; environments confirmed by technical team | UAT lead + technical lead | Start testing |
| G3 UAT exit | Execution evidence, pass rate, all critical failures reviewed, agreed workarounds | HR business process owner | Accept / remediate |
| G4 Release readiness | Cutover plan, support ownership, access validation, rollback/contingency for customer-controlled changes | Change advisory board | Go / conditional go / no-go for controllable changes |
| G5 Hypercare acceptance | Monitoring, daily defect burn-down, service desk handover, key process reconciliation | Service operations manager | Stabilized / extend hypercare |
| G6 Benefits review | Adoption, performance and financial/operational impacts vs original objectives | Portfolio sponsor | Close / follow-up |

## Indicative timeline — customer-controlled work

- **T-20 to T-11 business days:** review Oracle readiness notes, impact assess HR policies, integrations and reports; establish affected populations and test owners.
- **T-10 to T-6:** finish regression pack, data/privacy review, access and environment readiness confirmation.
- **T-5 to T-2:** execute UAT, triage defects, document exception decisions, prepare business communications.
- **T-1:** hold a release-readiness forum and archive sign-off evidence.
- **T+1 to T+10:** monitor critical workflows, log incidents, route fixes to technical owners, report business impact.
- **T+30:** review benefits and service indicators.

*These offsets are a teaching example, not a representation of Oracle's exact test/production cadence. Always use the client's actual schedule.*

## RACI (A = accountable; R = responsible; C = consulted; I = informed)

| Activity | Portfolio lead | HR process owners | IT / Oracle partner | Service ops | Security |
|---|---|---|---|---|---|
| Release scope & priorities | A/R | C | C | C | I |
| Business acceptance criteria | C | A/R | C | I | C |
| Technical build & integration | I | C | A/R | C | C |
| Business UAT | R | A/R | C | C | C |
| Security/privacy validation | I | C | R | I | A |
| Production deployment | I | C | A/R | C | C |
| Incident triage & SLA reporting | C | C | R | A/R | C |
| Executive readiness report | A/R | C | C | C | C |

## Release decision policy — example only

**No-go for discretionary changes** if any open P0 issue, failed critical payroll reconciliation, failed security/privacy control, or unresolved critical integration dependency is present. A conditionally accepted lower-priority defect requires owner, workaround, due date and formal HR risk acceptance.

**Mandatory Oracle quarterly updates** cannot be treated as automatically postponable by an internal committee. Escalate issues via the platform provider's published process, document business contingencies, and coordinate support.

## Evidence archive

Each change record should link requirements, test cases, signed UAT results, defect dispositions, access/security decisions, communications, cutover/hypercare plan and named approvers.

[Back to project](README.md)
