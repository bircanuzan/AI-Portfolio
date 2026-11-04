# Measurement system: baseline, KPI definitions and ROI

## Proposed leadership dashboard — no actual norbloc measurements
| KPI | Definition | Target / decision rule |
|---|---|---|
| Technical weekly active adoption | unique eligible users completing >=1 approved AI-assisted task in previous 7 days / eligible technical staff with access | **>=80% target**, with quality and risk gates |
| Sustained-use rate | unique eligible users with >=3 approved tasks per week / eligible staff | track trend, target after baseline |
| Accepted engineering cycle time | median elapsed time per complexity-matched accepted PR | positive experiment delta without quality loss |
| QA effectiveness | defects detected, meaningful coverage / mutation score, escaped defects | improve coverage, no severity regression |
| Verified RFP accuracy | reviewer-confirmed factual statements / total factual statements | pre-set high threshold with legal |
| KYB extraction accuracy | field- and document-level precision/recall vs independently labeled data | thresholds by field risk and cohort |
| Human review load | handling minutes + rework minutes per case | should improve without increased errors |
| AI unit cost | all-in licensing+API+evaluation+security costs / accepted task | monitored and budgeted |
| Governed coverage | approved AI workflows with owner, risk tier, evaluation, rollback / deployed AI workflows | 100% |
| Client outcomes | consented pilot satisfaction, exception burden, onboarding turnaround | establish baseline |

## Benefit calculation
```text
hours_released = observed_net_minutes_saved_per_task * monthly_task_volume / 60
gross_capacity_value = hours_released * fully_loaded_hourly_cost * realization_factor
monthly_net_value = gross_capacity_value - licenses - api - review_overhead
                    - support - amortized_implementation - security_controls
ROI = monthly_net_value / total_monthly_cost
payback_months = one_time_implementation / positive_monthly_net_benefit
```
**Warning:** capacity value is *not cash savings* unless resourcing or revenue conversion is proven.

## Worked illustration (hypothetical)
- 800 eligible monthly tasks; **4 net minutes saved** per task including human review.
- 53.3 hours released; AED 180/hour fully loaded; realization factor 60%.
- Gross capacity value approximately **AED 5,760/month**.
- Incremental recurring costs: AED 2,400/month; illustrative benefit **AED 3,360/month**.
- One-time integration/training: AED 12,000 => **~3.6-month simple payback** if benefits hold.
These figures are **scenario inputs**, not measured company performance or a forecast.

## Experiment hygiene
Timebox pilots; collect sample sizes, complexity, control/AI allocation, confidence ranges and error severity. Record adverse or inconclusive results. Produce monthly executive one-pager with **stop / iterate / expand** decisions.

## Reporting template
`period | workstream | eligible | weekly_active | baseline_median | assisted_median | quality_guardrails | all_in_cost | evidence_id | decision | owner`
