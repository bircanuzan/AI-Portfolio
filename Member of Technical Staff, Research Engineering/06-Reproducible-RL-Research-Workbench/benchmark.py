"""Evaluate trained policy against seeded random policy without ungrounded claims."""
import random
from environment import ACTIONS, STARTS
from pipeline import make_episode, verify_episode
from training import greedy


def benchmark(q, repeats=25, seed=123):
    rng = random.Random(seed)
    counts = {'q_learning': {'successes': 0, 'steps': 0, 'episodes': 0, 'valid': 0},
              'random': {'successes': 0, 'steps': 0, 'episodes': 0, 'valid': 0}}
    for label in counts:
        for i in range(len(STARTS) * repeats):
            s = STARTS[i % len(STARTS)]
            policy = (lambda state: greedy(q, state)) if label == 'q_learning' else (lambda state: rng.choice(ACTIONS))
            rows = make_episode(i, seed + i, policy=policy, start=s)
            verified, _ = verify_episode(rows)
            counts[label]['valid'] += int(verified)
            counts[label]['episodes'] += 1
            counts[label]['successes'] += int(rows[-1]['terminated'])
            counts[label]['steps'] += len(rows)
    for v in counts.values():
        n = v['episodes']
        v['success_rate'] = round(v['successes'] / n, 3)
        v['avg_steps'] = round(v['steps'] / n, 2)
        v['verification_rate'] = round(v['valid'] / n, 3)
    return counts
