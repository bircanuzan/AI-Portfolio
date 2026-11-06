# Member of Technical Staff, Research Engineering | Toy RL Environment & Evaluation Harness

**Status:** Independent teaching-scale tabular Q-learning sample. This is not a claim of professional RL research, large-scale model training, production infrastructure or open-source LLM fine-tuning.

## Environment
Finite 1D grid (5 positions). State=position; actions=left/right; terminal reward=1 at the goal, per-step penalty=-0.01. Q-learning updates a state/action table. Fixed RNG seed supports repeatability.

**Files:** toy_rl.py, TASK_AND_ACCEPTANCE.md.

**Run:** `python toy_rl.py`. Demonstrates environment contract, reward calculation, episode reset, deterministic evaluation and success metrics with standard-library Python.

**Next research extensions (not implemented):** partial observability, richer action spaces, human feedback, reward-model evaluation, distributed rollout and production benchmarking.