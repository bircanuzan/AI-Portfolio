# 05 — Advanced Excel Modelling: Named Ranges, Multi-Criteria Lookup, Pivot Tables and Conditional Formatting

**Independent, AI-assisted portfolio enhancement. Not eligible as an Aptura human-authored onboarding workbook or task.**

## Three task types Aptura asks SMEs to create
1. **Extend existing workbook**: take a current headcount model to six months, maintaining a correct roll-forward for approved joins and exits.
2. **Fix a broken workbook**: find formula/lookup/formatting errors such as wrong row range in SUMIFS, inclusion of proposed hires, duplicate salary counting and reversed budget variance.
3. **Build from a brief**: produce a fully documented compensation/headcount model and refreshable pivot summary, with a gold answer and atomic binary scorecard.

## Advanced Excel design contract
| Capability | Example | What a grader should inspect |
|---|---|---|
| Named ranges | \`BenefitsBurden\` -> Assumptions!$B$3; \`ReportingMonth\` -> Summary!$B$3 | A legitimate workbook-level or scoped name exists and formulas reference it |
| Multi-criteria lookups | \`=XLOOKUP(1,(Rates[Grade]=F2)*(Rates[Country]=G2),Rates[AnnualMin],"MISSING",0)\` | Match both grade and country, exact match and explicit missing-value behavior |
| SUMIFS by month/approval | \`=SUMIFS(Hires[FTE],Hires[Department],$A2,Hires[Start_Month],$B2,Hires[Approval],"Approved")\` | Proposed hires are not counted; formula updates if source rows change |
| Compensation | \`=SUMPRODUCT((Roster[Dept]=A2)*Roster[AnnualBase]*Roster[FTE])/12\` | 0.5 FTE salary is not counted at full pay |
| PivotTable | Rows: Month, Department; Values: Closing_FTE (sum), Loaded_Cost (sum), Budget_Variance (sum) | A **real refreshable PivotTable object**, not manually pasted totals |
| Conditional formatting | Negative budget variance: \`=$K2<0\` red fill | Excel rule object present and updates after recalculation |
| Auditability | Unique employee/requisition IDs, separate source tables and exception flags | No edits to underlying roster to manipulate answers |

## Concrete yes/no evaluator tests
- Does the workbook define the \`BenefitsBurden\` named range and use it in the loaded-cost formula?
- Does the combined grade+country lookup match the correct band with exact-match semantics?
- Does a proposed recruit remain excluded from approved closing FTE and cost?
- Do monthly FTE and payroll values change after an approved hire is introduced?
- Is there an Excel PivotTable with a refreshable source and the three requested value fields?
- Is there a conditional-format object for negative budget variance, not merely static red cell formatting?

## Rubric integrity
**Do not automatically award any criterion.** The earlier portfolio GOLD workbook may contain basic SUMIFS, source tables and formatting but does not guarantee a refreshable PivotTable or named ranges. A criterion is satisfied only when a grader can actually inspect that feature inside an Excel file.

## Mandatory Aptura boundary
Aptura requires the onboarding **brief and input workbook to be human-authored without AI**. This guide and the accompanying demonstration workbooks **were AI-assisted**, so do not submit or represent them as your human-built assignment. You can create a *separate new exercise* personally after their walkthrough.
