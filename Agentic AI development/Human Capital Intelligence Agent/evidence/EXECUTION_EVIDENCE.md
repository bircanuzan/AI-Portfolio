# Actual GitHub Actions execution evidence

**Source:** [Successful GitHub Actions run 41660241078](https://github.com/bircanuzan/AI-in-HR-Portfolio/actions/runs/41660241078)  
**Repository / branch:** bircanuzan/AI-in-HR-Portfolio, main  
**Commit:** 1edcce6fc9da100eae460bf2cbe62c8780a0293b  
**Date:** 3 November 2026 UTC | **Runner:** GitHub-hosted ubuntu-latest, Python 3.11.

## Observed results, confirmed from actual job logs
- Automated functional, access control, privacy, audit and connector tests: **35 tests passed**.
- Preauthored deterministic numeric benchmark assertions: **12/12 passed**.
- Benchmark loops: **50** sequential *in-process* executive briefing calls.
- Observed median (p50): **0.0353 ms** per in-process call.
- Observed p95: **0.0534 ms** per in-process call.
- Observed scripted errors: **0**.
- Artifact: hcia-synthetic-evidence / benchmark-results.json attached to the run.

**Interpretation limits:** timing excludes authentication, HTTP, audit writes, cloud, model inference, database services and enterprise HRIS/ATS integration; small sequential run, not a concurrency, production reliability or value/ROI benchmark. Values come from machine execution and may vary by runner. No live LLM or client data were used.

## Reproduce
From the project directory:

    python -m pip install -r requirements.txt
    python -m unittest discover -s tests -v
    python scripts/benchmark.py

See docs/EVALUATION_AND_METRICS.md, docs/PRODUCTION_READINESS.md and the live GitHub Action logs. Do not convert these local results into an unsupported production SLA.
