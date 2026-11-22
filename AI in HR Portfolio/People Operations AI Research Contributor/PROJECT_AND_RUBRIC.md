# Synthetic HR Headcount + Compensation Excel Evaluation Case

## Fictional client brief
A GCC shared-services group needs a Q4 2026 workforce model for six roles across HR, Technology and Operations. It must reconcile hires, exits, closing headcount, loaded monthly compensation and budgets. A benchmark evaluator checks whether AI can extend, repair and build such workbooks without silent errors.

## Excel workbook specification
**Sheets:** Read Me; Role_Master (roles/grades/salary bands); Monthly_Movements (role/month hires and exits); Headcount_Plan; Compensation_Forecast; Department_Budget; Pivot_Review; QA_Exceptions.

**Source:** data/scenario.json is deliberately fictional. Benefits load 24%; currency AED; monthly cost periods. No individual employee records.

**Formula patterns:**
- Named range Benefits_Load = 24%; Salary_Bands = Role_Master min/max source.
- Hires: `=SUMIFS(Movements[Hires],Movements[Role_ID],[@Role_ID],Movements[Month],[@Month])`
- Exits: `=SUMIFS(Movements[Exits],Movements[Role_ID],[@Role_ID],Movements[Month],[@Month])`
- Closing HC: `=[@Opening_HC]+[@Hires]-[@Exits]`
- Opening HC: first month from Role_Master, later month from *previous month closing for same Role_ID* (guarded two-criteria XLOOKUP / INDEX-MATCH).
- Monthly base cost: `=[@Closing_HC]*[@Salary_AED]`
- Monthly loaded cost: `=[@Base_Cost_AED]*(1+Benefits_Load)`
- Favorable budget variance: `=[@Budget_AED]-[@Loaded_Cost_AED]`.
- PivotTable rows Department, columns Month, values Sum Closing_HC and Sum Loaded_Cost_AED.
- Conditional formatting: negative HC red, salary out of band red, budget-minus-cost negative amber.

**Three tasks:** extend Q4 to new period; repair wrong role-month lookups and compensation formulas; build the complete model and explain exception checks from a new brief.

## Twelve binary yes/no criteria
| ID | Pass only if | Severity | Tested by code? |
|---|---|---|---|
| POP-01 | Exactly 18 unique role-month records | Critical | Yes |
| POP-02 | Every valid source role and month appears exactly once | Critical | Yes |
| POP-03 | Opening headcount carries from preceding month / initial source | Critical | Yes |
| POP-04 | Hires and exits match source movements | Critical | Yes |
| POP-05 | Closing headcount equals opening + hires − exits and is nonnegative | Critical | Yes |
| POP-06 | Salaries remain within disclosed role band | Critical | Yes |
| POP-07 | Monthly base and 24% benefits-loaded costs are correct to AED 0.01 | Major | Yes |
| POP-08 | Department/month totals reconcile to detailed rows | Critical | Yes |
| POP-09 | Budget-minus-cost monthly variance is accurate | Major | Yes |
| POP-10 | Excel named ranges and multi-criteria lookups exist and work | Major | Human Excel inspection |
| POP-11 | PivotTable reconciles, conditional formatting flags errors | Major | Human Excel inspection |
| POP-12 | Workbook documents source, units, assumptions and no private data | Major | Human Excel inspection |

Nine objective reference checks can be tested in the runnable code. POP-10 through POP-12 are **not evaluated** without a human reviewing an actual Excel workbook; never mark them passed from a JSON export.

## Governance, process and outcomes
Use synthetic data only; never authorize hiring, pay, grade or individual staff actions. The model is a simulated reference answer and rubric prototype, not a live AI model test. An output that looks correct does not establish the Excel formula/pivot quality without independent workbook inspection.

**Aptura assessment restriction:** For the real onboarding, write a fresh original brief and create workbook inputs personally **without AI**. This public AI-assisted case must not be reused as that submission.
