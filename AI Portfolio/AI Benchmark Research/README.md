# AI Benchmark Research

**Independent applied research portfolio | Evidence-based web research, OSINT, LLM evaluation & red-teaming**

A reproducible, source-led benchmark authoring and evaluation demonstration aligned with AI Benchmark Researcher responsibilities: **hard-fact discovery, primary-source verification, adversarial task design, model testing, observable tool-trace debugging, and reviewer QA**.

> **Evidence boundary:** This is an independently constructed research/evaluation demonstration. The reference tasks are verified baseline fixtures, **not claimed to defeat a frontier model**. The included example model runs are *synthetic*, not measurements of Claude, GPT, Gemini, or any named model. No access to private chain-of-thought is claimed. Skills coverage is a demonstration roadmap, not certification of employment, authorship of established benchmarks, or an engineering degree.

## What this project demonstrates

1. **Investigative web research & OSINT:** scoped queries; authority and provenance checks; archival and registry lookup strategy; discrepancy tracking; multilingual search pivots; ethical public-source research.
2. **Benchmark methodology:** task-design principles informed by [GAIA](https://ai.meta.com/research/publications/gaia-a-benchmark-for-general-ai-assistants/), [BrowseComp](https://openai.com/index/browsecomp/), [SimpleQA](https://openai.com/index/introducing-simpleqa/), and comparison notes for SWE-bench, Terminal-Bench and Humanity's Last Exam.
3. **Primary-sourced answer keys:** traceable evidence, stable factual answers, accepted-answer normalization, dates, provenance and abstention handling.
4. **Red-teaming:** distractor domains; stale-source traps; prompt-injection-in-retrieval fixtures; contradictory claims; query fixation; answer contamination; provenance laundering.
5. **Model QA and trace diagnosis:** observable search queries, tool responses, retrieved sources and final outputs; classify retrieval misses vs evidence misuse vs reasoning mistakes vs ambiguity.
6. **Python evaluation:** dependency-free deterministic grading; synthetic run replay; benchmark schema validation; regression tests; JSON outputs.
7. **Quality ownership:** peer-review checklist, severity taxonomy, escalation standards, leakage controls, benchmark refresh and versioning.

## Repository contents

| Path | Purpose |
|---|---|
| [data/benchmark_tasks.jsonl](data/benchmark_tasks.jsonl) | Four verified factual benchmark *baseline* tasks and source-backed answer keys |
| [data/synthetic_model_runs.jsonl](data/synthetic_model_runs.jsonl) | Explicitly **simulated** correct, incorrect and abstained responses, with observable tool event fixtures |
| [src/evaluate.py](src/evaluate.py) | Task validation, deterministic response grading, trace and source-usage analysis |
| [tests/test_evaluate.py](tests/test_evaluate.py) | Unit tests for grading, source verification flags and failure taxonomy |
| [docs/RESEARCH_PROTOCOL.md](docs/RESEARCH_PROTOCOL.md) | OSINT discovery, verification, research logs, provenance and ambiguity standard |
| [docs/REDTEAM_AND_TRACE_REVIEW.md](docs/REDTEAM_AND_TRACE_REVIEW.md) | Adversarial task patterns, injected-document fixture and model-run triage |
| [docs/PEER_REVIEW_CHECKLIST.md](docs/PEER_REVIEW_CHECKLIST.md) | Rubric, adjudication, peer-review and release gate |
| [docs/SKILLS_COVERAGE.md](docs/SKILLS_COVERAGE.md) | Job requirement-to-evidence mapping with honest limitations |

## Quick start

Python 3.10+; **no external dependencies**.

```bash
cd "AI Portfolio/AI Benchmark Research"
python -m unittest discover -s tests -v
python src/evaluate.py --tasks data/benchmark_tasks.jsonl --runs data/synthetic_model_runs.jsonl
```

The CLI outputs a JSON summary with `correct`, `incorrect`, `not_attempted`, evidence flags and inferred failure labels. This is an **offline local harness**, not an API integration or live frontier-model eval. To evaluate actual models, record *permitted* tool telemetry and final responses in the same run schema, record model/version/date/settings, and obtain necessary access.

## Task-authoring principles

- **Single checkable answer:** freeze the publication/version and avoid time-sensitive or person-dependent answer drift.
- **Hard to discover; easy to verify:** multi-hop clues and obscure public records are preferred over trivia; do not call a task difficult until tested against a target model.
- **Evidence-first:** answer key cites official publication, registry, primary archive, or other independently credible records. A URL alone does not establish that a claim is true.
- **Fairness:** ambiguous or underspecified prompts are rejected before being labeled model failures.
- **Reproducibility:** save query plan, retrieved source metadata, timestamp, search/tool log and reviewer verdict.
- **Safety:** no credential harvesting, private-person profiling, website abuse, or hidden-instruction execution.

## Benchmark references

These are **methodological references**, not claims of contributions to their original datasets:
- GAIA — multi-step research, browsing and tool use: https://ai.meta.com/research/publications/gaia-a-benchmark-for-general-ai-assistants/
- BrowseComp — difficult-to-find facts with checkable short answers: https://openai.com/index/browsecomp/
- SimpleQA — fact-seeking questions and explicit abstention: https://openai.com/index/introducing-simpleqa/
- RFC Editor — official protocol publication records: https://www.rfc-editor.org/info/rfc9110/
- NIST — GenAI risk-profile official bibliographic record: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

**Next evidence milestone:** run an approved model harness against newly authored, independently verified *hard* items; export real telemetry; obtain blind second-reviewer sign-off; publish measured pass/fail rates with model/version and caveats.

---
*Portfolio work product; November 2026. No client involvement or specific model failure is represented unless independently documented.*