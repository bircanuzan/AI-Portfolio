# Git, multi-file codebase investigation and CI evidence

**Evidence standard:** Separate what is concretely implemented here from career claims. This repository is a real, versioned GitHub codebase. This project is a small synthetic reference application and **does not prove prior ownership of a complex production service**.

## Verified GitHub execution — 9 November 2026

- **Real Git branch and review diff:** [Pull request #5](https://github.com/bircanuzan/AI-in-HR-Portfolio/pull/5), merged by squash commit [d6a22d5](https://github.com/bircanuzan/AI-in-HR-Portfolio/commit/d6a22d5610d012403c9704f9a46dfc8532180e97).
- **Evaluation CI:** [successful GitHub Actions run #12](https://github.com/bircanuzan/AI-in-HR-Portfolio/actions/runs/42582559552), both Python 3.11 and Python 3.12 jobs successful. Prior run logs explicitly recorded **29 passing unit tests** on Python 3.11 and produced the same benchmark pipeline.
- **Repository-wide taxonomy and link audit:** [successful audit run #84](https://github.com/bircanuzan/AI-in-HR-Portfolio/actions/runs/42582559583). The taxonomy now has an explicit approved role-project allowlist while preserving a fatal check on unknown roots.
- **Tested local fixture performance:** synthetic reference patch **10/10 (100/100)**; synthetic tax-order bug **8/10 (75/100)**; synthetic rounding bug **9/10 (90/100)**. These are executable candidate-patch fixture results, **not** real AI model leaderboard scores.
- **Artifacts:** The evaluation workflow uploads JSON benchmark output and repository inventory for each Python version. Inspect its Actions run artifacts to independently verify outputs and source revision.

These links establish actual versioned commits, a PR, CI executions and test evidence, **not** a claim that the code was deployed to a commercial production system.

## Implemented and verifiable

| Engineering requirement | Evidence you can inspect |
|---|---|
| Multi-module codebase tracing | `src/invoice.py` → `src/candidate_agents.py` → `src/eval_engine.py` → `benchmark.py` |
| Git versioning and change history | GitHub file history and commit SHA; `git log --oneline -- "Applied Engineer - Evaluations Role"` |
| Git patch/review workflow | PR-101 task spec; reproducible checkout, branch, diff and comparison commands below |
| Regression tests | `tests/test_invoice.py` |
| Independent benchmark tests | `tests/test_eval_engine.py` and 10 literal expected-output fixtures |
| CI as code | `.github/workflows/applied-engineer-evaluations.yml` in repository root |
| Runtime/environment evidence | `scripts/repository_audit.py` records Git SHA, module inventory, test paths and workflow presence |
| Archived machine-readable evidence | GitHub Actions uploads `artifacts/benchmark-results.json` and `artifacts/repository-audit.json` |

## Reproduce on a clean checkout

```bash
git clone https://github.com/bircanuzan/AI-in-HR-Portfolio.git
cd AI-in-HR-Portfolio
git log -5 --oneline -- "Applied Engineer - Evaluations Role"
git diff --stat HEAD~1..HEAD -- "Applied Engineer - Evaluations Role"
bash "Applied Engineer - Evaluations Role/scripts/ci.sh"
```

GitHub Actions runs Python 3.11 and 3.12, compiles modules, executes unit and edge-case tests, runs the three-candidate benchmark, emits JSON evidence and uploads artifacts. **A workflow file is not proof of a passing run**; inspect the live Actions status and downloadable artifacts.

## Representative branch/PR process (documented procedure, not a claim it was performed)

```bash
git switch -c eval/pr101-discount-regression
# Change implementation, tests and case fixtures as needed.
python -m unittest discover -s tests -v
git diff --check
git add "Applied Engineer - Evaluations Role"
git commit -m "test: add PR-101 regression evidence"
git push -u origin eval/pr101-discount-regression
# Open a PR; require green CI and reviewer sign-off before merge.
```

## Production-grade gaps and next evidence milestones

1. Evaluate a substantial, **public and licensed** multi-package codebase; record its real commit SHA, dependency lockfile, dependency graph, test commands and PR diff.
2. Capture a genuine branch, pull-request review, required status check and merge record (none asserted here).
3. Expand beyond `unittest` to integration tests, static analysis, mutation testing and flaky-test triage where appropriate.
4. Run actual external model-generated patches inside a sandbox with no secrets or outbound network access; retain source-to-result provenance.
5. Verify CI green status in GitHub's Actions UI before quoting a successful run or its test count on a CV.

These explicit gaps prevent a small, sound demonstration from being misrepresented as enterprise-scale production engineering.
