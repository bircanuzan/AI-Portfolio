# AI Strategy & Enablement Lead
## RegTech SaaS | Enterprise AI Adoption, Product Intelligence & Measurable Value

**Portfolio case study informed by a public role description at norbloc.** Independent, illustrative work; **not commissioned by norbloc**, not a representation of its internal systems, and not evidence of a live deployment.

### Executive proposition
Establish an AI capability that improves **how engineering, QA, product, customer-facing teams and leadership work**, while responsibly introducing AI-assisted functionality into a digital onboarding / KYC / KYB platform.

**Three connected workstreams**
1. **Enterprise enablement:** assess, pilot and govern AI developer assistants, testing, product discovery, knowledge retrieval, commercial enablement and automation.
2. **Product opportunities:** assess assisted KYB document extraction, discrepancy triage, anomaly prioritization and evidence-backed human review, integrated through controlled APIs.
3. **Management system:** adoption and capability building, ROI measurement, security/privacy, change management, model evaluations and accountable decision rights.

### Role-to-evidence mapping
| Role mandate | Evidence in this folder |
|---|---|
| Advise the CEO and prioritize investments | [01 — Strategy and investment case](strategy/01_AI_Strategy_and_Investment_Case.md) |
| Select AI tools and maintain a toolkit | [02 — AI toolkit and vendor scorecard](strategy/02_AI_Toolkit_and_Evaluation_Scorecard.md) |
| Drive onboarding, workshops and organization-wide adoption | [03 — Operating model and playbook](delivery/03_AI_Adoption_Operating_Model_and_Playbook.md) |
| Improve software development, QA and documentation | [04 — Engineering / QA workflow pilots](delivery/04_Engineering_QA_Product_and_Commercial_Pilots.md) |
| Embed AI into regulated products | [05 — KYB product concept](product/05_KYB_Document_Intelligence_Product_Design.md) |
| Secure use of LLMs, MCP, APIs and automation | [06 — Governance and risk register](governance/06_AI_Governance_Risk_and_MCP_Controls.md) |
| Track 80% adoption and business results | [07 — Measurement and executive dashboard](metrics/07_KPI_ROI_and_Executive_Dashboard.md) |
| Build and validate a safe workflow concept | [Executable synthetic-data demo](prototype/README.md) |
| Plan delivery | [08 — 90-day and 12-month plan](delivery/08_Transformation_Roadmap.md) |

### Architectural view
```text
CEO / AI Steering Group
   ├── AI Enablement Office: use cases, tools, training, analytics, champions
   ├── Engineering / QA: bounded, reviewed assistant workflows
   ├── Product: risk-tiered AI feature development and evaluation
   ├── Commercial: approved knowledge grounding and customer education
   └── Governance: Security, Privacy, Legal/Compliance, Product Owners
                       |
                       v
KYC/KYB workflow: ingestion -> classification/extraction -> validation
                 -> discrepancy/risk flags -> human decision -> audit evidence
```

### Implementation principles
- Treat clients' legal entity and beneficial ownership records as sensitive regulated data; use **synthetic data** during early experiments.
- No model gets autonomous KYC approval, sanctions disposition or customer rejection authority.
- Preserve provenance, versions, prompt/model revisions, access logs and evidence of human decisions.
- Measure changes against **real baselines and control cohorts**. All illustrative targets are explicitly labeled.
- Tool examples are market candidates, **not endorsements or claims of current licensing or performance**.

### Run the reproducible demo
```bash
cd "AI Strategy & Enablement Lead/prototype"
python regtech_demo.py data/synthetic_cases.json
python -m unittest discover -s tests -v
```

**Demo boundaries:** the extraction stage is deliberately mocked; the runnable code tests deterministic validations, exceptions, human routing and audit-ready output. No production model, norbloc API, live identity data or customer records are used.

**Authoring perspective:** HumanEvoX | AI transformation, organizational enablement, human-in-the-loop workflow architecture.
