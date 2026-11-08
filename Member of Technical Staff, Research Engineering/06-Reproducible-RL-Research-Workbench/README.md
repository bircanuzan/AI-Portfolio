# Reproducible RL Research Workbench
**Category:** Independent educational research-engineering portfolio project | **Application alignment:** micro1 Member of Technical Staff, Research Engineering

> **Evidence boundary:** This is a small self-directed, locally executed *tabular Q-learning* experiment, not a commissioned client project, large-scale reinforcement-learning infrastructure, published external benchmark, or fine-tuning of a neural network or language model.

## Client Inquiry (simulated)
A research team needs a self-contained RL environment that can yield reproducible, inspectable training episodes. Each experiment should define a reward function and terminal-state rules, generate synthetic data, verify every event transition, train an agent, and compare its capability to a baseline. Research results must have clear reproducibility metadata and should not be presented as generalizable until independently evaluated.

## Our Methodology / Tech Used
1. **RL environment design:** `environment.py` defines a 4x4 grid, two walls, four discrete actions, four start states, 30-step episodes, reward +1 at terminal goal, invalid movement penalty -0.10, ordinary step -0.02 and timeout penalty -0.30.
2. **Reward functions, verifiers and regression:** `pipeline.py` independently replays trajectories, checks state/action/reward/termination/timeout consistency, and rejects corrupted or illegally sequenced records. Tests cover terminal lock and invalid boundaries.
3. **Reproducible training:** `training.py` performs seeded tabular Q-learning for 4,500 episodes with an explicit exploration schedule and Q-table.
4. **Synthetic data:** `run_experiment.py` generates 20 synthetic episodes in JSONL, a deterministic SHA-256 digest, and a structured metrics manifest.
5. **Benchmark:** `benchmark.py` tests both trained and random policies on the same four start states, 25 episodes per start; records success rate, average steps and replay verification.
6. **QA / release gates:** `tests/test_workbench.py` uses Python unittest to check rewards, determinism, illegal post-terminal steps, corruption detection and starting-state coverage.

**Actual tools:** Python 3, Python standard library, Q-learning, MDP-style state/action/reward design, JSONL, deterministic RNG seeds, SHA-256, unittest, reproducibility manifests and a command-line evaluation pipeline. This example does not use PyTorch or Ray RLlib and should not be described as such.

## Result (KPI / SLA / Metrics)
**Local reference run (8 Nov 2026, Python 3.13.5):**
- **12/12 automated tests passed**, zero failures.
- **4,500 training episodes**, 4,496 ended successfully (99.91% training completion in the synthetic environment).
- **Trained greedy policy: 100/100 successes**, average **3.50 steps**.
- **Random policy: 48/100 successes**, average **23.27 steps**.
- **20/20 synthetic episode logs replay-verified**, 70 total transitions with a SHA-256 dataset fingerprint.
- **100% recorded episode replay verification** for both benchmark policies.

**Research KPIs:** episode completion, sample validity, reward correctness, deterministic same-seed runs, replay verification, step efficiency and measured baseline comparison.

**Proposed QA service level (not an achieved customer SLA):** every release candidate should include machine-readable metrics, fixed-seed reproduction instructions and a reviewable incident log; critical state/reward integrity failures block publication.

**Interpretation and limitations:** results are from a tiny finite navigation toy that is intentionally easy to learn. They do *not* demonstrate frontier model performance, open-source RL model fine-tuning, distributed episode pipelines, downstream model improvement or a deployed training platform. No live customer data was used.

## Reproduce the reference run
Python 3.10+; no third-party packages required.

```bash
python -m unittest discover -s tests -v
python run_experiment.py
```

The run writes `results/metrics.json` and `results/episodes.jsonl`. The committed `results/metrics.json` records the tested reference output. Because Python and system versions may differ, explicitly compare output rather than assuming every environment is identical.

## Files
- `environment.py`: episode dynamics and reward contract
- `training.py`: seeded tabular Q-learning reference implementation
- `pipeline.py`: synthetic episode generator, replay verifier, fingerprinting
- `benchmark.py`: balanced trained/random evaluation
- `run_experiment.py`: reproducible CLI entry point
- `tests/test_workbench.py`: 12 local QA tests
- `results/metrics.json`: local reference metrics + synthetic dataset digest
- `TASK_SPEC_AND_ACCEPTANCE.md`: task, success criteria, failure categories and SLA targets

## Related portfolio
[Member of Technical Staff, Research Engineering: project collection](https://github.com/bircanuzan/AI-in-HR-Portfolio/tree/main/Member%20of%20Technical%20Staff%2C%20Research%20Engineering).