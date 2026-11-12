"""Dependency-free finite-horizon navigation environment for RL demonstrations."""
from dataclasses import dataclass

ACTIONS = ('up', 'down', 'left', 'right')
WALLS = {(1, 1), (2, 1)}
GOAL = (3, 3)
STARTS = ((0, 0), (0, 3), (3, 0), (2, 2))


@dataclass(frozen=True)
class Transition:
    state: tuple[int, int]
    action: str
    next_state: tuple[int, int]
    reward: float
    terminated: bool
    truncated: bool
    invalid: bool


class GridWorld:
    """4 x 4 grid. Invalid moves receive a fixed cost and keep position."""
    def __init__(self, horizon: int = 30):
        if horizon <= 0:
            raise ValueError('horizon must be positive')
        self.horizon = horizon
        self.reset()

    def reset(self, start=(0, 0)):
        start = tuple(start)
        if not self.valid(start) or start == GOAL:
            raise ValueError('invalid start state')
        self.state = start
        self.steps = 0
        self.done = False
        return self.state

    @staticmethod
    def valid(pos):
        return len(pos) == 2 and all(isinstance(v, int) for v in pos) and all(0 <= v < 4 for v in pos) and tuple(pos) not in WALLS

    def step(self, action):
        if self.done:
            raise RuntimeError('cannot step an ended episode')
        if action not in ACTIONS:
            raise ValueError('invalid action')
        prior = self.state
        dx, dy = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}[action]
        candidate = (prior[0] + dx, prior[1] + dy)
        invalid = not self.valid(candidate)
        if not invalid:
            self.state = candidate
        self.steps += 1
        terminated = self.state == GOAL
        truncated = self.steps >= self.horizon and not terminated
        reward = 1.0 if terminated else (-0.30 if truncated else (-0.10 if invalid else -0.02))
        self.done = terminated or truncated
        return Transition(prior, action, self.state, reward, terminated, truncated, invalid)
