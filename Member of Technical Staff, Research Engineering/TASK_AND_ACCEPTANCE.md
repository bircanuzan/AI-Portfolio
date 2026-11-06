# RL environment engineering task

**Specification**
- Environment exposes `step(state, action) -> (next_state, reward, done)`.
- Reset starts at 0; terminal goal is state 4; max episode length=20.
- Reward is +1 on reaching goal and -0.01 otherwise.
- Training uses tabular Q-learning with fixed seed and 500 episodes.
- Evaluation executes greedy policy; report final trace and number of steps.

**Acceptance checks**
1. Position never outside 0..4.
2. Terminal reward is exactly 1.
3. Seeded runs produce the same Q table.
4. Evaluate returns an explicit success flag and a trace.
5. Reward hacking, reproducibility and overfitting risks are documented.

This demonstrator cannot substitute for the role's required deep RL/ML engineering track record.