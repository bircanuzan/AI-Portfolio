# Learning and deployment roadmap

These are practical estimates for someone with evaluation experience and basic Python, studying about 8–10 focused hours per week. They are not course durations or a hiring guarantee. Stages overlap; stronger coding foundations may take longer.

| Skill | Difficulty | Suggested practice | Evidence to retain |
|---|---|---|---|
| Python/SQL engineering | Moderate | 2–4 weeks strengthening modules, exceptions, types, SQL, tests and debugging | A service you can explain, modify and debug yourself |
| PyTorch and Hugging Face | Moderate to hard | 3–6 weeks learning tensors, autograd, tokenization, attention, training loops and generation | Reproducible small-model experiment, dependency versions and error analysis |
| SFT and LoRA | Moderate to hard after foundations | 2–4 additional weeks preparing instruction/response data, masking prompt loss, configuring adapters and checking overfitting | Base versus adapted model on a locked held-out dataset; adapter configuration and training logs |
| FastAPI, Docker and Linux | Moderate | 2–4 weeks serving typed requests, handling errors, containerizing and health checking | Local integration tests and documented startup/recovery |
| GPU serving, vLLM and optimisation | Harder | 4–8 additional weeks of practical experiments; hardware access required for GPU evidence | Hardware/model versions, p50/p95 latency, tokens/sec, peak memory and error rate under defined load |
| Production monitoring and rollbacks | Hard; develops through operational practice | Ongoing beyond tutorials | Reproducible failure drills, approved release bundles and verified recovery logs |

A first credible end-to-end prototype may take roughly 2–4 months; independent production readiness usually requires substantially more practice. Avoid equating a completed tutorial with production proficiency.

## Stage 1: Data, evaluation and prompt baseline

Extend the synthetic corpus to cover paraphrases, misspellings, multilingual messages, ambiguous requests and adversarial instructions. Document annotation rules and disagreements. Keep source/customer groups in one partition; detect exact and near duplicates. Run real model outputs through the scorer and retain failures. Add human rubric scores on a 1–5 scale for helpfulness and groundedness, with privacy and safety flags. Report per-intent quality, confusion matrix and uncertainty rather than relying on a single aggregate accuracy.

## Stage 2: Transformer and SFT/LoRA experiment

Start with a small, licensed pretrained model and learn tokenization, attention masks, padding, loss, gradients, training versus evaluation mode and generation settings. SFT teaches the model using input/desired-output pairs. LoRA trains a smaller set of added adapter parameters instead of updating all base parameters. They can be used together.

Use Hugging Face Transformers with PyTorch and PEFT. Confirm architecture-specific target modules; split before preprocessing; train only on training examples; mask prompt/padding tokens where appropriate. Track seed, model revision, dependency versions, hyperparameters and hardware. Compare prompt-only and adapted outputs on identical held-out cases. Measure regressions as well as improvements. Do not publish quality gains until the training and evaluation actually run.

## Stage 3: API and serving design

Proposed request: POST `/classify` with a bounded text field and a request ID. Proposed response: validated intent plus model/prompt version. Reject malformed/oversized requests, set timeouts, cap generated tokens and map upstream failures to explicit errors. Add `/health` and `/ready` endpoints. Keep API secrets outside code. Implement logging that omits raw support messages by default. FastAPI and Docker are future additions to this lab.

For vLLM, follow the official installation and hardware compatibility guidance and begin on an isolated development host. Keep any development endpoint on loopback or a private network. An unauthenticated public endpoint is not an acceptable deployment. No GPU resources have been provisioned or paid compute authorized by this project.

Compare serving configurations at fixed model quality, input/output lengths and concurrency. Record cold/warm behavior, hardware, p50/p95 latency, throughput, peak GPU memory, timeouts and error rates. Derive cost per 1,000 successful requests only from actual measured runtime and known prices. A faster configuration that breaks quality limits should not be selected.

## Stage 4: Monitoring and rollback drill

1. Version the model, adapter, tokenizer, prompt, configuration and container as one release bundle; retain the previous approved bundle.
2. Run schema, intent, privacy and operational checks before staging.
3. Inject controlled development failures: invalid outputs, model timeout, missing adapter and unavailable serving process.
4. On agreed regression thresholds, stop promotion or route traffic to the prior approved bundle. Human approval controls production changes.
5. Verify readiness and repeat the locked evaluation after restoring the bundle. Record detection and recovery times from the drill, clearly labeled as development measurements.

No production incident or rollback has been executed here. Production experience requires real operational ownership and review.

## Optional recommendation-system extension

Build an introductory content-based FAQ recommender using public/synthetic documents and embeddings. Separate training and evaluation queries, compare against a keyword baseline and report Recall@k with manually checked relevance judgments. This is planned and separate from the current intent-scoring harness.

## Official learning references

- [PyTorch basics](https://pytorch.org/tutorials/beginner/basics/intro.html)
- [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)
- [PEFT and LoRA quicktour](https://huggingface.co/docs/peft/quicktour)
- [vLLM quickstart](https://docs.vllm.ai/en/stable/getting_started/quickstart/)
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)

Software interfaces change. Confirm documentation and compatible versions when implementing each stage; the current project deliberately requires only Python's standard library.
