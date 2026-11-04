# Enterprise AI Engagement: Lead-to-Viewing Productivity

**Portfolio demonstration — synthetic data; not affiliated with Property Finder.**

**Business sponsor:** hypothetical agency CEO. **Pod:** one engagement lead / AI product owner, two forward-deployed engineers (integration and workflow), shared analytics partner. **Pilot window:** 12 weeks, conditional on approved access and privacy review.

## Problem to solve
Agents lose viable inquiries through delayed response and inconsistent qualification; agency leadership cannot attribute productivity improvements to AI rather than seasonality, advertising or staffing. Start with an operationally credible question: **Can a consent-aware, human-approved assistant reduce median lead response time and improve qualified viewing bookings without lowering customer experience?**

## Decision and delivery artifacts
1. [Engagement charter and discovery](01_Executive_Engagement_Charter.md) — client sponsor, operating model, current-state questions and decision rights.
2. [Use-case investment case](02_Use_Cases_and_Business_Case.md) — ranked opportunities, P&L logic and explicit assumptions.
3. [Architecture and data contract](03_Solution_Architecture_and_Controls.md) — system boundaries, pseudonymisation, API and approval gates.
4. [Engineering backlog and launch gates](04_Product_Backlog_UAT_and_Release.md) — two-engineer plan, acceptance tests, rollback.
5. [Controlled impact measurement](05_Experiment_and_Executive_Scorecard.md) — metrics, SQL, evaluation, statistical caution.
6. [Adoption and scaling](06_Adoption_Change_and_Productization.md) — front-line routines, ownership and reusability.
7. [Synthetic event data](data/synthetic_leads.csv), [analytics SQL](sql/lead_response_kpis.sql), [Python baseline](src/lead_triage.py), [automated tests](tests/test_lead_triage.py).

## Product hypothesis and boundaries
The assistant identifies pending inquiries, proposes a factual next response after retrieval of approved listing fields, and routes it for agent approval. It does not decide customer eligibility, make unsupported claims about properties, send without consent or silently alter CRM records.

## Run
- python src/lead_triage.py data/synthetic_leads.csv
- python -m unittest discover -s tests -v

**What is actually demonstrated:** a reusable engagement operating model, SQL measurement logic, approved-message workflow design, and executable consent-aware prioritisation baseline on synthetic records. **Not demonstrated:** model inference, live integrations, achieved ROI, production adoption or real-world A/B results.
