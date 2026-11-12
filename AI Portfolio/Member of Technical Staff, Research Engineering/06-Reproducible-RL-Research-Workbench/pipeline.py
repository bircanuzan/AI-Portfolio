"""Synthetic episode generation and independent replay-based QA/verifier."""
import hashlib
import json
import random
from environment import ACTIONS, GridWorld, STARTS


def make_episode(episode_id, seed, policy=None, start=None):
    rng = random.Random(seed)
    env = GridWorld()
    env.reset(start if start is not None else STARTS[episode_id % len(STARTS)])
    records = []
    while True:
        state = env.state
        action = policy(state) if policy else rng.choice(ACTIONS)
        t = env.step(action)
        records.append({'episode': episode_id, 'step': env.steps, 'state': list(t.state),
                        'action': t.action, 'next_state': list(t.next_state), 'reward': t.reward,
                        'terminated': t.terminated, 'truncated': t.truncated, 'invalid': t.invalid})
        if t.terminated or t.truncated:
            break
    return records


def verify_episode(rows):
    if not rows:
        return False, 'empty episode'
    env = GridWorld()
    env.reset(rows[0]['state'])
    seen_terminal = False
    for index, record in enumerate(rows, 1):
        if seen_terminal or record['step'] != index or tuple(record['state']) != env.state:
            return False, 'trajectory ordering or state mismatch'
        try:
            t = env.step(record['action'])
        except (RuntimeError, ValueError):
            return False, 'invalid action or illegal post-terminal step'
        expected = {'episode': rows[0]['episode'], 'step': index, 'state': list(t.state),
                    'action': t.action, 'next_state': list(t.next_state), 'reward': t.reward,
                    'terminated': t.terminated, 'truncated': t.truncated, 'invalid': t.invalid}
        if record != expected:
            return False, 'reward/state/terminal mismatch'
        seen_terminal = env.done
    return (seen_terminal, 'verified' if seen_terminal else 'missing terminal event')


def canonical_json(data):
    return json.dumps(data, sort_keys=True, separators=(',', ':'))


def sha256(records):
    return hashlib.sha256(('\n'.join(canonical_json(r) for r in records)+'\n').encode()).hexdigest()
