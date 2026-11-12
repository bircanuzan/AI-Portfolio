# Reproducible ML engineering task

**Challenge:** implement reproducible fitting/inference for synthetic y = 2x + 0.5 + Gaussian noise, with fixed train/validation split.

**Acceptance criteria**
1. Same seed produces identical synthetic dataset and fitted parameters.
2. Train/validation errors are calculated independently; validation samples never update weights.
3. Prediction remains numerically finite; invalid zero-length dataset needs validation if code is extended.
4. Report weight, bias, train MSE, validation MSE, steps and learning rate.
5. Performance claims must include hardware, sample sizes, environment and repeat runs, none of which are asserted here.

**Failure prompts for AI coding agents:** inadvertently leak validation data, omit seed, ignore noise distribution, create unstable update rule, miscompute MSE, confuse fit with inference.

**Evidence limits:** tiny educational model with no external dataset, advanced fine-tuning, graduate research output or performance tuning.