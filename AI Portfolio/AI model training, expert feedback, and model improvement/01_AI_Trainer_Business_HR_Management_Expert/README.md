# AI Trainer — Business, HR & Management Expert

**Project:** Evaluate an AI assistant answering fictional employee questions on hiring, organization design, change management and responsible HR processes.

**Evidence status:** Independent synthetic educational demonstration. No real client, deployed model, trained production system, or commercial result is claimed. **Deliverable:** Runnable synthetic quality/assurance demonstration, not a live model test.

## Fictional business / client requirement

Evaluate an AI assistant answering fictional employee questions on hiring, organization design, change management and responsible HR processes. A team needs an auditable and repeatable decision process rather than untracked subjective opinions.

## Methodology

1. Write realistic domain-expert prompts and gold-standard reasoning checkpoints.
2. Review two response candidates for correctness, ethical boundaries, practical utility and appropriate human escalation.
3. Score with an anchored 0–2 rubric, document error categories and rewrite an improved answer.
4. Audit the rubric for consistency across cases and report disagreements.

## Skills and technology / AI stack

Python 3, JSONL, HR process knowledge, structured rubrics, domain SME review, prompt engineering, human-in-the-loop escalation; optional LLM API for future real-model comparisons.

## Evaluation metrics and acceptance evidence

Case coverage, category-level rubric averages, grounded-answer rate, escalation appropriateness, reviewer agreement. These are **metrics to measure**, not results already attained. All authored candidate answers, labels and traces are fixtures; no LLM API generation is claimed.

## Portfolio deliverables

- `evaluate_domain.py` — runnable synthetic quality/assurance demonstration, not a live model test
- `cases.jsonl` — entirely synthetic scenarios, annotations, traces or evaluation examples
- `README.md` — business requirement, workflow, measurable indicators, and limitations

**Run:** Python 3.10+, from this directory: `python evaluate_domain.py`. Project 08's full LoRA training requires optional packages and model weights.

## Commercial relevance / interview framing

This project showcases the *methods* used in **AI Trainer — Business, HR & Management Expert** positions. To describe real work accurately, distinguish a portfolio exercise from professional assignments; only claim real-world outcomes when independent evidence exists.

[All 8 role tracks](../) · [AI Portfolio](../../)
