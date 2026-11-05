# 04 - Oracle transformation roadmap, UAT and executive governance

## Indicative 90-day inception plan (not an actual engagement)

| Window | Business and technical work | Gate / artifact |
|---|---|---|
| Days 1-15 | Stakeholder discovery, subsidiaries and licensed application inventory, operating baselines, process/controls map, privacy initial screening | Discovery report + agreed scope / constraints |
| Days 16-30 | Standardized capabilities, functional requirements, solution options, data sources, integration feasibility, roles and ownership | Architecture option decision + BRD |
| Days 31-45 | Logical HCM/ERP/integration design, security/privacy assessment, interface contracts, observability, data and analytics design | Design review / ADRs |
| Days 46-60 | Synthetic proof-of-value, unit tests, migration/exception rehearsal, proposed UAT scripts, support model | Demonstrable acceptance evidence |
| Days 61-75 | Vendor/technical feasibility, indicative effort and license assumptions, change impacts, subsidiary readiness and training plan | Pilot go/no-go recommendation |
| Days 76-90 | Governance handover, release-stage plan, test and reconciliation ownership, benefits baseline and measurement cadence | Steering decision pack and mobilization roadmap |

## Delivery roles / RACI sample

| Decision or activity | HR owner | Finance owner | EA / IT | Security / Legal | PMO |
|---|---|---|---|---|---|
| Worker event business approval | A/R | C | I | I | I |
| Cost-center master / accounting treatment | C | A/R | C | I | I |
| Integration architecture selection | C | C | A/R | C | I |
| Privacy and cyber control assessment | C | C | R | A | I |
| Business acceptance of integrated controls | A/R | A/R | R | C | C |
| Portfolio roadmap / cross-subsidiary dependencies | C | C | R | C | A/R |

R=responsible; A=accountable; C=consulted; I=informed. Any duplicate 'A' across co-owned business gates requires formal clarification before execution.

## Acceptance criteria / synthetic tests

| UAT | Test scenario | Pass condition |
|---|---|---|
| UAT-01 | Valid transfer with active cost center and approval | Accepted in staging; downstream route defined |
| UAT-02 | Unknown event type | Rejected with controlled reason |
| UAT-03 | Invalid cost center | Rejected; Finance exception owner |
| UAT-04 | Missing HR approval | Rejected; no downstream release |
| UAT-05 | Repeated event ID | Second occurrence rejected, no duplicate release |
| UAT-06 | Downstream interface unavailable | Requeue/exception with audit correlation, no silent success |
| UAT-07 | HR analyst requests sensitive finance output | Access denied |
| UAT-08 | Reconciliation mismatch | Discrepancy exposed and assigned |
| UAT-09 | Unapproved subsidiary variation | Exception escalated for governance decision |

The included Python test harness validates **staging controls only**, not Oracle APIs, access tokens or ERP transactions. UAT-06 to UAT-09 require a separate integration / identity test environment.

## RAID starter

- **Risk:** inconsistent subsidiary cost-center mapping. **Mitigation:** Finance-owned canonical reference table and signoff.
- **Assumption:** group HCM-to-ERP product/modules are licensed. **Validate:** current application inventory.
- **Issue:** undocumented ownership of rejected events. **Mitigation:** assign named queue owners, escalation SLA.
- **Dependency:** security/identity and data privacy decisions before interface pilot.
- **Risk:** enthusiasm for AI automation without human controls. **Mitigation:** explicit prohibited actions and output review.

## Steering committee one-page narrative

**Problem:** disconnected HR-to-Finance lifecycle changes cause rework and inconsistent controls (baseline TBD).  
**Decision needed:** approve architecture discovery and a limited synthetic-to-sandbox pilot, contingent on licensing/security/data review.  
**Recommended route:** canonical HCM event and finance-owned reference validation through an approved integration layer; human approvals and reconciled reporting.  
**Success:** correct event handling, no duplicate processing, controlled exceptions, auditable data ownership, stakeholder adoption and real measured baseline-to-benefit movement.  
**Unresolved:** licensing, integration feasibility, privacy, support and commercial case.

## Proof limitations

No external Oracle service is called; no vendor quote, license validation, named client commitment, implementation budget, live Oracle configuration, field mapping from an actual customer tenant or financial ROI is presented as fact.
