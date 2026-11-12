# Workforce planning forecast / scenario model card

**Additive enhancement to the existing Project 54, not a new standalone project.**

## Critical separation
- Existing Project 54: 200 fictional employees, single **Q3 2026** fixed-cohort attrition description (44 / 200). It cannot support time-series forecasting.
- Additional independent fixture: [24 synthetic monthly aggregate workforce records](data/synthetic_monthly_workforce.csv), July 2024–June 2026. **Entire series is invented** to exercise reproducible forecasting methods; it is NOT derived from the 200-person Q3 cohort or Project 11's 500 employee records.
- **Never join the three populations or describe any forecast as a prediction about the 200 workers.**

## Prediction target and model card
**Target:** monthly count of workforce exits at *aggregate organisation level*. Not employee-specific attrition probability, no demographic inference and no individual retention scoring.

**Candidate forecasts:**
- Last-observed monthly exits (naïve benchmark).
- Mean of the last three observed monthly exits, rounded to an integer.
Both are simple deterministic time-series baselines, not fitted machine learning models and **not AI predictors**.

## Validation
- Validate chronological contiguous months; no missing periods, negative counts or broken start + hire − exit = end balances.
- Retrospective **expanding-origin** holdout of final six monthly points. Prediction for each held-out point uses **only earlier actual observations**, never future rows.
- Compare methods on monthly exits mean absolute error (MAE), disclose the small holdout and synthetic provenance.
- Pick smaller MAE; deterministic alphabetical tie-breaker. Refit using all fictional history before 6-month recursive hypothetical projection.
- Do not interpret low synthetic MAE as externally validated forecasting accuracy.
- No protected attributes, personal records, compensation, health information or individual actions.

## Scenario levers and assumptions
- Planned hires fixed at **7 per month**.
- Exit multipliers: 1.00 baseline, 0.85 illustrative retention improvement, 1.20 stress.
- Six-month horizon, hypothetical target **220** employees, availability capacity factor **0.92** FTE/employee.
- Projection uses *rounded monthly exits* and enforces nonnegative workforce count and count balance.
- The 0.85 multiplier is **an assumption**, not an estimated intervention effect. The capacity factor is not measured.
- No uncertainty interval: only a sensitivity band of assumed exit multipliers; **not** a statistical confidence interval.

## Responsible decision constraints
1. No automated hire, dismissal, layoff, payroll, promotion or individual outreach based on scenarios.
2. No individual attrition-risk rankings; human HRBPs should evaluate actual workforce context.
3. A real deployment requires verified dated HRIS event history, data definitions, source reconciliation and country-specific privacy/legal review.
4. Real validation needs multiple time origins, holdout periods, relevant seasonal/market shocks, drift tests, error by segment (where reporting protects privacy), confidence/calibration checks as applicable and Finance signoff.
5. Fairness and labour impacts: assess which groups or roles might bear the costs of different capacity choices; never infer protected traits from incomplete data.
6. Decision-makers must record forecast uncertainty, costs, skill mix, vacancy capacity, interventions, employee voice and human review.

## Reproducible commands
```bash
python src/workforce_scenario_forecast.py --out evidence/forecast_scenario_synthetic.json
python -m unittest discover -s tests -v
```

The source code is Python standard-library. [Executive scorecard](../52_HR_People_Analytics_Research_Dashboard_Library/workforce_intelligence_scorecard.html) embeds the committed sample output; refresh embedded data if source or model changes.

**Capability claim:** reproducible synthetic rolling-origin model-comparison and scenario code. **Not claimed:** production predictive ML, calibrated individual attrition prediction, business intervention causal effect or real workforce forecast.
