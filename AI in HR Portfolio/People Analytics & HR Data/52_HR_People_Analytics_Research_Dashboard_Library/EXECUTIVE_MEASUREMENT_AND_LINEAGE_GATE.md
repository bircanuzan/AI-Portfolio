# Executive People Intelligence Scorecard | Measurement Release Contract

**Project 52's distinct role:** presentation, interpretation and quality gating. The original 60 dashboard research concepts remain unchanged. This example provides *one coherent CHRO decision view* powered by **two clearly separate synthetic aggregates**, not 60 more dashboards.

## Source traceability
| Panel | Source of numbers | Grain and limitation |
|---|---|---|
| Workforce snapshot and department exit flag shares | [Project 11 verified aggregate snapshot](../11_Data_Analytics_for_AI_in_HR/evidence/trusted_workforce_metrics.json) | 500 fictional employee rows; not valid actual employee turnover |
| Forecast comparison and workforce scenarios | [Project 54 independent aggregate history / result](../54_Attrition_Analysis_200_Employee_Synthetic_Case/evidence/forecast_scenario_synthetic.json) | 24 invented monthly records; not the 200-employee cohort or the Project 11 population |
| Decision framework | [Project 03](../03_People_Analytics_AI/DECISION_GOVERNANCE_AND_PEOPLE_INTELLIGENCE.md) | Decision owner and human approval; no actual sponsor approval |

## How to view
Download the self-contained [executive scorecard HTML](workforce_intelligence_scorecard.html) and open it in a browser. It includes **static embedded copies** of the versioned source JSON outputs, and can interactively explore a *hypothetical scenario* without transmitting data. If source data changes, the embedded fixtures need regeneration / reconciliation.

## Reporting gates
1. Show denominator, period and data source with every headline.
2. Do not compare 500-person employee-flag share to the unrelated 24-month monthly turnover history.
3. Suppress sample groups <10 and monitor complementary disclosure and cumulative privacy risks.
4. Label “sensitivity scenario”, not “95% confidence interval” or real prediction.
5. Show methodological limits and sources beside the numbers, including all excluded metrics.
6. Prevent individual-level inference, automated decisions and real HR actions.
7. An executive could approve *additional validation or piloting*, not take personnel action based on fictional scenarios.

## From metrics to action — decision framing
**Question:** Is workforce capacity at risk under alternative assumptions?

**Evidence:** cohort-specific descriptive counts, separate toy time series, documented backtest, sensitivity alternatives, and human review register.

**Proposed next step:** Verify true business definitions and obtain approved HRIS history, then validate the pipeline with a designated HR/Finance owner before making organisational recommendations.

**Evidence boundary:** HTML/SVG visuals and markdown are authored artifacts; not a live dashboard, Power BI deployment, employee data integration, validated predictive model, or achieved customer result.
