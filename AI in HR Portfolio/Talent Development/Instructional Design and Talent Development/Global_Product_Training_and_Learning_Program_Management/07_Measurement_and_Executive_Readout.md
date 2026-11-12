# 07 | Evidence, KPI definitions and executive readout

## Principles
Use leading and lagging measures separately. **Participation is not competency**. **Synthetic pilot data is not customer impact.** No conversion lift, shortened sales cycle or other business outcomes are claimed without a valid comparison group and observed data.

| Metric | Definition | Proposed goal | Caveats |
|---|---|---|---|
| Completion rate | Completed learners / assigned learners | >= 85% by day 21 | Requires LMS assignment window; initial synthetic file has no real dates |
| Knowledge/performance pass rate | Learners at >=20/25, no critical errors / assessed learners | >= 80% | Rubric is illustrative; valid only after calibrated assessment |
| Critical claims errors | Number of observed unsafe promises | 0 for qualified learners | A single severe error blocks individual passing |
| Manager follow-up coverage | Learners with a recorded manager observation / assigned learners | >= 75% by day 45 | Observations must be sampled and quality reviewed |
| Content release compliance | Published assets with approved version, SME owner, review date / published assets | >= 90% | No real production assets included |
| Learning improvement | Average post-score - pre-score for matched learner IDs | To be established | Synthetic sample has no pre-score and cannot estimate uplift |

## Reproduce the hypothetical learner report
```bash
python src/learning_metrics.py data/synthetic_learning_results.csv
python -m unittest discover -s tests -v
```
No external packages or systems are needed. The CSV has fictional records only.

### Synthetic executive illustration (12 sample participants)
| KPI | Example calculation | Example result | Interpretation |
|---|---|---|---|
| Assigned | 12 records with assigned=1 | 12 | Artificial cohort size |
| Completed | 10 / 12 | 83.3% | Below proposed 85% target |
| Assessed | 10 records with numeric score | 10 | Completion alone does not imply competence |
| Passed | 7 / 10 assessed with score >=20 **and** 0 critical errors | 70.0% | Below proposed 80% target |
| Blocked by critical error | 1 learner | 1 | Must remediate and reassess |
| Manager observed | 6 / 12 assigned | 50.0% | Below proposed 75% target |

*All figures above are derived from an invented example file, not learner telemetry, actual launches or verified outcomes.*

## Hypothetical programme manager's steering recommendation
**HOLD broad scale-up:** Adjust role plays and objections, validate whether the unsafe claim came from content misunderstanding or product misinformation, add manager observation slots, remediate learners who did not pass, then repeat a small pilot before expanding. The project's judgement demonstration is in the quality of the gate decisions, **not** in a fictional success story.

### Evidence to request for a real programme
LMS enrolment/export, versioned assessment rubrics, rater calibration, approved product sources, regional manager observations, content QA release logs, quiz validity review, learner accessibility feedback, current role metrics and approved privacy policy.

### Causal discipline
Even if a real sales win-rate trend rises after training, don't attribute it to the course without examining seasonality, pipeline changes, customer demand, tenure, product changes and a credible counterfactual.
