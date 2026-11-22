# Skills, technology, methodology, deliverables and evidence

## Task coverage

1. **Learning activities:** Analyze measurable objectives; design practice, feedback, spaced retrieval and authentic work simulations; check alignment to competency outcomes.
2. **Accessibility and inclusive design:** Review captioning, keyboard support, accessible media alternatives, cognitive load, language clarity, accommodations, and UDL-inspired flexible participation.
3. **Digital delivery:** Assess LMS/LXP constraints, mobile-first learning, bandwidth, self-paced versus instructor-led flows, SCORM/xAPI data concepts, privacy and learner support.
4. **Assessment validity:** Detect mismatches between learning objective and assessment, unclear scoring rubrics, unscored high-stakes judgments, and bias.
5. **Evidence and evaluation:** Identify unsupported pedagogical claims, compare alternative solutions and recommend data collection beyond completion rates.
6. **AI model feedback:** Build synthetic prompt-response comparisons, reference-answer criteria, failure tags and versioned evaluation reports.

## Technology / AI / tools used

| Technology | Demonstrated use | Evidence |
|---|---|---|
| Python 3 standard library | Rule-based structured evaluation, JSONL validation, metric aggregation | `evaluate_instructional_design.py` |
| JSON and JSONL | Machine-readable case fixtures, reference labels and authored candidate answers | `data/evaluation_cases.jsonl` |
| CSV | Export structured findings for spreadsheets / business analytics | Script export, when run |
| Python unittest | Automated tests for valid datasets, schema and deliberate counterexamples | `test_evaluate_instructional_design.py` |
| Human rubric / QA | Expert rating anchors, error taxonomy, proposed adjudication | `EXPERT_RUBRIC.md` |
| WCAG 2.2 / UDL 3.0 | Design and review concepts; linked official documentation | `EXPERT_RUBRIC.md` |
| Excel / Power Query / Power BI | Potential QA dashboards for exported CSV; **not used or integrated here** | Design option only |
| LMS/LXP, SCORM, xAPI | Metadata and learning-data design concepts; **no integration** | Methodology only |
| Model APIs, prompt engineering, AI agents | Future integration with versioned outputs; **no model API calls** | Roadmap only |

**Critical boundary:** This is a runnable offline QA demonstration *against hand-authored response fixtures*. It does not demonstrate executed model training, measured LLM quality, verified accessibility compliance or commercial customer outcomes.

## Methodology and documentation pipeline

- **1 — Discovery:** Audience analysis, performance goals, accessibility requirements, delivery constraints and risk context.
- **2 — Objective mapping:** Decompose performance requirements into observable outcomes; align activities and assessment evidence.
- **3 — Scenario design:** Author real-world educational-design prompts, strong vs flawed candidate answers, and reference checks.
- **4 — Benchmark preparation:** Version examples, apply a transparent rubric, tag failure severity, and keep prompt/reference documentation.
- **5 — Evaluator QA:** Programmatically check structured labels; human reviewers assess pedagogical reasoning, evidence and contextual validity.
- **6 — Error analysis:** Explain which claim or design decision fails, its impact, and the corrected instructional approach.
- **7 — Model comparison (future):** If actual LLM outputs become available, benchmark them consistently by version; track regressions and reviewer variance.
- **8 — Governance:** Human-review critical accessibility or learner-impact judgments before any real use.

## Measurable KPIs

### Current artifact outputs (not yet a real-model evaluation)
- Synthetic case count
- Fixture label agreement
- Deliberate-error detection count
- Schema validity on authored structured answers
- Offline unit-test success count when tests are actually run

### Proposed actual project KPIs (not achieved)
- Expert rubric scores by dimension (0–12)
- Valid assessment alignment rate and severity-weighted error density
- Accessibility-related critical defect rate
- Unsupported pedagogical claim rate
- Dual-reviewer agreement and adjudication turnaround
- Model regression rate across evaluation releases
- Learning transfer and behavior-change indicators only if studied with participants

## Professional portfolio project summary

**Requirement:** Determine whether AI-generated instructional plans are professionally defensible, accessible and pedagogically aligned.

**Methodology:** Synthetic expert tasks, independent reference decisions, 6-dimension human QA rubric, deterministic label verification, error rationale and an improvement recommendation.

**Tech/AI:** Python, JSONL, CSV, unit testing, rubric design, benchmark design; WCAG/UDL/learning-design frameworks; optional later LLM API evaluation.

**Results:** Committed source code, test suite, sample data and proposed measurement schema. No measured client KPIs, model improvement, completed accessibility audit or live LLM results claimed.
