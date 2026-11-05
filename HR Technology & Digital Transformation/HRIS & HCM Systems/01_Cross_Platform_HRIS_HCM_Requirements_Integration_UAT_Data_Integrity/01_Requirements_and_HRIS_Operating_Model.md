# Requirements & HRIS operating model

## Stakeholder discovery
HR Operations owns accurate employee master information and employment events; HRIS Product Owner translates policy/process requirements to the vendor; IT owns availability, security and integrations; Payroll/Finance own approved wages and reconciliations; Legal/Compliance determine applicable UAE employment and privacy obligations.

## Key use cases
| ID | As a... | Need... | Acceptance criteria |
|---|---|---|---|
| HRIS-01 | HR officer | Create employee from approved hire | Unique employee key, legal entity, signed contract, start date and approval evidence |
| HRIS-02 | Payroll lead | Receive changes by effective date | Every pay change has version, approval, before/after delta and period |
| HRIS-03 | HR manager | Process employee transfer | Old/new entity, responsible owner and cutover are explicit |
| HRIS-04 | Employee | Submit personal-detail update | Verify identity, mask sensitive details, approval log and SLA |
| HRIS-05 | HRBP | Initiate employee exit | EOS review route, asset/access return, final-pay approval (not automatic entitlement) |
| HRIS-06 | HRIS analyst | Investigate failed interface | Correlation ID, retry count, incident owner and reconciliation |
| HRIS-07 | HR lead | Inspect completion/accuracy KPIs | Approved refresh timestamp, entity-level access and test reconciliation |

## Product operating model
- **Source of truth:** designate target HRMS for employee master and effective-dated employment events; do not permit unmanaged Excel overrides.
- **Ownership:** HR Operations=business data; Payroll/Finance=financial validation; IT=integration/identity; Compliance/Legal=regulatory applicability; Vendor=software support.
- **Change management:** prioritised backlog, release criteria, process owner signoff, role-specific training and change communication.
- **Artifacts:** process inventory, requirement traceability, configuration decision log, issue register, data mapping, UAT evidence, cutover checklist, hypercare dashboard.

## Example 6-month project plan
Weeks 1-4 discovery and quality baseline; 5-8 process/fit-gap and mapping; 9-12 configuration review/integration prototype; 13-18 migration rehearsals/UAT; 19-21 cutover readiness; 22-24 hypercare and handover. Dates are illustrative, dependent on scope and vendor access.

**Important distinction:** This project is a business analyst / HRIS delivery design, not an assertion of directly configuring any production HRMS.