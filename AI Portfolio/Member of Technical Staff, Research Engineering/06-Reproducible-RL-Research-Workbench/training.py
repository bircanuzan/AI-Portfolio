"""Seeded tabular Q-learning training in a self-contained environment."""
import random
from environment import ACTIONS, STARTS, GridWorld


def greedy(q, state):
    # Tie order is explicit for reproducibility.
    return max(ACTIONS, key=lambda action: q.get((state, action), 0.0))


def train(seed=7, episodes=4500, alpha=0.22, gamma=0.94):
    rng = random.Random(seed)
    q = {}
    stats = {'episodes': episodes, 'terminal_successes': 0, 'total_steps': 0}
    env = GridWorld()
    for ep in range(episodes):
        state = env.reset(STARTS[ep % len(STARTS)])
        epsilon = max(0.04, 0.60 * (1.0 - ep / episodes))
        while True:
            action = rng.choice(ACTIONS) if rng.random() < epsilon else greedy(q, state)
            step = env.step(action)
            future = 0.0 if step.terminated or step.truncated else max(q.get((step.next_state, a), 0.0) for a in ACTIONS)
            old = q.get((state, action), 0.0)
            q[(state, action)] = old + alpha * (step.reward + gamma * future - old)
            state = step.next_state
            stats['total_steps'] += 1
            if step.terminated or step.truncated:
                stats['terminal_successes'] += int(step.terminated)
                break
    stats['training_success_rate'] = round(stats['terminal_successes'] / episodes, 4)
    return q, stats
