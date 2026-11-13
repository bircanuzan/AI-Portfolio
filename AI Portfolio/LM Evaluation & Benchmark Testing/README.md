# LM Evaluation & Benchmark Testing

**Portfolio track:** Applied AI evaluation, independent benchmark design, LLM testing, red-teaming and model quality assurance  
**Project type:** Reusable **reference delivery blueprint** for remote full-time or freelance AI evaluation roles  
**Evidence status (13 November 2026):** Methodology and KPI framework documented. **No client commission, live benchmark run, model comparison, achieved SLA, or independently verified client result is asserted here.**

## 1. Client requirement / problem statement

An AI lab, software provider or enterprise deploying a language model needs a defensible answer to five questions:
1. Is the model accurate, grounded, consistent and safe for the intended domain?
2. Which tasks, prompts, languages, modalities, contexts and edge cases produce failures?
3. Do automated scores agree sufficiently with expert reviewers?
4. Can observed regressions be detected before model or prompt releases?
5. Can decisions be reproduced from versioned cases, prompts, model outputs, sources and adjudication records?

**Representative client deliverables:** evaluation requirements matrix, risk/acceptance thresholds, test dataset and labeling guidelines, human-review rubric, benchmark suite, model comparison report, failure taxonomy, regression gate, QA evidence pack, issue log and executive scorecard.

## 2. Technologies / technical stack

| Layer | Technologies and purpose |
|---|---|
| Test authoring and evaluation | Python 3, Jupyter, pandas, pytest, JSON/JSONL, CSV; deterministic assertion-based graders and structured review workflows |
| Model and application access | Azure AI Foundry / Microsoft Foundry, Azure AI and model APIs, REST APIs; provider-agnostic interfaces for consistent test runs |
| LLM quality | Exact-match and normalized answer checks, reference-based grading, rubric scoring, pairwise evaluation, calibration and adjudication |
| Retrieval and factuality | Source provenance logs, URL/record IDs, citation checks, retrieval relevance and grounded-answer review |
| Repeatability | Git/GitHub version control, configuration snapshots, pinned benchmark versions, GitHub Actions CI where implemented |
| Reporting | Excel, Python visualizations and tabular QA dashboards |
| Optional integrations / extension points | LangSmith or Langfuse traces, OpenTelemetry, RAG evaluation frameworks, experiment tracking; **not represented as deployed here** |

## 3. Core professional skills

LLM evaluation and training; AI model QA; AI benchmarking; evidence-based web research; model factuality and hallucination testing; instruction-following evaluation; chain-of-actions/tool-output review; prompt and scenario design; adversarial/red-team test creation; rubric engineering; annotator calibration; error analysis; root-cause investigation; data quality control; performance testing; Python test automation; stakeholder reporting; responsible AI; auditability and release governance.

## 4. Methodology: end-to-end

1. **Discovery:** capture use cases, populations, supported languages, risk appetite, model versions, policy constraints and intended decisions; document explicit non-goals.
2. **Risk-based test plan:** map task families to failure modes (factuality, reasoning, instruction following, ambiguity, retrieval, hallucination, bias, safety, tool-use and multilingual handling).
3. **Benchmark construction:** build a stratified, leakage-aware dataset with cases, input prompts, ground truths or adjudication rules, sources, expected behavior, severity and immutable case IDs.
4. **Rubric and reviewer guide:** define pass/fail criteria and anchored 1–5 scales; pilot cases, dual-label samples, resolve rubric ambiguity and measure inter-rater consistency.
5. **Execution:** record model/version, parameters, timestamps, prompt templates, retrieved evidence, responses, tool observations, token usage and latency where available.
6. **Scoring:** combine deterministic checks with calibrated human scoring; separate verified factual errors from non-scored ambiguity; calculate confidence intervals for rates where sample sizes permit.
7. **Failure triage:** classify retrieval failure, unsupported claim, flawed reasoning, omission, refusal, prompt injection susceptibility and specification conflicts.
8. **Regression and release gate:** replay critical cases against candidate versions, compare changes to baseline, block on severe unresolved failures and archive the decision.
9. **Handoff:** deliver scored dataset, reproducible scripts/instructions, severity-ranked remediation backlog, acceptance evidence and executive summary.

## 5. Example client acceptance criteria

| Dimension | Proposed requirement |
|---|---|
| Coverage | Include every high-risk use case and agreed critical edge-case family |
| Ground truth | 100% of scored factual cases have verified reference or defined adjudication protocol |
| Traceability | Every score maps to case ID, model/prompt version, output and review evidence |
| Critical safety | No unresolved severity-1 failures at release |
| Review discipline | Disagreements are adjudicated and documented; blind-review where practical |
| Repeatability | Same benchmark version can be rerun with identical scoring logic |
| Data protection | Mask personal data, enforce access controls and follow the client's retention policy |

## 6. SLA / KPI / performance scorecard

**All values below are illustrative targets for a future engagement—not achieved outcomes.** Client-specific baseline, sample size, severity definitions and contractual SLAs must be agreed first.

| KPI | Calculation | Draft target | Measured result |
|---|---|---:|---|
| Evaluation case coverage | tested priority requirements / total priority requirements | 100% for critical requirements | Not measured |
| Benchmark completeness | cases with required schema and evidence / total cases | >= 98% | Not measured |
| Reference provenance | factual cases with verified sources / factual cases | 100% | Not measured |
| Reviewer agreement | weighted Cohen kappa on double-scored subset | >= 0.75 | Not measured |
| Label quality acceptance | accepted reviewed annotations / sampled annotations | >= 97% | Not measured |
| Critical regression pass | passing critical cases / total critical regression cases | 100% before release | Not measured |
| Severe defect escalation SLA | time from confirmed severity-1 defect to owner acknowledgment | <= 4 business hours | Not measured |
| Standard defect triage SLA | time from confirmed defect to categorized ticket | <= 1 business day | Not measured |
| Reporting timeliness | reports delivered by agreed milestone / all due reports | >= 95% | Not measured |
| Data handling incidents | confirmed unauthorized disclosures | 0 | Not measured |

**Model quality metrics to report, not pre-claim:** task accuracy, supported-claim precision, hallucination rate, refusal precision/recall, instruction adherence, human preference win rate, pass@k, citation correctness, p50/p95 latency, tokens/cost per evaluated case and rate of critical failures. Each requires a defined denominator and test dataset.

## 7. Deliverables and evidence artifacts

- `README.md` — scope, client requirement, technologies, competencies, methodology and acceptance criteria.
- `metrics/scorecard_template.csv` — evidence-ready metric collection sheet, with unmeasured values clearly marked.
- **Future proof of execution (not yet present):** anonymized benchmark cases, executable Python graders, real run logs, reviewer calibration output, reproducible test results and remediation tracking.

## 8. Professional positioning

Relevant to **LLM Evaluation Specialist, AI Benchmark Researcher, AI Quality Analyst, Model Evaluation Lead, AI Red Team/Evaluation Consultant**, remote full-time employment and remote project-based contracts.

**Confidentiality / evidence note:** No private customer data, proprietary model traces, protected datasets or unsupported performance claims are included.  
**Portfolio:** [AI Portfolio](../../) · [AI Benchmark Research](../AI%20Benchmark%20Research/).
