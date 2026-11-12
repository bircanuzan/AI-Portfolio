# AI Trainer - Remote | Generalist AI Data Quality Lab

> **Portfolio status:** Independent, synthetic demonstration. No confidential information, employer/client work, actual model-training delivery or production deployment is claimed. All records and ratings are invented to exercise the methodology.


## Business problem
A generalist AI-data team must consistently review content from different domains, annotate errors, and deliver helpful written feedback while working asynchronously.

## Demonstrator scope
1. **Task intake** — capture request, topic, reference evidence, rubric version, annotation owner and priority.
2. **Response quality review** — assess factual support, relevance, coherence and adherence to instructions on a 0-4 anchored scale.
3. **Data annotation** — assign one or more categories: `fact_error`, `irrelevant`, `ambiguous`, `incoherent`, `instruction_failure`, `missing_evidence`, `acceptable`.
4. **Human feedback** — record an explanation grounded in the response and an actionable revision suggestion.
5. **Independent remote execution** — validate file formats, support a second review and retain review timestamps and rubric versions.
6. **Quality assurance** — route critical factual errors to a second human reviewer; report agreement and percentage of records needing correction.

## Worked sample
Synthetic case G-01 asks for a 2026 market-growth figure but provides no supporting source. The sample model answer invents a precise number. Reviewers flag `missing_evidence`, score factual support 0/4 and recommend withholding a numeric claim until a source is supplied.

## Evidence / files
- `rubric.md`: score anchors, decision rules, failure labels, feedback standard.
- `data/sample_reviews.json`: synthetic human review records across business and HR.
- `src/quality_gate.py`: read and validate annotations, calculate weighted ratings and reviewer disposition.
- `tests/test_quality_gate.py`: local regression examples.

## Acceptance criteria
Every completed record has five explicit scores, identifiable reviewer feedback, traceable task ID, source context, rubric version and human escalation for factual score zero. Evaluation is offline, does not call an LLM, and does not claim to verify external facts automatically.

## Run
```bash
python -m unittest discover -s "AI Model Training & Evaluation Freelancer Project/AI Trainer - Remote/tests"
python "AI Model Training & Evaluation Freelancer Project/AI Trainer - Remote/src/quality_gate.py" "AI Model Training & Evaluation Freelancer Project/AI Trainer - Remote/data/sample_reviews.json"
```
