# SFT / LLM Fine-Tuning Engineer

**Project:** Adapt a small pretrained language model to produce strict JSON support-intent labels using supervised examples, with a baseline-versus-adapter comparison.

**Evidence status:** Independent synthetic educational demonstration. No real client, deployed model, trained production system, or commercial result is claimed. **Deliverable:** Real optional LoRA fine-tuning example (requires ML dependencies); dataset and checks supplied.

## Fictional business / client requirement

Adapt a small pretrained language model to produce strict JSON support-intent labels using supervised examples, with a baseline-versus-adapter comparison. A team needs an auditable and repeatable decision process rather than untracked subjective opinions.

## Methodology

1. Build synthetic gold-answer pairs with separate train, validation and locked test sets.
2. Validate class labels and exact leakage before training.
3. Tokenize prompt/target examples and mask prompt tokens from SFT loss.
4. Optionally train LoRA adapters using PEFT/Transformers, then evaluate actual generations on the held-out test split.

## Skills and technology / AI stack

Python, JSONL, PyTorch, Hugging Face Transformers, PEFT/LoRA, tokenization, training loss masking, GPU/CPU evaluation, reproducibility.

## Evaluation metrics and acceptance evidence

Exact intent accuracy, JSON-schema validity, unknown-label recall, training cost and latency; no claimed results until run. These are **metrics to measure**, not results already attained. All authored candidate answers, labels and traces are fixtures; no LLM API generation is claimed.

## Portfolio deliverables

- `train_lora.py` — real optional lora fine-tuning example (requires ml dependencies); dataset and checks supplied
- `data/train.jsonl`, `data/validation.jsonl`, `data/test.jsonl` — synthetic support-intent examples, with a locked test split
- `README.md` — business requirement, workflow, measurable indicators, and limitations

**Run:** Python 3.10+, from this directory: `python train_lora.py`. Project 08's full LoRA training requires optional packages and model weights.

## Commercial relevance / interview framing

This project showcases the *methods* used in **SFT / LLM Fine-Tuning Engineer** positions. To describe real work accurately, distinguish a portfolio exercise from professional assignments; only claim real-world outcomes when independent evidence exists.

[All 8 role tracks](../) · [AI Portfolio](../../)

**Companion full SFT implementation:** [NLP Engineering — SFT/LoRA lab](../../NLP%20Engineering/01_SFT_LoRA_Model_Adaptation/) includes optional PyTorch/Transformers/PEFT training and baseline-versus-adapter test scripts.
