# Prompt Engineering — Measurable System-Prompt Regression

**Role aligned:** MacroCoderz Prompt Engineer, worldwide remote, https://macrocoderz.com/careers/prompt-engineer . **Synthetic educational demo**: example responses are manually authored fixtures, not captured LLM outputs and not model-performance claims.

## Scenario
Build and compare versioned instructions for a safe HR-policy assistant, including citation requirements, unknown questions, privacy, tool use, agent escalation and prompt injection. Define expected behavior before changing prompts and keep a regression suite.

## Tech + JD skills
System prompt design, tool descriptions, JSON output formats, evaluation dataset design, counterexamples and edge cases, Python scoring, error taxonomy, manual annotation, regression and model comparison, readable handover documentation. Optional future integrations: promptfoo or LangSmith; not implemented.

## Files
- PROMPT_VERSIONS.md — system prompts v1/v2 and change rationale
- eval_set.json — synthetic input/expected behavior, sensitive/edge cases
- demo_responses.json — illustrative test harness responses, *not* model output
- evaluate.py — deterministic coverage, decision and phrase checker
- test_evaluate.py — regression unit tests
- EXPERIMENT_PROTOCOL.md — real evidence capture, grading, version comparison

Run: `python evaluate.py --responses demo_responses.json` and `python -m unittest test_evaluate.py`. Standard library Python 3.10+. A green run proves **only** that fixtures match rules.

## Planned next evidence
Run both prompts against a genuine LLM with same model/settings and approved test context; capture exact response, model/date, latency, token use, tool actions and reviewer rubric; audit errors. Record before/after by case without making invented claims.
