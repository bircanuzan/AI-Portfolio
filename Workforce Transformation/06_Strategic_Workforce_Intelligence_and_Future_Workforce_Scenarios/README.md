# 06 — Strategic Workforce Intelligence & Future Workforce Scenarios

**Independent HumanEvoX case:** Atlas UAE Shared Services; 2027–2029 *synthetic* planning horizon. The numbers are invented exercise inputs, **not economic forecasts for the UAE or verified labor-market data**.

## Unique decision this project answers
What mix of people, skills, AI assistance and external capacity might an organization need over a multi-year horizon, under uncertain demand and technology performance? This **extends** [Project 01's current-capacity baseline](../01_Capacity_and_Headcount_Decision_Lab/) and [Project 02's job architecture](../02_Role_Architecture_Skills_and_Redeployment/) instead of duplicating them.

## Artifacts and technical demonstrations
- [Strategy, planning and scenarios](01_Strategic_Planning_and_Scenarios.md) — horizons, assumptions, scenario families, human decision rules, reskilling and sourcing.
- [Data platform, lineage, UAE context and governance](02_Workforce_Intelligence_Data_Architecture.md).
- [Invented demand-supply dataset](data/synthetic_workforce_outlook.csv) and [synthetic skills gap dataset](data/synthetic_capability_gaps.csv).
- [Runnable deterministic scenario calculator](src/forecast_scenarios.py) and [skills-gap calculator](src/skills_gap.py).
- [Unit tests](tests/test_workforce_intelligence.py).

## Leadership research relevance
- MOHRE research: labour-market intelligence, data integrity, source governance and evidence-based workforce decisions — **not** a claim of access to the MOHRE Labour Market Observatory.
- e& research: integrated workforce visibility, Oracle Fusion Cloud HCM, Oracle Grow and Dynamic Skills as **company-level platform context**, not tools used in this demo.
- Bukhatir / Noaman Minhas: unified skills, talent, learning and workforce planning.
- G42: capacity and capability beyond raw headcount; work decomposition and human accountability.
- ADNOC: enterprise AI skills, career mobility and frontline enablement; company initiatives only.

## Run (standard-library Python)
From repository root:

    python "Workforce Transformation/06_Strategic_Workforce_Intelligence_and_Future_Workforce_Scenarios/src/forecast_scenarios.py"
    python "Workforce Transformation/06_Strategic_Workforce_Intelligence_and_Future_Workforce_Scenarios/src/skills_gap.py"
    python -m unittest discover -s "Workforce Transformation/06_Strategic_Workforce_Intelligence_and_Future_Workforce_Scenarios/tests" -v

## Evidence boundary
The scripts perform simple arithmetic and transparent assumptions, **not machine-learning predictions or automated employment decisions**. No Oracle/Workday/SAP tenant, official government source, real employee records or Power BI workspace is connected. Decisions about hiring/redeployment always require authorized human review.

[Master portfolio](../README.md) · [People analytics](../../People%20Analytics%20%26%20HR%20Data/)