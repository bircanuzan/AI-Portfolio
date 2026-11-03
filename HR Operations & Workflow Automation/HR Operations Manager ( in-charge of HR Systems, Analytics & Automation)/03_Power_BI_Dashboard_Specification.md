# Power BI: data model, KPIs, example DAX

**Deliverable type:** Power BI-ready analytic design and DAX examples. No `.pbix` file, licensed tenant, connected finance system or screenshot of live dashboards is claimed.

## Proposed star schema
- `DimEmployee`: EmployeeKey (surrogate), pseudonym, BusinessUnitKey, LegalEntityKey, JoinDate, ExitDate; no bank account, full name, national ID or personal contact details.
- `DimDate`: DateKey, CalendarDate, Month, FiscalYear.
- `DimControl`: ControlKey, ControlCode, Severity, AccountableFunction.
- `FactPayrollBatch`: PayrollLineID, EmployeeKey, DateKey, ProposedNetAED, AuthorisedNetAED, ApprovalState, ReconciliationState.
- `FactPayrollExceptions`: ExceptionID, PayrollLineID, ControlKey, OpenedAt, ClosedAt, Status, OwnerFunction, IsBlocking.
- `FactHRService`: TicketID, EmployeeKey, OpenedDate, ClosedDate, SLAHours, WithinSLA, ContactChannel, SelfServiceResolved.
- `FactLifecycleChanges`: EventID, EmployeeKey, EffectiveDate, ChangeType, ApprovedFlag.

Use a single-direction many-to-one relationship from facts to shared dimensions; do not create ambiguous many-to-many relationships. RLS by authorised HR entity/business unit and a separate aggregated executive view.

## Illustrative measures (validate in actual Power BI schema)
```DAX
Payroll Lines = COUNTROWS(FactPayrollBatch)

Approved Payroll Lines =
CALCULATE([Payroll Lines], FactPayrollBatch[ApprovalState] = "Approved")

Payroll Approval Rate % =
DIVIDE([Approved Payroll Lines], [Payroll Lines])

Open Payroll Exceptions =
CALCULATE(
    COUNTROWS(FactPayrollExceptions),
    FactPayrollExceptions[Status] <> "Closed"
)

Blocking Payroll Exceptions =
CALCULATE(
    COUNTROWS(FactPayrollExceptions),
    FactPayrollExceptions[IsBlocking] = TRUE(),
    FactPayrollExceptions[Status] <> "Closed"
)

Exception Affected Lines % =
DIVIDE(
    DISTINCTCOUNT(FactPayrollExceptions[PayrollLineID]),
    [Payroll Lines]
)

HR Service SLA % =
DIVIDE(
    CALCULATE(COUNTROWS(FactHRService), FactHRService[WithinSLA] = TRUE()),
    CALCULATE(COUNTROWS(FactHRService), NOT ISBLANK(FactHRService[ClosedDate]))
)

Employee Self-Service Resolution % =
DIVIDE(
    CALCULATE(COUNTROWS(FactHRService), FactHRService[SelfServiceResolved] = TRUE()),
    COUNTROWS(FactHRService)
)
```

**Dashboard 1: Executive HR Operations scorecard** — headcount movement, open blockers, payroll approval rate, HR service SLA, trends against baselines.  
**Dashboard 2: HRMS master data quality** — missing effective dates, duplicates, stale statuses, unresolved role changes.  
**Dashboard 3: Payroll & EOS reviews** — variances, blocking control categories, approvals, pending expert EOS reviews; never publish individual amounts to non-authorised viewers.  
**Dashboard 4: Employee experience** — ticket volume, SLA, self-service resolution, onboarding completion, digital channel adoption.

## Power Query transformation plan
1. Parameterise period/legal entity and source folder; reject missing required fields.
2. Apply explicit types and Decimal/Currency controls; reject negative or malformed fields rather than silently coercing.
3. Use a pseudonymous employee key, strip bank details and direct identifiers.
4. Merge HRMS/payroll only on validated entity + employee ID, not names.
5. Report unmatched records, duplicates and count/total reconciliation before refresh.
6. Persist only authorised history and an approval/reconciliation timestamp.

**Management decisions:** Which control requires investment? Which service queues are breaching SLA? What pay or HRMS change process creates repeat errors? All improvements require a measured before/after baseline.