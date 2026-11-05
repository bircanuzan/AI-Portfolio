# Model evaluation quality gate and error taxonomy

## Task should be rejected or repaired if:
1. Data includes actual proprietary payroll records or personally identifying information.
2. Approval state on a hire/exit is unavailable or ambiguous.
3. Effective month conflicts across HR approvals without a documented precedence rule.
4. Salary band tables have duplicate grade keys or are absent.
5. Formula convention on mid-month joiners or variable pay is unspecified.
6. Ground truth cannot be independently reproduced by a reviewer.

## Common model failure types
- **Source confusion:** count proposed job requisitions as approved.
- **Formula logic:** incorrect criteria ranges in SUMIFS / incomplete fiscal month coverage.
- **Compensation:** treat 0.5 FTE as 1 FTE or double-count salary on exits.
- **Scenario:** silently apply annual merit assumptions when they are defined but not in scope.
- **Integrity:** alter underlying roster to make outputs easier.
- **Rendering:** pretty worksheet with wrong values or hard-coded instead of dynamic formulas.
- **Auditability:** produce numbers without reproducible source links.
- **Excel:** fake pivot output rather than a refreshable PivotTable.

## Review procedure
Two reviewers can score independently, flag disagreements by numbered criterion and adjudicate using source data and formula trace. Keep model version, submitted file hash, original task and score-sheet revision. Never conflate evaluator performance with a legal payroll approval.

## Aptura submission restriction
The job description prohibits AI-generated briefs and input workbooks for the onboarding exercise. This project's contents were created with AI assistance and therefore **cannot be submitted as independent human-built work**. The project serves only as a portfolio illustration of the relevant Excel/evaluation concepts.
