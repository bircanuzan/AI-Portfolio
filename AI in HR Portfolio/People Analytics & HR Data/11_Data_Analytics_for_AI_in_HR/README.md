# Project 11 — Trusted HR Data, Descriptive Analytics and Metric Contracts

**Five-hundred-row synthetic HR dataset; existing PDF, Excel, pandas script, SQL templates and Power BI DAX examples are preserved.**

## New: trusted-data production approach demonstrated offline
- [Data contract and validation gates](DATA_CONTRACT_AND_QUALITY_GATES.md)
- [Python standard-library validation and aggregate metric exporter](src/trusted_workforce_metrics.py)
- [Data validation unit tests](tests/test_trusted_metrics.py)
- [Reproducible synthetic aggregate output JSON](evidence/trusted_workforce_metrics.json)

Run from this Project 11 folder:
```bash
python src/trusted_workforce_metrics.py --out evidence/trusted_workforce_metrics.json
python -m unittest discover -s tests -v
```

## Existing preserved artifacts
- [Original invented source records](synthetic_hr_data.csv)
- [Original pandas analytics script](hr_analytics_python_example.py)
- [SQL example queries](hr_analytics_queries.sql)
- [Power BI DAX measure patterns](power_bi_dax_measures.txt)
- [HR analytics Excel workbook](independent_portfolio_AI_in_HR_Analytics_Lab.xlsx)
- [Portfolio PDF](independent_portfolio_Data_Analytics_for_AI_in_HR_Portfolio.pdf)

**Distinct scope:** raw fictional source → strict data quality and denominator control → validated descriptive metrics. Project 52 handles presentation; Project 54 owns independent scenario modelling. `exit_12m` is an invented binary flag, **not a longitudinal employer attrition time series**.

[Connected workflow](../WORKFORCE_INTELLIGENCE_PIPELINE.md) · [All four projects](../README.md)
