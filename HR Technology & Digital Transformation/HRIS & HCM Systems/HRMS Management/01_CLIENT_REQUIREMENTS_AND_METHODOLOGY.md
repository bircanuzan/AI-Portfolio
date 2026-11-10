# HRMS Management — Client Requirements and Methodology
**Context:** Fictional 2,400-employee GCC employer; assumptions are synthetic and for interview/portfolio use.

## Client requirement
The client's HRMS function must operate Oracle HCM as a governed product, not as a series of isolated support tickets. HR users require accurate, secure employee data, dependable lifecycle workflows, faster service, reliable leadership dashboards and transparent IT/vendor accountability.

### Requirement-to-acceptance matrix
| ID | Business requirement | Functional / control approach | Acceptance measure | Accountable owner |
|---|---|---|---|---|
| REQ-01 | HCM roadmap and business alignment | Sponsor-approved 12-month product roadmap; weighted value/risk/effort scoring; quarterly re-plan | 100% Wave-1 work items have owner, acceptance tests and approved priority | HRMS product owner |
| REQ-02 | Accurate employee master data | Data dictionary, required-field validations, uniqueness/effective-date checks, steward exception queues | >=99.5% mandatory field completeness, measured against sampled or full scoped population | HR data owner |
| REQ-03 | Secure roles and workflows | Access matrices, least privilege, segregation-of-duties check, documented approval paths | 100% privileged access reviewed quarterly; 0 unresolved critical access findings pre-release | InfoSec + HR |
| REQ-04 | Dependable HR integrations | Source/target mappings, ownership, feed timing, rejected-record queue and reconciliation | >=99.5% source/report reconciled; every failed transfer alerted and assigned | IT integration lead |
| REQ-05 | Predictable releases and support | UAT traceability, defect triage, cutover, rollback, hypercare and BAU transition | Zero open P1/P2 defects at go/no-go; critical path UAT 100% pass | IT release lead + HRMS owner |
| REQ-06 | Less manual HR administration | Rules-based case intake, standard approval workflow and exception handling | Case handling 25→12 min; service SLA 78→>=95% (modeled) | HR operations lead |
| REQ-07 | Governed employee-facing AI | Approved knowledge base, low-confidence human escalation, PII controls and testing | 100% flagged cases human reviewed; 0 autonomous high-impact decisions | HR + privacy + AI lead |
| REQ-08 | Actionable workforce analytics | Oracle OTBI/Analytics Publisher specification; Power BI KPI dashboard; data reconciliation | Monthly reporting within 24h; >=99.5% data reconciliation | People analytics owner |

## 7-step methodology
1. **Diagnose (Days 1–20):** Conduct HR/IT/Finance/payroll interviews, capture AS-IS processes and system issues, sample employee master data and support tickets, baseline KPIs, classify risks.
2. **Prioritise (Days 21–35):** Score initiatives for value, process frequency, legal/security risk, dependencies, time-to-value and delivery effort. Build a 12-month backlog and roadmap.
3. **Architect business controls (Days 36–60):** Define TO-BE flows, requirements, user stories, data owners, access roles, integration contracts, testable acceptance criteria and a reporting dictionary.
4. **Pilot (Days 61–85):** Prepare anonymised/synthetic validation data, configure **design prototypes only** for case routing, OCR and a policy FAQ workflow; assess error rates, safe exceptions and effort.
5. **Assure (Days 86–100):** Execute UAT plan with technical owners, defect triage, access tests, reconciliation and documentation/training readiness. This project contains the plan, not executed evidence.
6. **Release (Days 101–120):** Set go/no-go, controlled cutover, change communications, service-desk handover and 30-day incident/adoption monitoring. No real release is claimed.
7. **Optimise (Day 121+):** Monitor service quality, data exceptions, report usability and controls monthly; review product value quarterly; validate ROI with Finance.

## Functional handoffs / RACI
| Workstream | Accountable | Consulted/Responsible parties |
|---|---|---|
| Business priority and benefit | HR sponsor / HRMS owner | HR Ops, Finance, IT |
| Oracle configuration and release | IT system owner | Oracle/vendor functional consultants, HRMS owner |
| Security and privacy | InfoSec / Privacy | HR data stewards, Legal, IT |
| Payroll and employment-policy integrity | Payroll/HR policy owner | Finance, Legal, IT |
| UAT sign-off | HR process owner | HR superusers, IT QA, vendor |
| Analytics definitions | HR analytics owner | Finance, HRMS owner, data stewards |
| Automation acceptance | HR Ops product owner | InfoSec, IT, employee services |

## Primary user stories
- **HR administrator:** As an HR administrator, I can view approval state, exceptions and audit history of a worker data change so that I can process cases accurately without ad-hoc email chasing.
- **Line manager:** As a manager, I can submit a standard request through self-service and see its status without contacting HR.
- **Payroll specialist:** As a payroll specialist, I receive an approved, reconciled and time-stamped employee-change extract with clear rejection handling.
- **Leadership:** As an executive, I can review a governed workforce KPI pack with an agreed data cut-off, definitions, reconciliation and drill-down.
- **IT security:** As an access reviewer, I can certify role assignments and detect high-risk combinations before deployment.
- **Employee service agent:** As a service agent, I can review AI-suggested categorisation and referenced policy answers, then approve, reject or escalate them.

**Evidence limit:** Functional product design only; no unverified client outcomes, live Oracle system administration or deployed interfaces.
