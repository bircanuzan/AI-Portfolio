# Project 1 — Supervised Fine-Tuning (SFT) with LoRA

**Portfolio type:** independent learning / reference implementation, using synthetic support requests. **Status:** code and training protocol provided; no claim that a model was trained, a GPU run completed, or accuracy improved. Not a commissioned client engagement.

## In plain English

Supervised fine-tuning (SFT) shows a pretrained language model examples of the right question-and-answer pairs, so it can learn a desired response format and behavior. In this fictional project an assistant should classify a customer-support message as `billing`, `technical`, or `unknown`, returning exactly `{"intent":"billing"}` (or the corresponding label). We fine-tune a small existing open-weight instruction model, **not** train a model from scratch.

**Why it matters to AI training jobs:** demonstrates data preparation, gold-standard answers, train/validation/test separation, model adaptation, evaluation design and reproducible training. Developing and executing such code is more advanced than human response-rating work.

## Business requirement and methodology

A fictional helpdesk needs reliable routing, consistent machine-readable outputs and escalation of out-of-scope queries. The design uses synthetic training pairs, a locked hold-out set, and a separately recorded baseline-versus-adapter comparison.

1. Validate synthetic JSONL rows and prevent exact-match leakage across the three sets.
2. Prepare the prompt with `<message>` and a reference JSON completion. Mask the prompt tokens from the supervised loss so training targets only the desired answer.
3. Start with `Qwen/Qwen2.5-0.5B-Instruct`, add LoRA adapters using **PEFT**, and train with the Hugging Face **Transformers Trainer** / **PyTorch**.
4. Compare the untouched base model with the fine-tuned adapter on the exact same held-out prompts.
5. Score exact-label accuracy and strict JSON-schema compliance, then inspect errors, bias, unsafe content, latency and regressions before any real deployment.

## Tools and skills demonstrated

Python, JSONL/JSON validation, dataset QA, train/validation/test leakage checks, PyTorch, Hugging Face Transformers, PEFT/LoRA, tokenization, instruction-style causal language modeling, loss masking, adapter checkpoints, evaluation, reproducibility and human-in-the-loop review.

LoRA updates small adapter matrices rather than all model parameters, lowering training memory and compute requirements. This is **supervised learning from gold answers**, not RLHF.

## Files

- `data/train.jsonl`, `data/validation.jsonl`, `data/test.jsonl` — entirely fictional message/label pairs
- `validate_data.py` — dependency-free QA and split-leakage checks
- `train_lora.py` — genuine optional Transformers/PEFT LoRA training script
- `evaluate_model.py` — compare base and adapted model output quality on held-out prompts
- `test_validate_data.py` — dependency-free unit tests
- `requirements.txt` — optional ML dependencies

## Reproduce

From this directory, Python 3.10+:

```bash
python validate_data.py
python -m unittest -v test_validate_data.py
# Optional: requires downloaded model weights, sufficient disk and compute (GPU preferred)
pip install -r requirements.txt
python train_lora.py --output-dir outputs/sft_adapter
python evaluate_model.py --adapter outputs/sft_adapter --output outputs/eval.json
```

The model download can be large, a CPU run can be slow, and dependencies may need environment-specific adjustment. No cloud credentials are included. Keep generated model weights and private data out of GitHub.

## KPIs / evidence boundaries

**Proposed metrics (not achieved claims):** exact intent accuracy, strict JSON validity, unknown-class recall, regression count, training loss, inference latency and cost per 1,000 classifications. No before/after uplift or project ROI is asserted until the scripts are executed and results recorded. Dataset examples are synthetic; they do not establish production generalization.

## Professional narrative

**Client requirement:** fictional consistent support intent routing. **Method:** baseline, curated answer pairs, LoRA adaptation, locked holdout comparison. **Technology:** Python, PyTorch, Hugging Face Transformers, PEFT, JSON. **Result:** reproducible code and a verification protocol; model performance not yet established. **Risks:** overfitting, leakage, unsafe downstream automation, language coverage, privacy, and model license/compliance checks.

See companion [Project 2 — RLHF preference optimization](../02_RLHF_Preference_Feedback_Demo/) to understand the difference between training from correct answers and training from ranked answers.
