# Fairness and model-outcome review: genuine arithmetic on SYNTHETIC labels
**Scope:** 20 entirely fictional applicant records; Group A and B are artificial labels. No protected trait is guessed, no real candidate and no machine-learning system output was collected. The labels **model_selected** are invented solely for testing the audit calculator.

Run:
```bash
python fairness_audit.py synthetic_fairness_cases.csv
python -m unittest test_fairness_audit.py -v
```

## Calculated expected metrics
| Metric | Synthetic Group A | Synthetic Group B |
|---|---:|---:|
| Number of fictional records | 10 | 10 |
| Job-qualified (fictional evaluator label) | 7 | 7 |
| Selected by an **invented** scoring outcome | 7 | 4 |
| Selection rate (selected / 10) | 70% | 40% |
| True-positive rate (qualified selected / 7 qualified) | 85.7% | 57.1% |
| False-rejected qualified cases | 1 | 3 |

Absolute selection rate gap = **30 percentage points**; qualified-selection gap = **28.6 percentage points**.

**Interpretation:** the constructed group difference requires investigation of decision criteria, input distribution, sample sizes, data provenance and confounders before any deployment decision. This mini-dataset cannot establish statistical significance, causal discrimination, demographic fairness, or whether an organisation satisfies any law. It is deliberately small and artificial.

## Production fairness review design
1. Privacy/Legal establish lawful authority and purpose for any group-level analysis. Never guess demographics from names, images or proxies.
2. Freeze pre-registered business-relevant labels and intended use; check labelling bias and qualifications rubric.
3. Audit class balance and representativeness, stratification and confidence intervals, and conflicting fairness objectives.
4. Compare selection rates, group-specific true/false positive rates, stability and candidate complaint data with a sufficiently powered dataset.
5. Review raw erroneous cases with trained human assessors and document mitigation.
6. Re-test independent holdout data and monitor change after deployment.
7. Determine risk acceptance via board-approved contextual criteria, not a universal threshold (including the non-universal US 'four-fifths' heuristic).

**No technical fairness claim** is made for any real LLM, vendor, recruitment process or client.
