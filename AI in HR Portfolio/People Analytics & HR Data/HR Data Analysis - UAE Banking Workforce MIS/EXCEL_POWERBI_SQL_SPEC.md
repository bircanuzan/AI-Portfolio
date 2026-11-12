# Analyst Build Specification — Excel, DAX-style Measures & SQL

Independent design notes. Every example is fictional. These formulas are illustrative and must be reconciled to actual institution-specific definitions before deployment.

## Excel model: suggested tabs
1. **CONTROL**: as-of date, data owner, signed budget version, approved target rule, exception threshold.
2. **HRMS_SNAPSHOT**: employee ID, effective date, division, active status, Emirati grouping, FTE, annualized cost.
3. **FUNDED_PLAN**: division, approved capacity FTE, annual budget AED, illustrative national workforce share.
4. **REQ_TRACKER**: req ID, division, status, requested FTE and expected annual cost.
5. **QUALITY_CHECKS**: uniqueness, valid dates, status/FTE/cost reasonableness, orphan divisions.
6. **DIVISION_MIS**: actual HC, active FTE, national workforce FTE, approved FTE, vacancy, annual budget, active cost, variance, approved requests.
7. **MANAGEMENT_PACK**: movement bridge, budget exceptions, target variance, assumptions, approvals.

## Excel-style formulas (structured tables)
```excel
=COUNTIFS(HRMS_SNAPSHOT[Division],[@Division],HRMS_SNAPSHOT[Status],"Active")
=SUMIFS(HRMS_SNAPSHOT[FTE],HRMS_SNAPSHOT[Division],[@Division],HRMS_SNAPSHOT[Status],"Active")
=SUMIFS(HRMS_SNAPSHOT[FTE],HRMS_SNAPSHOT[Division],[@Division],HRMS_SNAPSHOT[Status],"Active",HRMS_SNAPSHOT[EmiratisationGroup],"Emirati")
=MAX(0,[@FundedFTE]-[@ActualFTE])
=[@ActualAnnualizedCostAED]-[@BudgetAnnualAED]
=IFERROR([@EmiratiFTE]/[@ActualFTE],0)
=MAX(0,ROUNDUP([@FundedFTE]*[@IllustrativeTargetShare]-[@EmiratiFTE],0))
```
**Warning:** A simple COUNTIFS assumes one active row per employee at cutoff. First deduplicate and effective-date HRMS records, and reconcile against payroll/Finance under the approved institutional process.

## DAX-style measures (conceptual; validate relationships & filters)
```dax
Active FTE =
CALCULATE(SUM(Employees[FTE]), Employees[Status] = "Active")
Emirati FTE =
CALCULATE([Active FTE], Employees[EmiratisationGroup] = "Emirati")
Funded FTE = SUM(FundedPlan[FundedFTE])
Vacancy FTE = MAX(0, [Funded FTE] - [Active FTE])
Actual Cost Annual AED =
CALCULATE(SUM(Employees[AnnualCostAED]), Employees[Status] = "Active")
Cost Variance AED = [Actual Cost Annual AED] - SUM(FundedPlan[BudgetAnnualAED])
Emirati FTE Share = DIVIDE([Emirati FTE], [Active FTE])
```

## SQL control patterns (illustrative SQL, dialect-specific)
```sql
-- Month-end duplicate check: must return zero records
SELECT employee_id, as_of, COUNT(*) AS n
FROM hrms_snapshot
GROUP BY employee_id, as_of
HAVING COUNT(*) > 1;

-- Current active headcount and annualized cost by division
SELECT division, COUNT(DISTINCT employee_id) AS active_hc,
       SUM(fte) AS active_fte,
       SUM(annual_cost_aed) AS annualized_cost_aed
FROM hrms_snapshot
WHERE status = 'Active' AND as_of = :report_cutoff
GROUP BY division;

-- Compare actual FTE to approved positions (after source validation)
SELECT p.division, p.funded_fte, COALESCE(a.actual_fte,0) AS actual_fte,
       p.funded_fte - COALESCE(a.actual_fte,0) AS signed_vacancy_fte
FROM funded_positions p
LEFT JOIN (
 SELECT division, SUM(fte) AS actual_fte
 FROM hrms_snapshot
 WHERE status = 'Active' AND as_of = :report_cutoff
 GROUP BY division
) a ON a.division=p.division
WHERE p.as_of = :report_cutoff;
```

## Executive pack views
- **Group overview:** active employees / FTE, approved FTE, funded vacancy, open approved requisitions, personnel-cost variance.
- **Division heatmap:** monthly FTE change, funded vacancy, national workforce share, data exceptions.
- **Emiratisation planning:** illustrative target FTE and unfilled gap by division, with source/definition footnote.
- **Forecast & sensitivity:** expected hires/leavers and cost exposure at alternative fill assumptions.
- **Control register:** missing keys, mismatch severity, record count, owner, age, action and closure.

## External filing safeguards
CBUAE information needs, scope and regulatory templates are dynamic. An institution's authorized compliance and regulatory-reporting officers must determine actual filing requirements; this independent case must never be presented as a CBUAE-compliant submission engine.
