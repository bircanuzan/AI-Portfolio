# People Analytics & HR Data

**Four distinct, existing projects.** This category now demonstrates a connected and responsible people-intelligence workflow, with separate ownership of executive strategy, data assurance, visualization and workforce scenario analysis.

## Start with the complete workflow
**[Trusted data → analysis → workforce insights → human-reviewed decisions](WORKFORCE_INTELLIGENCE_PIPELINE.md)** documents source lineage, exact steps, technical execution, and the essential warning against joining unrelated synthetic populations.

| Project | Dedicated professional capability | New, nonduplicative enhancement |
|---|---|---|
| [03 — People Analytics & AI](03_People_Analytics_AI/) | Executive questions, people strategy, decisions and governance | [Decision register and responsible analytics charter](03_People_Analytics_AI/DECISION_GOVERNANCE_AND_PEOPLE_INTELLIGENCE.md) |
| [11 — Data Analytics for AI in HR](11_Data_Analytics_for_AI_in_HR/) | Trusted HR datasets, metric definitions and descriptive calculation | [Standard-library source validation and metric contract](11_Data_Analytics_for_AI_in_HR/DATA_CONTRACT_AND_QUALITY_GATES.md), [Python script](11_Data_Analytics_for_AI_in_HR/src/trusted_workforce_metrics.py), [tests](11_Data_Analytics_for_AI_in_HR/tests/) and [synthetic aggregate snapshot](11_Data_Analytics_for_AI_in_HR/evidence/trusted_workforce_metrics.json) |
| [52 — HR & People Analytics Dashboard Library](52_HR_People_Analytics_Research_Dashboard_Library/) | Visual insight and executive communication, original 60 concepts | [Executive scorecard HTML](52_HR_People_Analytics_Research_Dashboard_Library/workforce_intelligence_scorecard.html) with [source lineage / release gates](52_HR_People_Analytics_Research_Dashboard_Library/EXECUTIVE_MEASUREMENT_AND_LINEAGE_GATE.md); existing 60 dashboards unchanged |
| [54 — Attrition Analysis / Workforce Scenario Methods](54_Attrition_Analysis_200_Employee_Synthetic_Case/) | Original 200-person cohort description, plus distinct **aggregate** workforce scenarios and time-series benchmarking | [Model card](54_Attrition_Analysis_200_Employee_Synthetic_Case/FORECAST_MODEL_CARD_AND_VALIDATION.md), [24-month fictional history](54_Attrition_Analysis_200_Employee_Synthetic_Case/data/synthetic_monthly_workforce.csv), [forecast code](54_Attrition_Analysis_200_Employee_Synthetic_Case/src/workforce_scenario_forecast.py), [tests](54_Attrition_Analysis_200_Employee_Synthetic_Case/tests/) and [executive decision review](54_Attrition_Analysis_200_Employee_Synthetic_Case/DECISION_SIMULATION_REVIEW.md) |

## Methods and evidence boundary
**Actually authored:** SQL/DAX templates from the original work, Python descriptive analytics, new stdlib data checks, chronological holdout model comparison, assumptions-based workforce projections, local tests, JSON snapshots, SVG concepts and interactive HTML.

**Not claimed:** trained production predictive AI, individual employee attrition prediction, causal effect of retention interventions, true employer workforce history, Power BI tenant, real client data, paid deployment, or measured ROI.

**Critical distinction:** Project 11's 500 synthetic employee rows, Project 54's original 200 fixed-cohort employee rows and Project 54's new 24 invented monthly records are **three unrelated populations**. No cross-population statistical inference or joins.

[Repository home](../README.md) · [Detailed overview](../PORTFOLIO_DETAILED_OVERVIEW.md)
