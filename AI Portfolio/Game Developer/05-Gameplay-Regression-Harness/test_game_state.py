import unittest
from game_state import TokenGame

class TokenTests(unittest.TestCase):
    def test_hold_counts_once(self):
        game=TokenGame()
        for _ in range(20): game.advance(True)
        self.assertEqual(game.count,1)

    def test_three_distinct_presses(self):
        game=TokenGame()
        for _ in range(3):
            game.advance(True); game.advance(False)
        self.assertEqual(game.count,3)
        self.assertTrue(game.complete)

    def test_no_overshoot(self):
        game=TokenGame()
        for _ in range(10):
            game.advance(True); game.advance(False)
        self.assertEqual(game.count,3)

if __name__ == "__main__":
    unittest.main()
