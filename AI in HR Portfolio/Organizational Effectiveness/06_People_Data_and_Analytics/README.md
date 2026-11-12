# 06 | Data Integrity, People Analytics & Management Reporting

## Position-led source of truth
Recommended architecture: HRIS position and employee effective-dated records → validation and role/grade dictionary → payroll, finance and ATS reference checks → approved Group analytics model → row-level-secured dashboard and committee pack. Define Group Legal Entity and Cost Centre master keys with a change-control owner.

## Monthly close reconciliation
- Employee ID and position ID uniqueness, valid active organisational unit, grade and position lifecycle.
- Incumbency: unfilled position, multiple incumbent, missing position, frozen seat or wrong reporting unit.
- Annual pay-base reconciliation between HRIS and payroll with tolerance and effective-date review.
- Finance budget vs authorised posts; ATS requisitions with invalid/unapproved position; contingent register vs supplier invoices.
- Org chart effective date, manager IDs, hierarchy loops and highest-risk exceptions.
- Exception record: source system; affected record; severity; business owner; due date; root cause; fix; sign-off; audit reference.

## Example local defect
The case deliberately contains E02 HRIS annual base AED 360,000 and payroll AED 355,000. The engine flags the AED 5,000 discrepancy instead of silently treating one system as correct. The proper response is to investigate effective dates and authoritative evidence, not automatically overwrite payroll or employee records.

## People data quality and privacy
Gold metrics: match rate; duplicate position count; unowned exceptions; days to resolution; late approved effective-dated changes; approved position-to-ATS linkage; pay-data access exceptions. Make restricted pay and identity detail visible only to authorised roles. Sample files hold invented role/ID values, not real employees.

## Executive dashboards
Monthly vertical scorecard: occupied FTE, vacant authorised posts, cost-to-budget, contractor ratio where available, critical roles, grade consistency exceptions, data quality, hiring exceptions and Group People deliverable health. Annual People Report: methodology, year-on-year definitions, assurance, data caveats and governance sign-off.

## HR technologies (design options only)
Oracle Fusion HCM, SAP SuccessFactors Employee Central and Workday for HRIS sources; Power BI/SQL for reporting; Power Automate for approval routing; OpenAI/Azure OpenAI/Copilot for constrained summarisation with provenance and human review. **None connected or deployed in this work sample.**
