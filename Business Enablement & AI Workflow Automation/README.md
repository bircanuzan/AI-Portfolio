# Business Enablement & AI Workflow Automation — MoonTech JD-aligned project

**Role benchmark:** [MoonTech / ITCAN Business Enablement Specialist](https://ae.indeed.com/viewjob?jk=84c72f6cdbe6e80c), Dubai remote.

**Project nature:** Independent **synthetic** creator-commerce business operations case, not a MoonTech engagement or integration with proprietary Moon AI agents. The n8n example is an importable *draft* and has not been executed in a live n8n instance. Input data and sample KPI numbers are fictional.

## Problem
A campaign operations organization loses time moving campaign briefs across sales, creator matching, approvals, campaign execution and attribution reporting. Leadership needs clear quarterly objectives, defined ownership, automated handoffs, CRM visibility and evidence of adoption.

## Deliverables
1. [Quarterly OKRs, discovery, SOP and RACI](OPERATING_MODEL_OKRS_SOP.md)
2. [Synthetic intake/throughput data](data/synthetic_campaigns.csv)
3. [Executable Python operations KPI script](src/enablement_dashboard.py) with [unit tests](tests/test_enablement_dashboard.py)
4. [n8n draft-only mock workflow](workflows/n8n_campaign_draft_only.json) — manual trigger, mock intake, validation, draft task generation. No external data or write actions.
5. [Implementation and adoption runbook](IMPLEMENTATION_AND_ADOPTION.md)

## Run
`python src/enablement_dashboard.py`
`python -m unittest discover -s tests -v`
Python 3.10+, standard library only. The report is computed from **hypothetical** data.

## Skills mapped to advertised JD
Quarterly OKR facilitation and cascade; process mapping / bottleneck discovery; SOPs; cross-functional RACI; CRM and SaaS tool administration *concepts*; n8n workflow *design*; Make/Zapier equivalent trigger–filter–action mapping; AI-agent handoff safety; KPIs, executive reporting and dashboards; training workshops, change management and measured adoption. Distinguish planning/documentation and local scripts from real SaaS administration or production n8n delivery.

## What would count as real additional proof
Import and run this workflow in a personal n8n sandbox with screenshots and run IDs; connect an authorized test CRM; show successful and failed executions, retry/idempotency tests, actual elapsed times, workshop feedback, and a dated acceptance log. None of those are currently claimed.

## Related existing work
[Business Process Mapping and AI Transformation](../30_Business_Process_Mapping_Analysis_and_AI_Transformation/README.md) · [AI Adoption](../AI%20Adoption/README.md) · [AI Integration Engineering](../AI%20Integration%20Engineering/README.md).
