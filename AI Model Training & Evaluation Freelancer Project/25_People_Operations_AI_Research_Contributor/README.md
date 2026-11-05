# Project 25 — People Operations AI Research Contributor

**Demonstration aligned to Aptura's People Operations AI Research Contributor job description.**

> **NON-SUBMISSION WARNING:** Aptura's onboarding work sample requires a task brief and compulsory input Excel workbook **authored independently without AI**. This repository and the downloadable demonstration workbooks were created with AI assistance. They are **portfolio examples only** and **must not** be passed off as your human-built onboarding task.

## In plain English
Can a model repair and extend an Excel workforce plan without overlooking approved hiring, departures, salary cost or compensation exceptions? This portfolio shows how an expert could define an auditable Excel problem, calculate a verified answer and write binary criteria for assessing AI outputs.

## Synthetic Excel evaluation scenario
A fictional four-department organization plans its workforce from **November 2026 through April 2027**. The data contain 18 roster records, five planned hires (four approved and one not), two approved exits, salary grades/bands, benefits-burden assumptions and monthly departmental budget caps.

### Task sequence
1. **Extend an existing headcount model:** month-by-month FTE opening + approved hires - approved exits = closing. Proposed/unapproved requisitions are excluded.
2. **Repair and complete compensation formulas:** sum FTE-adjusted salaries, apply only approved hire/exit changes from their effective month, calculate monthly cash cost and a separate benefit burden.
3. **Build a brief-driven analytical view:** verify salary-band exceptions, report department/month trends using a pivot table and conditional formats, and identify budget overruns.
4. **Evaluate AI output:** apply clear gold metrics and 12 atomic yes/no conditions. Distinguish formula correctness from formatting quality and avoid ambiguous inputs.

## Files
- [Task brief and data definitions](01_Excel_Benchmark_Task_Brief.md)
- [Correct calculations and source reconciliation](02_Gold_Answer_and_Model_Logic.md)
- [12 binary grading criteria](03_Objective_Yes_No_Grading_Rubric.md)
- [Known failure modes, quality gates and human review](04_Error_Cases_and_Eval_Governance.md)
- [Example input CSVs](data/) for review and re-use in **non-Aptura** exercises
- [Python headcount and compensation oracle](src/gold_oracle.py) and [test suite](tests/test_gold_oracle.py) for independent verification
- **Two real Excel files** are provided as downloadable conversation artifacts: one INPUT model to complete and one GOLD solution with formulas. They are *AI-assisted demonstration outputs* and are not human-authored Aptura submissions.

**[Advanced Excel implementation and grader checks](05_Advanced_Excel_Modelling_and_Pivot_Test_Design.md)** — named ranges, multi-criteria XLOOKUP, SUMIFS, real pivot-table specifications and conditional-format rule design. This is an AI-assisted teaching artefact and does not claim those objects exist in the prior sample workbooks.

## Excel techniques mapped to the job
Cross-sheet SUMIFS, FTE-weighted salary formulas, multi-criteria month/department lookups, salary band checks, pivot-ready normalized data, conditional formatting, controlled assumptions, payroll/benefits cost projections, model completion and error testing. A **true Excel PivotTable** and **named ranges** are identified as an additional hands-on requirement, not claimed as implemented in this repository's example workbook.

## Run tests
Python 3.10+: `python src/gold_oracle.py` then `python -m unittest discover -s tests -v`. Standard library only. This runs a deterministic oracle from sanitized synthetic data; it does **not** grade arbitrary free-form AI outputs.

## Ethical use
To apply to Aptura, create a *new* scenario **yourself** from permitted, independently sanitized or public source data, build the actual Excel workbook unaided, write your own instructions and submit only original, human-built content. This portfolio sample is for interview discussion, not task submission.
