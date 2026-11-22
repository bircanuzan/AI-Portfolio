# AI Data Quality / Training Dataset Specialist

**Project:** Quality-check a synthetic AI-training dataset for labeling errors, duplicates, schema problems, privacy-looking markers and split leakage.

**Evidence status:** Independent synthetic educational demonstration. No real client, deployed model, trained production system, or commercial result is claimed. **Deliverable:** Runnable synthetic quality/assurance demonstration, not a live model test.

## Fictional business / client requirement

Quality-check a synthetic AI-training dataset for labeling errors, duplicates, schema problems, privacy-looking markers and split leakage. A team needs an auditable and repeatable decision process rather than untracked subjective opinions.

## Methodology

1. Define required fields, allowed labels and split policy.
2. Validate case IDs, text normalization, label distribution and exact duplicate content.
3. Check accidental cross-split overlap and marker-based sensitive-data risk; flag uncertain items.
4. Export a quarantine queue and clean-data report without silently changing source records.

## Skills and technology / AI stack

Python 3, JSONL, regular expressions, datasets/ETL quality assurance, labeling guidelines, dataset lineage; optional pandas/SQL.

## Evaluation metrics and acceptance evidence

Invalid row rate, duplicates, cross-split leakage, label mix, privacy flag rate and quarantine backlog. These are **metrics to measure**, not results already attained. All authored candidate answers, labels and traces are fixtures; no LLM API generation is claimed.

## Portfolio deliverables

- `audit_dataset.py` — runnable synthetic quality/assurance demonstration, not a live model test
- `cases.jsonl` — entirely synthetic scenarios, annotations, traces or evaluation examples
- `README.md` — business requirement, workflow, measurable indicators, and limitations

**Run:** Python 3.10+, from this directory: `python audit_dataset.py`. Project 08's full LoRA training requires optional packages and model weights.

## Commercial relevance / interview framing

This project showcases the *methods* used in **AI Data Quality / Training Dataset Specialist** positions. To describe real work accurately, distinguish a portfolio exercise from professional assignments; only claim real-world outcomes when independent evidence exists.

[All 8 role tracks](../) · [AI Portfolio](../../)
