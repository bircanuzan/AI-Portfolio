# Job requirement → portfolio evidence map

**Purpose:** Show how work in this folder maps to an AI Benchmark Researcher / LLM Red-Teaming role. A requirement appearing here is **not** an assertion that all external experience or credential prerequisites are satisfied.

| Role requirement | Evidence in this project | Status |
|---|---|---|
| Investigative research, fact-checking, technical QA | Source ledger, provenance rules and verified public baselines | Demonstrated workflow |
| GAIA, BrowseComp, SimpleQA benchmark familiarity | Methodology comparisons, source-backed grading and abstention | Demonstrated conceptual alignment; **not original benchmark authorship** |
| SWE-bench / Terminal-Bench familiarity | Comparison below: execution-based vs web-fact benchmark tasks | Conceptual only; no claimed runs |
| Humanity's Last Exam familiarity | Comparison below: hard expert reasoning vs verifiable lookup | Conceptual only; no claimed runs |
| OSINT, academic archives, local records and obscure databases | Search/registry/archive research protocol and provenance fields | Designed workflow; specialized archive challenge pending |
| Model search trajectory and log analysis | Observable tool-event schema, automated tags and review decision tree | Local synthetic replay |
| Precise benchmark prompts and primary-sourced answer keys | `data/benchmark_tasks.jsonl`; ambiguity gate | Four verified baseline fixtures |
| Red-teaming and reasoning-trap design | Pattern library; simulated incorrect-answer records | Test patterns, not verified model-breaking outcomes |
| Prompt-injection task design | Benign untrusted retrieved-page fixture and safe pass criterion | Designed, not live-tested |
| Cross-domain scaling | Re-application protocol and duplicate/leakage controls | Design protocol |
| Lead review / benchmark audit / QA owner | Release checklist and adjudication template | Independent proposed process, not a job-title claim |
| Relevant engineering bachelor’s degree | External qualification; **not evidenced by this repository** | Not claimed |

## Benchmark comparison
- **BrowseComp:** agentic web research for hard-to-locate facts; this is the closest methodology for the planned advanced work.
- **GAIA:** multi-step, real-world assistant tasks involving tools/browsing and potentially multiple modalities.
- **SimpleQA:** short-form factual questions and evaluation of correctness versus abstention.
- **SWE-bench:** software issue resolution assessed against repository tests; requires executable patches rather than fact-only answers.
- **Terminal-Bench:** execution in terminal-like environments; requires sandboxed environment/task-specific success criteria.
- **Humanity's Last Exam:** expert-created difficult questions across fields; may require specialist validation distinct from web-search benchmarking.

**No claimed performance** on any of these benchmarks, and no claim of access to private held-out test sets. Publication metadata and methodologies are attributed to their creators.

## Skills and keywords for responsible portfolio indexing
AI Benchmark Research, LLM Benchmark Design, AI Model Evaluation, Red Teaming, Prompt-Injection Testing, Research QA, Source Verification, OSINT, Web Research, Fact Checking, Hallucination Detection, Retrieval Evaluation, Agent Tool-Use Testing, Search Trajectory Debugging, Failure Root-Cause Analysis, Python, JSONL, Dataset Curation, Annotation Guidelines, Evidence-Based Rubrics, Quality Assurance, Reviewer Calibration, Adversarial Test Cases, AI Safety, Responsible AI, Human-in-the-Loop Validation, Model Monitoring, Experiment Documentation.

## Evidence-development backlog
1. Author 8–12 genuinely hard public-record tasks from multiple domains with two independent reviewers and evidence snapshots.
2. Run approved browsing-capable model comparisons; capture model versions, timestamps, token/tool settings and observable logs.
3. Publish auditable success, abstention and failure metrics with confidence intervals and human adjudication.
4. Add real retrieval-integrity and prompt-injection tests in a safe sandbox with replayable fixtures.
5. Add actual SWE-bench/Terminal-Bench **exercises** only after running their specified environments; keep separately from web-research task claims.