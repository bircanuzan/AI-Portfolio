# AI Vendor Assurance — Do Not Accept 'Fair, Accurate and Transparent' Without Evidence

## Problem
AI recruitment vendors may use broad claims such as 'fair', 'accurate' or 'explainable'. None of these attributes has a context-free single score. The procurement team should request *specific claims, definitions, test populations, uncertainty, evidence and limits*.

| Vendor claim | Define before testing | Useful evidence | Caveat |
|---|---|---|---|
| Accuracy | On which decision/task, reference labels and time window? | Holdout benchmark, label quality, precision/recall, error categories, confidence intervals | A high overall accuracy can hide subgroup failures |
| Fairness | Which protected characteristics, adverse outcomes, jurisdictions and fairness definitions? | Lawful subgroup outcome analysis, selection-rate and error-rate comparisons, expert review | Fairness metrics may conflict; lawful data access and context matter |
| Transparency | Transparent to whom, about what, and at what stage? | User notices, model/data documentation, explanation availability, contestation routes | A dashboard is not proof of explanation faithfulness |
| Explainability | Are reasons faithful to actual drivers of each decision? | Feature-importance validation, reason-code tests, independent review | Plausible-sounding narratives may not explain model behaviour |
| Reliability | How stable under time, data and model changes? | Time-split tests, drift alarms, versioned test results, incident reports | One successful demo is not a guarantee |
| Security | How does the vendor handle injection, leakage and tool access? | Red-team summaries, penetration/security tests, IAM controls | Shared responsibility must be documented |
| Accountability | Who handles incidents, appeals and remediation? | Named owners, SLAs, audits, change-management logs | Independent assurance is different from vendor self-attestation |

## Practical buyer's evidence request
1. Intended use, contraindications and limitations.
2. Full model/version and material-change notification commitments.
3. Dataset provenance, population coverage and annotation quality.
4. Pre/post-deployment evaluation protocol with disaggregated results as legally appropriate.
5. Statistical uncertainty, error severity and escalation criteria.
6. Third-party audit scope (who audited, when, which version, which population).
7. Procedures for contested decisions and human review.
8. Security/privacy assessment and retention or deletion commitments.
9. Operational dashboards and historical incident/change logs.
10. Right to re-evaluate the vendor when models, prompts or datasets change.

## What this project actually proves
- It can **measure whether answers cite the active approved source version**, and whether the sample answers match their expected synthetic references.
- It can **identify missing evidence** and recommend a HOLD for defined critical failures.
- It **cannot determine demographic fairness**, real-world truth, bias, legal compliance, vendor safety or model validity from six hand-authored fixtures.

## Potential original concept: 'AI Assurance Debt'
Unresolved verification work accumulates when organisations add AI tools faster than they can document their purpose, source dependencies, controls, evidence and risk ownership. A proposed (not industry-standard) management view could show: percentage of untested material changes, aged critical exceptions, unknown vendor versions, overdue reviews, evidence gaps and open appeals. These are operational accountability signals, not a universal ethical score.
