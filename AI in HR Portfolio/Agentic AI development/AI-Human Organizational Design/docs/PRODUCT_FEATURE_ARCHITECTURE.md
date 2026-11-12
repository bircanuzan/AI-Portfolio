# AI-Human Organizational Design — Product features and executable scope

This document updates the former Human Capital Intelligence Agent. Existing source and provenance are preserved under the stable internal Python package \`src.hcia\`; the **external product name** is now **AI-Human Organizational Design**.

**Current status:** executable synthetic workbench, not enterprise deployment or a tested hosted-LLM session. No customer access, official G42 selection or vendor partnerships.

## Product objective

Start with business objectives and workflows, map activity volumes and exception handling, allocate work between people and agents, redesign roles and organization units, model human review and net capacity, then produce a governed executive decision pack. **Humans must approve every material people, authority and structural change.**

## Incorporating capabilities studied in leading market platforms

| Platform benchmark | Feature family incorporated into design | Actual present status |
|---|---|---|
| Orgvue Henshaw | Org hierarchy, role families, task mapping, future-state structure, scenarios | Synthetic executable hierarchy, job families and scenario; no data cleaning ML or visual editor |
| Nakisa | Position planning, people costs, workflow approvals, enterprise HRIS alignment | Synthetic headcount/cost intelligence plus human approval HOLD; **no live HCM integration or write-back** |
| Reejig Work OS | Map → Analyze → Build → Run → Measure → Log → Update; agent/workforce orchestration | Task ledger and candidate design; no real workflow rollout or measured value |
| TechWolf | Task intelligence, job skills, AI-suitability and workforce design | Skills required by synthetic future roles and task eligibility; **no actual employee matching or external benchmarking** |
| Visier Vee | Workforce diagnostics, people data governance and analytical explanations | Synthetic aggregate workforce intelligence; no enterprise statistical engine |
| G42 agent workforce initiative | Agent duties, supervision, probation, review, controlled authority, suspension | Candidate digital-agent register and human controls **as draft only** |

This is a *feature benchmark and original design synthesis*, not a claim to incorporate competitors' proprietary software or outperform commercially tested products.

## Run a unified design blueprint

From the renamed directory:

\`\`\`bash
python -m src.hcia.organization_platform
python -m unittest tests.test_organization_platform -v
python -m unittest discover -s tests -v
\`\`\`

The read-only blueprint returns 7 activity categories, 8 illustrative future roles, 7 future organization units, agent-candidate records with named human managers, skills lists, human-held decisions, audit/evidence labels, separate workforce analytics, net-capacity scenarios and financing assumptions. All organizational approvals remain HOLD.

Financial assumptions are optional. The code does not convert hypothetical recovered time into payroll savings or validated ROI.

## Next engineering increments, with acceptance criteria

1. **Work/role intelligence:** add authorized data harmonization, effective-date job families, skill ontology, workflow exceptions and measurable uncertainty; test on synthetic dirty-data fixtures.
2. **Agentic planning:** add LangGraph durable checkpoints around existing native function-calling tools; compare against a deterministic baseline for accuracy, safety and cost. Live model trace mandatory to claim live LLM operation.
3. **Digital agent lifecycle:** scoped identity, registered tools, access decisions, probation scorecards, reviewed promotion, suspended/retired states, automated emergency stop *with human authority*; test permission bypass and adversarial cases.
4. **Organization digital twin:** interactive current/future structure, span/layer analytics, versions, alternative modeling and transparent trade-offs; validate with organization design SMEs.
5. **Evidence-based workforce economics:** baseline versus matched pilot workflows, human correction and oversight labor, total run cost, tracked value and independently approved Finance assumptions.
6. **Enterprise interoperability:** signed identity, secure retrieval, read-only Oracle Fusion HCM/Workday/SAP connectors, reliable data lineage, least-privilege approval workflow and audit; write-back prohibited until approved.
7. **G42 deployment readiness:** sovereign-model API, Azure-compatible container deployment, security and Responsible AI assurance, p50/p95 and reliability under load, real end-user pilot and references.

## Public research references

- Orgvue: https://www.orgvue.com/platform/
- Nakisa: https://nakisa.com/ai-platform/
- Reejig: https://www.reejig.com/platform
- TechWolf: https://www.techwolf.ai/fall-launch-26
- Visier: https://www.visier.com/
- G42: https://github.com/G42-Careers/Agent-Jobs/blob/main/AGENTS.md
