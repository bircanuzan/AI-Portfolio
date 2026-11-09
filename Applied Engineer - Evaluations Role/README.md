# Applied Engineer — Evaluations Role

**Hands-on Python evaluation engineering | PR-to-benchmark design | regression tests | multi-candidate analysis | Git/CI evidence**

> **Evidence disclosure:** This is an independently authored, synthetic engineering demonstration for portfolio review. The scenario and three candidate patches are not commissioned Mercor work, actual Claude Code/Codex runs, a client production service, or proof of prior enterprise-scale codebase ownership. Workflows and source are real, inspectable GitHub files.

## Executive technical summary

A source-controlled mini codebase that converts a **synthetic pull-request requirement (PR-101)** into an executable AI-coding evaluation suite. It tests invoice discount/tax ordering, decimal precision, input validation and backward compatibility. Two intentionally faulty candidates create **observable, independently reproducible regressions**; a deterministic evaluator reports exact expected-versus-observed evidence, weighted rubric scores and environment-vs-candidate failure classifications.

The repository-root [GitHub Actions workflow](../.github/workflows/applied-engineer-evaluations.yml) runs the full pipeline on Python 3.11 and 3.12 and archives machine-readable artifacts. Consult the live [Actions page](https://github.com/bircanuzan/AI-in-HR-Portfolio/actions/workflows/applied-engineer-evaluations.yml) before claiming CI is green.

## Role requirements mapped to inspectable evidence

| Applied-engineering requirement | Executable or documentary evidence | Strength / limits |
|---|---|---|
| Complex codebase navigation and architectural understanding | [Repository audit](scripts/repository_audit.py) captures real Git revision, repository file inventory and local import/function graph; [architecture & CI dossier](docs/GIT-CI-EVIDENCE.md) maps implementation → candidate → evaluation → tests | **Real GitHub code, synthetic small case**; not equivalent to production-scale software ownership |
| Git change tracking and pull-request evaluation | PR-101 [source-controlled task and patch acceptance criteria](docs/PR-101-Evaluation-Task.md), [Git workflow/CLI evidence](docs/GIT-CI-EVIDENCE.md), commit history | Real commits; documented PR procedure, not fabricated PR review |
| CI automation and verification | [GitHub Actions](../.github/workflows/applied-engineer-evaluations.yml), [CI shell runner](scripts/ci.sh), unit/edge-case tests, uploaded JSON artifacts | Workflow configured; verify actual Actions execution |
| Python coding, code quality and test engineering | [Reference module](src/invoice.py), [two regression-inducing patches](src/candidate_agents.py), [unit tests](tests/test_invoice.py) | Working project-specific reference code |
| Turn PRs into executable coding-agent evaluations | [PR-101 specification](docs/PR-101-Evaluation-Task.md), [10 objective test oracles](evaluation_cases.json), [benchmark CLI](benchmark.py) | Synthetic PR, suitable as a reusable pattern |
| Agent evaluation and model benchmarking | [Deterministic evaluation engine](src/eval_engine.py) and [candidate patch implementations](src/candidate_agents.py) | **Three synthetic candidate patches** — no real model comparisons claimed |
| Rubrics, judgment, evidence, failure analysis | [Versioned weighted rubric](rubric.json), [failure analysis](docs/FAILURE-ANALYSIS.md), explicit expected vs observed and failure taxonomy | Machine-checkable rubric plus [source-citation validation](src/review_validator.py), [qualitative schema](rubrics/qualitative_review.json), [review protocol](docs/LLM-JUDGE-PROTOCOL.md); no external judge invoked |
| Reproducibility and experiment artifacts | [CI script](scripts/ci.sh) creates `artifacts/benchmark-results.json` and `artifacts/repository-audit.json` | Deterministic local evaluation; commit SHA included when run in Git checkout |

## Quick start

Requirements: Python 3.11+ and Bash. No paid AI API, external Python packages, or credentials required.

```bash
git clone https://github.com/bircanuzan/AI-in-HR-Portfolio.git
cd AI-in-HR-Portfolio
bash "Applied Engineer - Evaluations Role/scripts/ci.sh"
```

Run stages independently:

```bash
cd "Applied Engineer - Evaluations Role"
python -m unittest discover -s tests -p 'test_*.py' -v
python benchmark.py --out artifacts/benchmark-results.json
python scripts/repository_audit.py --out artifacts/repository-audit.json
```

## Expected local synthetic benchmark (not measured model performance)

- **Reference patch**: 10/10 case passes, rubric score 100/100.
- **Tax-before-discount patch**: expected failures PR101-C02 and PR101-C03, score 75/100.
- **Truncation patch**: expected failure PR101-C04, score 90/100.

Scores above are calculated from authored fixtures and tests, **not** claimed results from external AI model runs. Independent test assertions will catch deviations.

## Key files

```text
Applied Engineer - Evaluations Role/
├── README.md
├── benchmark.py
├── evaluation_cases.json
├── rubric.json
├── rubrics/qualitative_review.json
├── src/
│   ├── invoice.py
│   ├── candidate_agents.py
│   ├── eval_engine.py
│   └── review_validator.py
├── tests/
│   ├── test_invoice.py
│   ├── test_eval_engine.py
│   └── test_review_validator.py
├── scripts/
│   ├── ci.sh
│   └── repository_audit.py
└── docs/
    ├── PR-101-Evaluation-Task.md
    ├── FAILURE-ANALYSIS.md
    ├── GIT-CI-EVIDENCE.md
    └── LLM-JUDGE-PROTOCOL.md

# At repository root:
.github/workflows/applied-engineer-evaluations.yml
```

## Engineering judgment, not buzzwords

The evaluator distinguishes code regressions from infrastructure failures. Its acceptance tests assert explicit expected numerical outcomes, including half-cent rounding and invalid-input behavior. The reference baseline must pass every case for the CLI to succeed. The GitHub workflow separately runs unit tests, compiles sources and collects machine-readable evidence. The [evidence dossier](docs/GIT-CI-EVIDENCE.md) candidly lists what remains necessary to establish experience with a **large production codebase**, real pull requests and real coding-agent outputs.

**Author:** Independent technical portfolio — Bircan Uzan | Python 3 · Git · GitHub Actions · unittest · JSON rubrics · deterministic AI evaluation patterns
