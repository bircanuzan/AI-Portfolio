# Coding-Agent PR Regression Benchmark

An **independent, synthetic Python evaluation laboratory** for evaluating code changes against a pull-request-style task. It is not a contribution to an external open-source project or an evaluation of real Claude Code/Codex sessions.

## PR-202: strict environment configuration parser

A fictional PR requires a parser to:
- ignore blank lines and whole-line comments;
- split on the **first** equals sign, allowing additional equals signs in values;
- validate uppercase configuration keys;
- reject duplicate keys and invalid assignments;
- keep deterministic results across runs.

The lab includes the correct reference implementation plus two intentionally flawed candidate patches. The executable benchmark compares each candidate against specification-derived fixtures and reports case-by-case evidence.

## Run

```bash
cd Coding-Agent-PR-Regression-Benchmark
python -m unittest discover -s tests -v
python benchmark.py
```

Python 3.10+ standard library only. All cases are **authored synthetic fixtures**, not evidence from frontier coding-agent runs.

## Files

- `config_parser.py`: reference implementation.
- `candidate_patches.py`: two faulty change candidates.
- `benchmark.py`: reproducible behavioral comparison and JSON output.
- `tests/test_benchmark.py`: unit, edge-case and regression assertions.
- `../.github/workflows/coding-agent-evaluation-labs.yml`: CI configuration.

## Evaluation principles

The task specification defines behavior independently of any candidate. A fixed oracle tests functionality, invalid inputs, and corner cases; failures include expected-versus-observed evidence. The reference is treated as a validation control. No production codebase ownership, real pull-request acceptance, third-party model comparison or passing CI status is implied by this README.
