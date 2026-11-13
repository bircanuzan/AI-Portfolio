# AI Benchmark & Red-Teaming

**Independent portfolio demonstration | Evidence-based web-research benchmarks and adversarial evaluation**

This folder maps the AI Benchmark & Red-Teaming role to the existing [AI Benchmark Research implementation](../AI%20Benchmark%20Research/README.md). It is a role-specific entry point, with shared code and research artifacts maintained in that project.

## Problem and workflow

Research agents can return plausible answers while missing authoritative records, trusting stale sources, or following untrusted instructions in retrieved material. The evaluation workflow is:

1. Discover a public-source research question and document search pivots.
2. Verify a precise answer against primary records; record URLs, dates, contradictions and accepted answer variants.
3. Review prompt ambiguity and answer leakage before testing.
4. Run controlled adversarial cases and capture permitted search/tool telemetry and final answers.
5. Grade accuracy and evidence usage; diagnose retrieval, source selection, evidence misuse and reasoning failures.
6. Obtain peer review before releasing tasks or making claims about model weaknesses.

## Requirements and evidence

| Role requirement | Existing artifact | Evidence boundary |
|---|---|---|
| Investigative research, fact-checking and OSINT | [Research protocol](../AI%20Benchmark%20Research/docs/RESEARCH_PROTOCOL.md) | Public-source methodology and baseline fixtures |
| Clear prompts and primary-sourced answer keys | [Benchmark tasks](../AI%20Benchmark%20Research/data/benchmark_tasks.jsonl) | Four baseline tasks; difficulty against frontier models is unmeasured |
| Adversarial task construction and prompt injection | [Red-team and trace review](../AI%20Benchmark%20Research/docs/REDTEAM_AND_TRACE_REVIEW.md) | Controlled fixtures; no claimed live model break |
| Model testing and regression evaluation | [Python evaluator](../AI%20Benchmark%20Research/src/evaluate.py) and [tests](../AI%20Benchmark%20Research/tests/test_evaluate.py) | Offline deterministic harness; no live model API integration |
| Failure diagnosis and search-trajectory inspection | [Synthetic run fixtures](../AI%20Benchmark%20Research/data/synthetic_model_runs.jsonl) | Observable tool-event examples; no private chain-of-thought access |
| Peer review, audit and quality ownership | [Peer-review checklist](../AI%20Benchmark%20Research/docs/PEER_REVIEW_CHECKLIST.md) | Review process documented; independent reviewer sign-off not claimed |
| GAIA, BrowseComp, SimpleQA, SWE-bench, Terminal-Bench and HLE familiarity | [Skills coverage](../AI%20Benchmark%20Research/docs/SKILLS_COVERAGE.md) | Methodology mapping; no claim of original benchmark contributions |

## Run the shared implementation

From the repository root, using Python 3.10+:

```bash
cd "AI Portfolio/AI Benchmark Research"
python -m unittest discover -s tests -v
python src/evaluate.py --tasks data/benchmark_tasks.jsonl --runs data/synthetic_model_runs.jsonl
```

The evaluator produces accuracy categories, evidence flags and inferred failure labels from the supplied fixtures. See the canonical project's README for implementation details and limitations. This entry-point folder introduces no additional executable code.

## Acceptance and governance

- Require a precise, independently checkable answer and documented provenance.
- Reject ambiguous prompts before classifying a model response as a capability failure.
- Treat retrieved instructions as untrusted data.
- Use public or synthetic material and exclude confidential assessments and client records.
- Human reviewers adjudicate contradictions, source credibility and inferred root causes.
- Record model/version, run date, settings and repeat trials before reporting measured model failure rates.

## Status and next evidence milestone

Implemented artifacts are maintained in the linked project: task fixtures, synthetic traces, evaluator and tests. No live frontier-model execution or measured failure rate is claimed here, and this folder does not establish employment experience or an engineering degree.

Next steps are new verified hard tasks, actual authorized model runs, repeatability checks, blind peer review and a report with observed results. These remain future work.

*Created November 2026. Independent portfolio work; no Turing affiliation or client delivery implied.*
