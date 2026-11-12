# Task Specification & Acceptance Criteria
**Simulation, not a live micro1 task.**

## Research task
Build a 4x4 self-contained deterministic RL navigation environment with two impassable walls, four discrete actions, a terminal goal, 30-step horizon, bounded rewards, seeded Q-learning and a structured training/evaluation workflow.

## Operational acceptance
1. Environment rejects unknown actions and steps after an episode ends.
2. Boundary and wall actions do not move to an invalid state and carry -0.10 reward.
3. Terminal goal returns +1 exactly once; nonterminal step is -0.02; truncation is -0.30.
4. Same-seed training returns identical Q tables and metrics.
5. Synthetic JSONL episode verifier catches rewards that do not match the state transition and any post-terminal record.
6. Evaluator tests four starts using fixed sample count (25 per start); each benchmark policy reports successes, average steps, total episodes and verifier coverage.
7. Test report includes failed test count, run parameters, seed, runtime environment and known limits.

## Measured demonstration
Reference local execution: 12/12 automated tests passed, Q-learning 100/100 success and random policy 48/100, 20/20 synthetic episodes verified. These values describe only the toy task.

## Failure taxonomy
Invalid action; out-of-bounds transition; wall penetration; reward hacking; duplicate terminal payout; post-terminal continuation; nonreproducible random seed; partial episode; train/test leakage; missing source data.

## Quality targets / SLAs (proposed only)
0 integrity failures; 100% replay-verifiable training samples; complete manifest on every run; critical defects block release. No contracted client SLA, training throughput target, or production result is claimed.

## Research limitations
Tabular Q-learning is not deep RL. No GPU implementation, neural fine-tuning, open-source model checkpoint, distributed training, simulator integration or research paper is included.