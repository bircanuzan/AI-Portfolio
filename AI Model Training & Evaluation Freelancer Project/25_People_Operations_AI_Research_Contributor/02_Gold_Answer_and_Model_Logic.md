# Verified gold answer and explicit model assumptions

The calculation uses **fictional data** and a full-month planning convention. All employees in the roster count as active as of October 2026.

## Approved workforce transitions
- Operations: opening 5.5 FTE; +1.0 approved November hire; -1.0 approved December exit; a proposed January hire is ignored.
- Analytics: opening 4.0 FTE; +1.0 approved December hire.
- Engineering: opening 5.0 FTE; +1.0 approved January hire.
- Sales: opening 3.0 FTE; -1.0 approved February exit; +1.0 approved March hire.

## Key reference calculations
| Check | Gold result |
|---|---:|
| Total baseline opening FTE for Nov 2026 | 17.5 |
| Total November approved additions | 1.0 |
| Total Nov 2026 closing FTE | 18.5 |
| Operations Nov base payroll | AED 74,750.00 |
| Operations Nov loaded payroll (22% burden) | AED 91,195.00 |
| Operations Nov budget cap | AED 85,000.00 |
| Operations Nov variance | **-AED 6,195.00** |
| Operations Dec closing FTE | 5.5 |
| Operations Dec base payroll | AED 62,916.67 |
| Operations Dec loaded payroll | AED 76,758.33 |

## Formulas — examples
The row-numbered solution workbook contains:
- **Opening_FTE**: initial `SUMIF(Roster[Department],Dept,Roster[FTE])`; subsequent months reference prior closing FTE for the same department.
- **Approved_Hires_FTE**: SUMIFS by department, effective month and approval = Approved.
- **Approved_Exits_FTE**: SUMIFS by department, effective month and approval = Approved.
- **Closing_FTE**: `Opening + Hires - Exits`.
- **Monthly_Base_AED**: (FTE-adjusted roster annual salaries + all approved hire salary through current month - all approved exit salary through current month) / 12.
- **Loaded_Cost_AED**: monthly base × (1 + Assumptions benefits-burden cell).
- **Variance_vs_Cap_AED**: monthly cap - loaded cost.

## Why "reasonable" AI solutions sometimes fail
Using full annual salaries while ignoring part-time FTE; counting unapproved hires; subtracting an exit twice; including an exit salary before its effective date; hardcoding benefits cost; reporting cap difference with reversed sign; reporting 18.0 employees instead of 17.5 FTE; pretending average compensation is equivalent to actual budget.

## Limits
This toy model omits bonus, variable pay, gratuity/end-of-service, statutory/local-law differences, raises, vacancies without budget, cost-center allocations and partial-month payroll. Any real model needs approved policy, verified source records and finance review.
