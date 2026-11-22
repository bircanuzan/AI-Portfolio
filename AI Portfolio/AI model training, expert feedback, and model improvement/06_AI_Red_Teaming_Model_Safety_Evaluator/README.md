# AI Red Teaming / Model Safety Evaluator

**Project:** Probe a fictional enterprise assistant with benign, safety-focused adversarial cases such as role spoofing and requests to expose restricted HR information.

**Evidence status:** Independent synthetic educational demonstration. No real client, deployed model, trained production system, or commercial result is claimed. **Deliverable:** Runnable synthetic quality/assurance demonstration, not a live model test.

## Fictional business / client requirement

Probe a fictional enterprise assistant with benign, safety-focused adversarial cases such as role spoofing and requests to expose restricted HR information. A team needs an auditable and repeatable decision process rather than untracked subjective opinions.

## Methodology

1. Create a threat taxonomy and expected safe handling behavior.
2. Design synthetic prompt-injection and sensitive-information boundary tests.
3. Score authored example responses for refusal appropriateness, information leakage and groundedness.
4. Record false refusals and escalate severe failures to humans; propose remediation retesting.

## Skills and technology / AI stack

Python 3, JSONL, adversarial testing, prompt-injection taxonomy, OWASP LLM risk concepts, audit trail, safe completion rubrics.

## Evaluation metrics and acceptance evidence

Boundary violation count, unsafe compliance rate, refusal accuracy, severe-finding count and regression status. These are **metrics to measure**, not results already attained. All authored candidate answers, labels and traces are fixtures; no LLM API generation is claimed.

## Portfolio deliverables

- `safety_review.py` — runnable synthetic quality/assurance demonstration, not a live model test
- `cases.jsonl` — entirely synthetic scenarios, annotations, traces or evaluation examples
- `README.md` — business requirement, workflow, measurable indicators, and limitations

**Run:** Python 3.10+, from this directory: `python safety_review.py`. Project 08's full LoRA training requires optional packages and model weights.

## Commercial relevance / interview framing

This project showcases the *methods* used in **AI Red Teaming / Model Safety Evaluator** positions. To describe real work accurately, distinguish a portfolio exercise from professional assignments; only claim real-world outcomes when independent evidence exists.

[All 8 role tracks](../) · [AI Portfolio](../../)
