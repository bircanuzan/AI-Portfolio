# People Operations AI Research Contributor

**HumanEvoX — independent, synthetic portfolio case**

[Job description — Aptura (global remote contract)](https://jobs.ashbyhq.com/aptura/8f4a50aa-5fbe-4337-951e-d8efdfd9e61f)

## Project — Q4 People Operations Excel Evaluation Lab

**Client requirement (fictional):** Reconstruct an October–December workforce plan across 6 synthetic role families in Human Resources, Technology and Operations. Extend a headcount model, repair incorrectly calculated salary cost and roll-forward formulas, compare to monthly department budgets, identify errors in AI-produced results and construct a precise yes/no scoring rubric.

**Methods / HR skills:** workforce planning; headcount bridge (opening + hires − exits); grade and compensation band checks; monthly payroll; benefits-loaded costs; budgets/variance; HR analytics; structured quality assurance; source reconciliation; model evaluation.

**Required Excel skills from JD:** named ranges, multi-criteria SUMIFS/XLOOKUP, pivot tables, conditional formatting, fixing broken models, building from a brief and extending existing plans. The Excel workbook *design* is documented in [PROJECT_AND_RUBRIC.md](PROJECT_AND_RUBRIC.md); the working Python example checks numerical accuracy, not actual PivotTable behavior.

**Implemented tools:** Python 3, Decimal, JSON, unittest, GitHub version control and GitHub Actions. The example includes a synthetic workforce dataset, reference calculator, binary rubric grader and regression tests.

## Files
- [JD-specific skills and AI technology](JD_SKILLS_TECH.md)
- [Case study, Excel worksheet design and evaluation rubric](PROJECT_AND_RUBRIC.md)
- [Synthetic people operations scenario](data/scenario.json)
- [Deterministic HR reference model and grader](src/headcount_eval.py)
- [Regression tests](tests/test_headcount_eval.py)

## Run
From repo root:

    python "AI in HR Portfolio/People Operations AI Research Contributor/src/headcount_eval.py"
    python -m unittest discover -s "AI in HR Portfolio/People Operations AI Research Contributor/tests" -v

**Integrity boundary:** This is a public AI-assisted portfolio example, not an Aptura client assignment, a live LLM evaluation, a production HR system, a measured customer result or real employee information.

**Crucial:** Aptura's onboarding explicitly requires task briefs and source workbooks to be **human-created without AI**. Do NOT submit this AI-assisted example as the required Aptura screening task. Prepare a separate original, human-built task and workbook if pursuing that application.
