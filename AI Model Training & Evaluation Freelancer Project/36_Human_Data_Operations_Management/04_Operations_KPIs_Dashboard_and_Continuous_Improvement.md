# 04 | Data-ops KPIs, reporting and workflow improvement

## Operational scorecard
| KPI | Definition | How to interpret |
| --- | --- | --- |
| Items collected | Count unique valid task IDs from authorized input | Source suitability and coverage still need checks |
| Annotation completeness | Annotated case-reviewer pairs / expected pairs | Capacity/assignment gap |
| Inter-rater agreement | Same A/B labels / doubly-labelled cases | Calibration indicator |
| Cohen's kappa | Chance-adjusted class agreement | Not a substitute for adjudication |
| Reviewer gold accuracy | Reviewer labels equal to independent gold / gold-covered tasks | Requires credible source of truth |
| Escalation / disagreement | Tasks with disagreeing labels / dual-labeled tasks | Review workload and instruction gaps |
| Cases reviewed / day | Total completed items / observed working days | Include actual staffing hours for fair productivity |
| Median processing minutes | Median time from assignment to annotation completion | Better than mean alone for skewed queues |
| Rework rate | Rework-flagged tasks / all unique tasks | Avoid double counting reopened cases |
| Accepted batch % | Released, fully approved records / records in batch | Policy controls, not model training performance |

## Sample dashboard storyboard
1. Top: tasks collected, completeness, agreement, kappa and release state.
2. Middle: queue distribution and error/confusion matrix.
3. Bottom: trend by day, backlog/stale items, rework time and corrective actions.
4. Executive callout: "Do we scale, repair guidelines or pause?" with reasons.

## Python reporting
Run src/audit_annotations.py for label/QA and src/report_ops.py for productivity/KPIs. Raw CSV stays unchanged. Reports use only pseudonymous case IDs and fictional categories.

## Example improvement backlog
| Finding | Recommended change | Owner | Verification |
| --- | --- | --- | --- |
| other vs policy disagreement | Add examples of vague/unspecified requests | Annotation lead | Recalibrate fresh sample |
| payroll vs benefits boundary | Clarify allowances vs coverage with mixed-intent examples | HR SME | Reviewer accuracy on edge cases |
| Rework queues grow | Monitor mismatch per agent and pair with targeted coaching | Operations manager | Lower rework without lower quality |
| Missing data provenance | Add mandatory source/consent/version fields | Data governance | 100% approved source audit |
| Excess manual reporting | Automate validation and metric aggregation | Data engineer | Same checked figures, less rekeying |

## Business storytelling
Translate "agreement is below our pilot threshold" into a defensible recommendation: **pause scale-up, refine rules and re-run an independent calibration sample**. Never claim actual productivity improvement from synthetic metrics.
