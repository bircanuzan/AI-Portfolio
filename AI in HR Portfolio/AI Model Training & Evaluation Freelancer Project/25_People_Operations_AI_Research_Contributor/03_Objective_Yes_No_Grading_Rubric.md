# Twelve atomic yes/no scoring criteria (12 points)

A reviewer awards **one point only for Yes** on each independently observable criterion. No partial points, subjective writing quality bonuses or "almost right" decisions. The evaluator must open the completed workbook and examine formulas/outputs.

| # | Binary criterion | Example verification |
|---|---|---|
| 1 | Every department has all six periods and no missing month | 24 dept-month model rows |
| 2 | Only Approved hire rows add FTE | Operations proposed January hire excluded |
| 3 | Approved exits reduce FTE beginning in correct month | Operations Dec -1 FTE |
| 4 | Each new month's opening FTE equals prior month's closing FTE | Same dept chain |
| 5 | Each row's closing FTE equals opening + approved hires - approved exits | Exact formula equality |
| 6 | Salary baseline multiplies roster full-time salary by FTE | Operations half-time role correctly treated |
| 7 | Approved hire and exit salary changes occur in the proper months | No premature cost changes |
| 8 | Annual compensation converts to monthly via /12 consistently | Full-month assumption |
| 9 | Loaded cost uses a reference to the benefits burden assumption, not hard-coded rate | 22% can be changed centrally |
| 10 | Budget variance = cap minus loaded cost and negative entries are flagged | Operations Nov = -6,195 |
| 11 | Exact-match band review identifies salary outside grade min/max | Compare each role to Comp_Bands |
| 12 | A genuine pivot table summarizes relevant FTE/payroll by department/month | Refresh and inspect totals |

**Passing threshold for portfolio demonstration:** 12/12 for a fully correct gold solution. If using this rubric to grade a model output, do not assign a point for a feature merely promised in the prose but missing in the Excel file.

**Caveat:** The provided GOLD workbook covers core calculations but does **not** implement a genuine PivotTable or salary-band exception audit; therefore it is **not a 12/12 completion**. Those are deliberate extension tasks. The complete rubric is a design template, not a claim of a reviewer-approved task.
