# Executive scenario review — synthetic, not an HR staffing recommendation

**Illustrative workforce-planning decision**: Would an invented employer achieve a hypothetical closing headcount of 220 given a planned 7 hires/month and alternative exit-rate multipliers?

## Numerical example generated from fictional monthly history
- Final month in the independent history: **2026-06**, invented closing workforce **196**.
- Six-month retrospective holdout: `mean3` MAE 1.2; `last` MAE 1.3; selection `mean3` on this one synthetic trajectory.
- These scores evaluate a teaching fixture, **not** predictive accuracy on a real employer.

| Exit sensitivity case | Exit multiplier | Six-month ending headcount | Gap to fictional 220 target | Capacity @ 0.92 assumption |
|---|---:|---:|---:|---:|
| baseline | 1.00 | 190 | 30 | 174.8 |
| retention_hypothesis | 0.85 | 196 | 24 | 180.3 |
| stress | 1.20 | 178 | 42 | 163.8 |

## Decision interpretation
- **What the analysis supports:** explicit exploration of workforce headcount arithmetic, which assumptions are consequential, and a traceable handoff to HR / Finance.
- **What it does not support:** declaring a retention programme caused lower turnover, recommending layoffs, declaring that 220 is an optimal target, or predicting an identifiable person's resignation.
- **Approval status:** NOT APPROVED; scenarios are teaching hypotheses, not an employer workforce plan.

## Required human review register
| Review | Owner | Condition before action |
|---|---|---|
| Monthly HRIS data and period definition | HRIS + People Analytics | Dated event history and reconciled denominators |
| Skill mix and redeployment | Workforce Planning + Talent | Role/skill capacity, not just raw headcount |
| Hires, vacancy lead times and financial plan | Talent Acquisition + Finance | Approved hiring feasibility and cost assumptions |
| Employee impact, fairness, privacy | HR Legal / Employee Relations | Protected-group assessment without disclosure |
| Final scenario selection | CHRO and business executives | Document assumptions, uncertainty, dissent and follow-up cadence |

This is an independent **synthetic** executive brief, not advice to make specific employment decisions.
