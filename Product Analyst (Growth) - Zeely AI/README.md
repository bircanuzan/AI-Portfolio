# Product Analyst (Growth) — Growth Funnel & Monetization Analytics

**Target competency:** acquisition→activation→purchase→monetization analytics, B2C/subscription segmentation, A/B testing, retention, LTV and ARPU, self-service KPI monitoring, and experiment decision standards.

**Portfolio status:** reproducible analytics blueprint with synthetic data and links to existing analytics portfolio. This is **not** a claim of work for Zeely, a live growth product, verified uplift, or experience with a named real B2C subscription employer.

## Problem
Growth teams need consistent metric definitions and actionable evidence about where web visitors convert, why customer segments differ, whether experiments improve business outcomes, and how pricing changes affect revenue, churn and lifetime value.

## Project design
1. Define event taxonomy and deduplicate funnel events from acquisition through purchase and retention.
2. Build an auditable SQL metric layer: visitors, activated users, first purchases, paid conversion, ARPU, retention and subscription revenue.
3. Segment cohorts by acquisition channel, signup month and product behavior; distinguish selection bias from causal test outcomes.
4. Design randomized A/B tests with primary metric, guardrails, sample-size/power and pre-registration; inspect confidence intervals and practical significance.
5. Analyze subscription economics using observed cohort revenue and explicit LTV assumptions; track refunds and failed payments.
6. Publish KPI definitions, dashboard/alert specifications, data-quality gates and stakeholder decision notes.

## Existing portfolio evidence
- [People Analytics & HR Data: validated metrics, SQL/DAX templates, scenario analytics, dashboards](../People%20Analytics%20%26%20HR%20Data/README.md)
- [Model evaluation & experiment tracking](../Model%20evaluation%20and%20experiment%20tracking/README.md)

## Core technology and methods
SQL, Python, pandas, Power BI, Tableau, Excel/Power Query; descriptive statistics, proportion tests, cohort/segmentation analysis, A/B experiment interpretation, anomaly thresholds, and metric contract validation.

## Deliverables / acceptance
- [Metric dictionary and experiment framework](GROWTH_METRICS_AND_EXPERIMENTS.md)
- Clear denominator/source definitions; reproducible cohort queries; no fabricated growth uplift or company access.

**Scope boundary:** Zeely-specific datasets, production web events and subscription transactions were not accessed. Any thresholds or examples are illustrative only.
