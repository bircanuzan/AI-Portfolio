# Excel workforce planning benchmark — sample task brief

**Audience:** People Operations analyst working with an inherited, partially completed Excel workbook.
**Data:** entirely fictional; not sourced from a real employee or employer.
**Date:** October 2026 baseline; planning horizon November 2026 to April 2027.

## Three tasks for an evaluator
### A. Extend monthly headcount
Given a current employee roster and separate hiring/exits worksheets, calculate opening, authorized additions, authorized leavers and closing full-time equivalents (FTE) for four departments and six periods. Dates in YYYY-MM order represent changes effective at the beginning of that month. A proposed/unapproved hire **must not** contribute to plan. Headcount must reconcile month-to-month.

### B. Fix the payroll model
Starting from the same roster, calculate FTE-adjusted annual base pay and monthly base compensation. Approved hires and exits change monthly compensation beginning in their respective effective month; the model does not prorate within a month. Benefits burden is 22% of base payroll, from the assumptions tab. Monthly budget variance = approved monthly cap - loaded payroll. Negative variance should be clearly highlighted. The INPUT workbook intentionally leaves the pay/burden/cap/variance output formulas blank; they are tasks, not corrupted file references.

### C. Build from a brief
Produce a department/month pivot summary for closing FTE, loaded payroll and budget variance. Test the roster's salary entries against grade min/max thresholds, flag exceptions, and add a brief explanation of likely business implications. Protect personally sensitive data by using the fictional IDs and no actual salary records.

## Expected work product
An amended Excel model, traceable formulas, analyst note describing assumptions/exception risks, and the completed 12-part yes/no rubric. The task should be independently verified before grading any model output.

## Critical Excel checks
- SUMIFS based on department + effective month + Approved status.
- Lookup into salary bands using exact grade matching, not loose approximate grades.
- Separate FTE from headcount, monthly base from loaded compensation, and actual from proposed vacancies.
- Use assumptions cells for burden; no hard-coded formula constants.
- Numeric outputs and percentage/currency formats must remain consistent.
- PivotTable grouped by month and department should recalc after roster changes.
- Keep all source rows intact with distinct employee/requisition keys.

**No real employee data or personally identifiable information.**
