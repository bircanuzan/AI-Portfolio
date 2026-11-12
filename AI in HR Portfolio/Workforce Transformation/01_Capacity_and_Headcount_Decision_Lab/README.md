# 01 — Capacity and Headcount Decision Lab

**Business problem:** A UAE client requests four additional hires after adopting AI tools. Finance wants productivity; managers worry about service quality; employees need clarity. Headcount cannot be decided from activity counts alone.

## Methodology
1. Discovery workshop: business demand, service definition, SLA, exceptions, case mix, customer experience, constraints and data ownership.
2. Observe tasks by role and measure task minutes, volume, rework, queue, meetings, coverage and utilization.
3. Calculate effective human capacity = paid hours × productive fraction × current FTE.
4. Baseline labor demand = monthly volume × minutes per case / 60.
5. Build *illustrative* AI-assisted scenario: human time saved applies only to eligible, successfully assisted case share; all AI-attempted cases incur human-review minutes.
6. Add a demand-variability buffer; compare modeled required FTE with staffing. Do **not** treat the result as authority to hire, redeploy or reduce staff.
7. Validate in supervised pilot: time study, SLA, error/exception rates, job satisfaction, accessibility, quality, privacy and actual review load.
8. Present options: process redesign, capability investment, schedule changes, hiring case or staged combination.

## Artefacts
- [Synthetic process inputs](data/synthetic_workload.csv)
- [Python scenario calculator](src/workforce_capacity.py)
- [Unit tests](tests/test_capacity.py)

## Outputs and decision gates
- Role-by-role baseline workload, protected capacity, assistable workload, modeled demand and demand-to-FTE gap
- Scenario sensitivity: compare with/without AI, eligibility and review rates; **never equate freed capacity to cash savings**
- Human decision log: manager validates assumptions, HR verifies impact, finance checks cost, legal reviews employment consequences, IT/security approves any tooling

## Practical interview story
"When a manager asks for additional headcount, I would not accept a raw utilization claim. I would study actual case mix, priority, quality, reviews and workforce constraints, compare baseline versus redesigned work, and only then develop a validated hiring and capability plan."

**Boundaries:** Synthetic sample only; no employee records, actual capacity measurements, hiring recommendation or client results. Python is a transparent scenario model, not an AI/ML forecaster.
