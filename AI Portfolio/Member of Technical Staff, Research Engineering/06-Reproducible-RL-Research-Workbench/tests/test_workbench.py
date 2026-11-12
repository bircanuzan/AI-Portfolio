"""Deterministic environment, pipeline and training-quality assertions."""
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from environment import ACTIONS, GridWorld, STARTS
from pipeline import make_episode, verify_episode, sha256
from training import train, greedy
from benchmark import benchmark


class EnvironmentTests(unittest.TestCase):
    def test_out_of_bounds_penalty(self):
        env=GridWorld(); env.reset((0,0)); t=env.step('left')
        self.assertTrue(t.invalid); self.assertEqual(t.next_state,(0,0)); self.assertEqual(t.reward,-.10)
    def test_wall_blocking(self):
        env=GridWorld(); env.reset((0,1)); t=env.step('right')
        self.assertTrue(t.invalid); self.assertEqual(t.next_state,(0,1))
    def test_terminal_reward_and_lock(self):
        env=GridWorld(); env.reset((3,2)); t=env.step('down')
        self.assertTrue(t.terminated); self.assertEqual(t.reward,1.0)
        with self.assertRaises(RuntimeError):env.step('down')
    def test_timeout(self):
        env=GridWorld(horizon=1); env.reset((0,0)); t=env.step('right')
        self.assertTrue(t.truncated); self.assertEqual(t.reward,-.30)
    def test_invalid_action(self):
        env=GridWorld(); env.reset((0,0))
        with self.assertRaises(ValueError):env.step('teleport')


class PipelineTests(unittest.TestCase):
    def test_replay_validation(self):
        rows=make_episode(2,seed=23)
        self.assertEqual(verify_episode(rows),(True,'verified'))
    def test_tampered_reward_fails(self):
        rows=make_episode(0,seed=25); rows[0]['reward']=42.0
        self.assertFalse(verify_episode(rows)[0])
    def test_repeatable_sha(self):
        self.assertEqual(sha256(make_episode(3,42)),sha256(make_episode(3,42)))
    def test_malformed_order_fails(self):
        rows=make_episode(1,42); rows[0]['step']=5
        self.assertFalse(verify_episode(rows)[0])


class TrainingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.q, cls.metrics=train()
    def test_train_determinism(self):
        q2,m2=train()
        self.assertEqual(self.q,q2); self.assertEqual(self.metrics,m2)
    def test_benchmark_verifier(self):
        results=benchmark(self.q,repeats=3)
        self.assertEqual(results['q_learning']['verification_rate'],1.0)
        self.assertEqual(results['random']['verification_rate'],1.0)
    def test_all_start_states(self):
        for pos in STARTS:
            rows=make_episode(7,51,policy=lambda state: greedy(self.q,state),start=pos)
            self.assertTrue(rows[-1]['terminated'],msg=str(pos))


if __name__=='__main__':unittest.main()
