# Integrated Human–AI Workforce Architecture Workbench

**A connected, executable, eight-module demonstration rather than eight isolated documents.**

This is an *integration layer* for existing [Workforce Transformation Projects 01–08](../README.md), **not Project 09** and not a separate duplicated capability.

## What it actually does

Runs the existing Python model functions and reuses the existing role, governance and synthetic case files in one controlled chain:

| Input module | Real code or data used | Consolidated decision output |
|---|---|---|
| 01 — Workload & capacity | Existing \`model()\`/CSV | Human hours, modeled FTE, gaps |
| 02 — Job/skill architecture | Existing role matrix | Human-owned work, agent-assist candidates, accountable owner |
| 03 — Employee transition | Existing metric dictionary | Change safeguards and quality gates |
| 04 — Enterprise organization design | Existing \`score_option()\`/CSV | Organization choice **discussion**, risk/ownership holds |
| 05 — Digital worker orchestration | Existing \`evaluate()\`/JSON | Safe routes; risky requests held for human review |
| 06 — Strategic workforce intelligence | Existing \`run()\` and skills-gap models | 2027–2029 reference/assisted/stress scenarios |
| 07 — Product/technical architecture | Existing \`run()\` triage model | Approved/held product-backlog *discussions* |
| 08 — Workforce economics | Existing \`run()\` cost model | Opportunity vs human-review costs, no unverified ROI |

## Three real output artifacts generated

1. **\`architecture_evidence.json\`** — machine-readable results, controls, input provenance and executive HOLD status.
2. **\`executive_decision_pack.md\`** — executive scorecard, current workforce, digital agent gates, scenarios, product and economics, plus outstanding business decisions.
3. **\`executive_dashboard.html\`** — self-contained, offline, responsive dashboard with year (2027–2029) and scenario selection; no remote dependencies, API or third-party script.

## Running

Python 3.10+ from repository root; all standard library, **no paid account or API key**:

\`\`\`bash
python "Workforce Transformation/00_Integrated_Architecture_Workbench/src/architect_workbench.py" --out /tmp/humanevox-workforce
python -m unittest discover -s "Workforce Transformation/00_Integrated_Architecture_Workbench/tests" -v
\`\`\`

Open \`/tmp/humanevox-workforce/executive_dashboard.html\` in a browser. On Windows, choose any writable local output folder instead of \`/tmp\`.

On GitHub, the [existing Workforce and AI Transformation CI workflow](../../.github/workflows/portfolio-transformation-tests.yml) runs the workbench and its integration tests and uploads the **generated outputs as an Actions artifact**. Download it from the latest successful workflow run's **Artifacts** section.

## What is explicitly NOT complete or claimed

A live customer transformation, production HRIS data, actual AI/LLM inference, agent tool calls, security-validated API integration, customer HRIS permissions, validated financial ROI or human employment decisions **require a separate authorized pilot and real system credentials/data**. The workbench correctly marks its release status **HOLD**, and its outputs do not authorize such actions.

## Architecture rationale and measurement

A working demonstrator should join strategy, organization and technical work in a traceable way. This integration uses live *code execution over invented inputs*, not enterprise systems. It makes negative cases and uncertainty visible rather than pretending to have measured client savings.

**Nonduplication:** The underlying modules remain authoritative for their specialized models; this layer imports their existing functions. See [leadership theme-to-evidence map](../00_LEADERSHIP_RESEARCH_TO_EVIDENCE_MAP.md) and [executive pilot gates](../00_EXECUTIVE_CASE_AND_PILOT_PLAN.md).
