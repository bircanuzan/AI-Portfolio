# Turkish Language AI Evaluator

**Independent, reproducible portfolio demonstration | Turkish-language AI content evaluation, factuality, message drift & cultural nuance**

This project operationalizes a multilingual AI evaluation role focused on assessing the coherence, accuracy, relevance, tone, and cultural appropriateness of Turkish-language AI-generated content. It also covers detecting unsupported claims, content drift and mismatches between a supplied visual description and text. **The demo uses synthetic inputs only, is not a commissioned client project, and does not claim any model benchmark results.**

## Role-aligned client requirements
- Review AI-generated Turkish text for fluency, grammar, coherence, naturalness, tone and cultural nuance.
- Detect **message drift**: intent deviation, omission, unwarranted additions, inconsistent persona, or response to the wrong instruction.
- Identify **hallucinations**: unsupported factual claims, internally contradictory statements, invented product details and unrealistic descriptions.
- Review **visual-attribute consistency** when textual image metadata is supplied, without claiming to perform image recognition.
- Document structured error labels, severity and explanations that model trainers can act on.
- Apply annotation guidelines consistently and route ambiguous or high-impact cases to a human adjudicator.
- Support short-turnaround remote contract QA with reproducible, privacy-conscious records.

## Project files
- [evaluation_rubric.md](evaluation_rubric.md): operational taxonomy, scoring anchors, review/acceptance criteria and proposed KPIs.
- [data/synthetic_turkish_evaluations.jsonl](data/synthetic_turkish_evaluations.jsonl): synthetic Turkish prompts/responses and human-entered evaluation judgments, including a visual-description scenario.
- [evaluate.py](evaluate.py): dependency-free Python validation and QA summary of **human-supplied** annotations.
- [tests/test_evaluate.py](tests/test_evaluate.py): unit tests for input quality, scoring logic, and disagreement handling.

## Skills and techniques
Native Turkish language analysis; Turkish/English language comparison; prompt-response alignment; factuality/groundedness verification; error taxonomy design; hallucination and message-drift categorization; cultural localization; structured annotation; rubric calibration; cross-review and human-in-the-loop adjudication; Python, JSONL, QA reporting.

## Methodology
1. **Task intake:** Define target instruction, evidence available, target Turkish audience and any visual-attribute metadata.
2. **Prepare samples:** Separate the source prompt, candidate AI response, evidence source and annotation context.
3. **Evaluate human judgments:** Rate instruction alignment, coherence, groundedness, Turkish naturalness, and cultural appropriateness on a 0–3 scale.
4. **Classify issues:** Record `message_drift`, `unsupported_claim`, `visual_attribute_mismatch`, `contradiction`, `fluency`, `tone_cultural_nuance` or `other`, with explanations.
5. **Escalate:** Flag severe/unsupported claims, conflicts between raters and missing evidence for a second review.
6. **Deliver feedback:** Summarize error prevalence, score distribution, actionable annotations and release-blocking findings.

## Run
Python 3.10+; no third-party dependencies.
```bash
cd "AI Portfolio/Natural Language Processing (NLP)/Turkish Language AI Evaluator"
python evaluate.py --input data/synthetic_turkish_evaluations.jsonl --output reports/qa_report.json
python -m unittest discover -s tests -v
```

## Evidence boundaries
This is a **synthetic, manually labeled example** designed to demonstrate workflow, judgment criteria, and report generation. The Python script validates and aggregates human ratings; it **does not automatically understand Turkish semantics, verify external facts, inspect images, or score an LLM**. KPIs in the rubric are proposed targets, not verified service levels. Named companies, customers and real-world deployments are deliberately excluded.
