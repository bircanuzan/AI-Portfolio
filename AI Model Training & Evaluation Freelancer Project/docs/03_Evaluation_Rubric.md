# Human Evaluation Rubric

Six dimensions total **100 points**. Score each from 0–4: 0 absent/incorrect; 1 weak; 2 partial; 3 strong; 4 complete and independently defensible.

| Dimension (CSV field) | Weight | Anchor for 4/4 |
| --- | ---: | --- |
| Problem structuring (`structure`) | 20 | Clear decision, MECE-style issue tree, well-argued options and trade-offs |
| Evidence traceability (`evidence`) | 20 | Every material claim linked to provided input, with uncertainty and counterevidence |
| Quantitative integrity (`quantitative`) | 20 | Arithmetic independently checks out, formulas auditable, units/scenarios reconciled |
| Deliverable craft (`craft`) | 15 | Executive-clear, concise and internally consistent; formats and labels support review |
| Implementation readiness (`implementation`) | 15 | Owners, dependencies, success metrics, risks, decision gates and practical milestones |
| Governance & controls (`governance`) | 10 | Confidentiality, human approvals, provenance, limitations and appropriate escalation |

**Composite** = Σ(weight × dimension_grade / 4), rounded to two decimals. For tasks without heavy numeric work, evaluate internal data logic and appropriate handling of unavailable figures; do **not** simply award a high quantitative score.

**Human decision thresholds (illustrative):**
- ≥85 and no critical issue: exemplar / ready for expert review
- 70–84.99 and no critical issue: revise minor issues
- 50–69.99 and no critical issue: substantive rework
- below 50 or **critical defect**: fail review

## Critical defects
`fabricated_evidence`, `material_formula_error`, `wrong_units`, `unapproved_disclosure`, `unsupported_decision`, `unowned_control`.

A critical defect forces **FAIL / max published score 49**, regardless of the raw total. **This is a project rule, not a validated industry standard.** An evaluator must document why the defect is material.

## Calibration
1. Two reviewers independently score at least 20 varied outputs before operational use (future proposed validation).
2. Compare dimension-level differences and discuss discrepancies ≥2 points.
3. Measure agreement with weighted kappa or ICC; document tie-breaks.
4. Run blinded repeat grading after revisions.
5. Retain source snapshots and task versions to avoid leakage.

The bundled CSV is an **illustrative, authored rating sheet**, not a dataset of independently evaluated third-party AI responses.

