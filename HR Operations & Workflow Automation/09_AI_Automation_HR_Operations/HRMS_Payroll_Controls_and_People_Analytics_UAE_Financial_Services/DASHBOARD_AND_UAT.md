# Power BI dashboard design & user acceptance testing

This is a **Power BI-ready specification**, not an exported PBIX or an assertion that a Power BI tenant was connected.

## Decision questions
- Are employee HRMS records complete and consistent before each payroll cycle?
- Which exception types and owners have the greatest outstanding backlog?
- Are exited employees awaiting legally reviewed EOS cases?
- How long do employee services take, and how many are automated with human approvals?

## Proposed star schema
- **FactHRMSChecks:** SnapshotDate, EmployeeID (pseudonym), CheckID, IsPass, Owner, BusinessUnit.
- **FactPayrollExceptions:** BatchID, EmployeeID, ControlType, Status, RaisedAt, ClosedAt, ApprovalStatus.
- **FactHRServiceRequests:** CaseID, CaseType, OpenedAt, ClosedAt, SLAHours, ApprovedBy, Resolution.
- **DimDate**, **DimBusinessUnit**, **DimControl**, **DimEmployee** (only non-sensitive analytical attributes).

## Core measures (illustrative DAX)
\`\`\`DAX
Unique Employees = DISTINCTCOUNT(DimEmployee[EmployeeID])

Outstanding Payroll Exceptions =
CALCULATE(COUNTROWS(FactPayrollExceptions), FactPayrollExceptions[Status] <> "Closed")

Payroll Exception Rate =
DIVIDE(
    DISTINCTCOUNT(FactPayrollExceptions[EmployeeID]),
    [Unique Employees]
)

HRMS Completeness % =
DIVIDE(
    CALCULATE(COUNTROWS(FactHRMSChecks), FactHRMSChecks[IsPass] = TRUE()),
    COUNTROWS(FactHRMSChecks)
)

Cases Closed Within SLA % =
DIVIDE(
    CALCULATE(COUNTROWS(FactHRServiceRequests), FactHRServiceRequests[WithinSLA] = TRUE()),
    CALCULATE(COUNTROWS(FactHRServiceRequests), NOT ISBLANK(FactHRServiceRequests[ClosedAt]))
)
\`\`\`

Suggested dashboard pages: **Executive Scorecard**, **HRMS Data Quality**, **Payroll Exceptions & EOS**, **HR Service SLA**, **Employee Self-Service & Automation**.

Use drill-through only for authorised staff; executive pages should show anonymised or aggregate results. No live employee data or actual Power BI output was accessed here.

## Proposed UAT cases
| UAT ID | Action | Expected result |
| --- | --- | --- |
| UAT01 | Duplicate employee ID in batch | Blocks release and produces traceable exception |
| UAT02 | Approved 10,000 / proposed 10,100 | Shows amount variance needing reconciliation |
| UAT03 | No verified bank reference | Payment withheld pending verification |
| UAT04 | Payment while approval pending | Payment blocked; request goes to owner |
| UAT05 | Exited employee / EOS review pending | Specialist EOS case initiated; no auto-calculation |
| UAT06 | Authorised aggregate dashboard refresh | KPIs reflect approved latest reconciled snapshot |
| UAT07 | Unauthorized user opens payroll row | Access denied and attempt logged |
| UAT08 | Service request exceeds SLA | Reminder/escalation routed to named human owner |

**Exit criteria:** all critical controls passed in a controlled test environment, no high-severity unresolved UAT failures, written HR/Finance/IT approval, data reconciliation evidence and updated process documentation.

## Adoption and benefits measurement
Track baseline and post-change manual handling time, exception rate, release-delay causes, ticket SLA, employee self-service rate, rework volume and manager satisfaction. Do not claim these improvements until measured in a real environment.