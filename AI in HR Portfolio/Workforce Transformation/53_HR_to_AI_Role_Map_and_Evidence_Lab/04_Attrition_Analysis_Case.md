# Case 1 — Synthetic 200-employee attrition analysis

**Hypothetical UAE employer pain point:** HR leaders want to understand departures and decide where to investigate employee experience and retention risks without ranking individuals or misrepresenting causes.

**Dataset:** [synthetic_200_employees.csv](data/synthetic_200_employees.csv); 200 fabricated employee IDs with department, tenure, engagement/support levels, training access and fictional exit flags. No human records, protected traits, real client or authentic attrition results.

**Method:** generate fixed input values; validate count and unique IDs; calculate number of departures / total workers and departmental rates; compare only descriptively; identify information missing (time window, populations, manager changes, labor-market factors, reasons for leaving).

**Tools:** Python 3 standard library (csv and collections), JSON/CSV, GitHub. No Power BI build, predictive model or data-science credential implied.

**Recorded baseline:** [computed synthetic counts](evidence/synthetic_attrition_baseline.json). Run with:
~~~bash
python scripts/attrition_analysis.py
~~~

**Governance:** never apply group associations to an individual employee; no intervention targeting based solely on attrition rate. For an actual employer obtain definitions, time window, minimum cell size, access approval and retention consent/lawful basis.

**Business deliverable:** a descriptive baseline and a proposed stakeholder workshop to validate causes, identify data-quality issues and decide whether an approved longitudinal pilot is warranted.

**No measured outcome or proof of causal drivers.** Project 52 already contains thematic dashboards; this case instead provides a **reproducible raw-data exercise**.
