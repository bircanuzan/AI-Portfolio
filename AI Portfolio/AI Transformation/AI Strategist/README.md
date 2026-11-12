# AI Strategist | Enterprise AI Engagement & Deployment Strategy
## Portfolio case study: Real-estate agency AI adoption

**Role alignment:** sector_organization — AI Strategist (job-description-informed independent case study).

**Status:** Designed as a reproducible portfolio prototype using synthetic data. **Not a sector_organization engagement, product integration, live agency deployment, or claimed commercial result.** No real property, client, customer, or proprietary company data is included.

### Executive brief
A real-estate marketplace's strategic agency customers struggle with lead response time, inconsistent listing quality and inefficient manual work. This project shows how an AI Strategist can lead a senior-client engagement from discovery and measurable business case through product requirements, a defensible engineering backlog, pilot evaluation, frontline adoption and reusable scaling.

**Executive decision:** Pilot a consent-aware, human-reviewed lead response assistant with two agency cohorts. Establish baseline response and viewing conversion performance before deciding to scale. No automatically sent messages, lead rejections or pricing decisions.

### Evidence in this repository
| Role requirement | Working / written evidence |
| --- | --- |
| CEO/COO discovery; use-case selection | Stakeholder map, discovery agenda, scored use-case register |
| Business case; commercial judgment | Unit economics, assumptions, sensitivity, go/no-go criteria |
| Product-owner delivery with 2 engineers | Acceptance criteria, APIs/data contract, backlog, dependency map |
| LLM literacy, workflows, CRM | Consent-aware deterministic baseline, anonymised prompt contract and human review |
| SQL and analytics | PostgreSQL-style KPI query and synthetic event data |
| Prototype-to-production & adoption | Release gates, control-group design, training and change plan |
| Executive storytelling & scale | Board scorecard, reuse decision and productization criteria |

### Repository structure
- [Enterprise AI Engagement project](Enterprise_AI_Engagement_for_Real_Estate_Agencies/README.md): the main case study, charter and technical artifacts.

### How to run the baseline
From the main project directory: **python -m unittest discover -s tests -v** and **python src/lead_triage.py data/synthetic_leads.csv**. Python standard library only.

### Important claims boundary
The Python workflow is a testable **deterministic baseline**, not a production LLM, deployed API, integrated CRM, measured uplift or evidence of client-delivered engagement. AI generation is specified as a gated integration design, not simulated as though an LLM were called. Technical controls and methodology are portable across industries.
