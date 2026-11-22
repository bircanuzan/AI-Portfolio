# AI Data Analytics — AI-Assisted Commercial & Usage Intelligence

**Project type:** Independent, reproducible portfolio demonstration using entirely synthetic telecom/eSIM data. **Not** a BNESIM client project, employment claim or production deployment.

## Business requirement
A global digital-connectivity business needs consistent commercial and usage reporting across geographies, acquisition channels and products; trustworthy KPIs; quick exception detection; and documentation that lets analysts extend the reporting workflow.

## Solution and methodology
1. **Requirements & KPI dictionary:** define revenue, gross profit, gross margin, average order value, order counts, data usage, return-order share and quality thresholds.
2. **Ingest & profile:** import synthetic CSV transactions; check schema, nulls, duplicates, invalid dates and numeric ranges.
3. **Transform & validate:** quarantine bad records, use deterministic Python/Decimal financial arithmetic; preserve exceptions for review.
4. **Analyse:** aggregate by geography, channel, product and reporting month; reconcile segment totals against company totals.
5. **Visualise:** expose machine-readable JSON and segment CSVs for Power BI/Tableau. Suggested pages: executive trends, region/channel profitability, demand/usage, data-quality drilldown.
6. **AI-assisted insight layer (proposed):** use LLM APIs / Azure AI Foundry to draft narrative insights *only from validated metrics*; use grounded prompts, schema-based output, regression tests, manual approval and explicit uncertainty. This repo does not claim an LLM API execution.
7. **Agent & workflow integration (design):** orchestrate scheduled runs using n8n / Make / Zapier / Power Automate, API/webhook triggers, anomaly flags, notifications and human sign-off before publication.
8. **Measure:** correctness of totals, share of quarantined records, dashboard freshness, reporting SLA, time-to-insight, cost per report and analyst-approved narrative accuracy.

## Skills and technology mapped to the AI Data Analytics internship

| Area | Technology / skills | What the project demonstrates |
|---|---|---|
| Analytics engineering | Python, CSV, Decimal, JSON, SQL | Profiling, cleansing, repeatable calculations, grouped aggregations |
| BI & visualisation | Power BI / DAX, Tableau, Excel, Power Query | Proposed dashboard model and governed KPI definitions; CSV export for implementation |
| AI/LLM | Azure AI Foundry, LLM APIs, prompt engineering, evaluation rubrics | Proposed grounded insight summarisation and quality checks; no falsely claimed live API calls |
| Automation & agents | n8n, Make, Zapier, Power Automate, REST/webhooks | Proposed extract-transform-validate-report-notify workflow and human-approval gate |
| Data quality & governance | duplicate handling, schema checks, anomaly alerts, lineage, exception queue | Transparent rejected-record audit trail and reconciled metrics |
| Business | commercial analytics, product/region segmentation, KPI reporting, stakeholder reporting | Reproducible management reporting outputs |

## Demonstration
Requirements: Python 3.10+; no external dependencies.

```bash
cd "AI Portfolio/AI Data Analytics"
python analytics_pipeline.py
python -m unittest discover -s tests -v
```

The script creates `output/metrics.json`, `output/quarantined_rows.csv`, `output/by_country.csv`, `output/by_channel.csv`, `output/by_product.csv`, `output/by_month.csv` and `output/stakeholder_summary.txt`.

**Expected synthetic-only checks:** 9 rows ingested, 6 accepted, 3 quarantined (duplicate, missing country, negative revenue). Revenue = $195, cost = $82, gross profit = $113; gross margin ≈ 57.95%; average order value = $32.50. These are calculations on fabricated data, not business outcomes.

## Analytics and evaluation acceptance criteria
- Revenue and cost reconcile across all group-by outputs.
- Duplicate order identifiers do not inflate sales.
- Invalid rows appear in an auditable exception export.
- Financial arithmetic uses exact decimal values rather than LLM-generated figures.
- LLM-assisted narrative can be published only with source metric references and human approval.
- No personal customer records or proprietary company data are used.

## Proposed iteration
Real-world deployment would require warehouse integration (SQL/dbt), scheduled orchestration, dashboard refresh, secrets management, least-privilege access, monitored pipelines, dataset drift checks, cost logging and formal UAT. None of those production steps are claimed as delivered here.

*Prepared as a skills demonstration aligned to a Dubai AI Data Analytics Intern job description.*
