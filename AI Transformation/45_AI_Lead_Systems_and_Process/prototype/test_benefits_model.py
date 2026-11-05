import unittest
from benefits_model import evaluate


class BenefitsTests(unittest.TestCase):
    def test_base_case(self):
        actual = evaluate()
        self.assertEqual(actual["hours_released_monthly"], 75)
        self.assertEqual(actual["net_monthly_aed"], 5000)
        self.assertEqual(actual["simple_payback_months"], 8.4)
        self.assertEqual(actual["year_one_net_aed"], 18000)

    def test_sensitivity(self):
        actual = evaluate(realization=0.6)
        self.assertEqual(actual["net_monthly_aed"], 2000)
        self.assertEqual(actual["simple_payback_months"], 21)
        self.assertEqual(actual["year_one_net_aed"], -18000)

    def test_invalid_realization(self):
        with self.assertRaises(ValueError):
            evaluate(realization=1.2)


if __name__ == "__main__":
    unittest.main()
