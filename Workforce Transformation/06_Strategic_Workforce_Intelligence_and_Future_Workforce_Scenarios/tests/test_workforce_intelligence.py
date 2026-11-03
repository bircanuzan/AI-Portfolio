import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from forecast_scenarios import estimate, run as forecast_run
from skills_gap import rank_gap, run as skills_run

def row(**updates):
    x = dict(year="2027", function="Test", monthly_cases="600", minutes_per_case="20",
             assistable_share="0.5", minutes_saved_per_assisted_case="10",
             review_minutes_per_assisted_case="3", productive_hours_per_fte="120",
             available_fte="2")
    x.update(updates)
    return x

class PlanningTests(unittest.TestCase):
    def test_baseline_exceeds_assisted_when_net_time_positive(self):
        self.assertGreater(estimate(row(), enable_assistance=False)["scenario_fte"],
                           estimate(row())["scenario_fte"])
    def test_no_assistance_equals_baseline(self):
        r = estimate(row(), enable_assistance=False)
        self.assertEqual(r["baseline_fte"], r["scenario_fte"])
    def test_increased_demand_increases_need(self):
        self.assertGreater(estimate(row(), 1.2)["scenario_fte"], estimate(row())["scenario_fte"])
    def test_review_cost_cannot_be_ignored(self):
        self.assertGreater(estimate(row(review_minutes_per_assisted_case="9"))["scenario_fte"],
                           estimate(row(review_minutes_per_assisted_case="1"))["scenario_fte"])
    def test_bad_eligibility(self):
        with self.assertRaises(ValueError):
            estimate(row(assistable_share="1.5"))
    def test_bad_capacity(self):
        with self.assertRaises(ValueError):
            estimate(row(productive_hours_per_fte="0"))
    def test_failed_assistance_not_assumed_successful(self):
        r_high = estimate(row(assistance_success_rate="0.9"))
        r_low = estimate(row(assistance_success_rate="0.1"))
        self.assertLess(r_high["scenario_fte"], r_low["scenario_fte"])
    def test_zero_success_can_add_review_overhead(self):
        r = estimate(row(assistance_success_rate="0"))
        self.assertGreater(r["scenario_fte"], r["baseline_fte"])
    def test_invalid_success_rate(self):
        with self.assertRaises(ValueError):
            estimate(row(assistance_success_rate="1.2"))
    def test_scenario_rows(self):
        self.assertEqual(len(forecast_run()), 9)
    def test_skills_priority(self):
        v = rank_gap(dict(capability="Agent", role_group="Ops", required_proficiency="4",
                          current_aggregate_proficiency="2", priority_weight="5"))
        self.assertEqual(v["illustrative_priority"], 10)
    def test_invalid_skills(self):
        with self.assertRaises(ValueError):
            rank_gap(dict(capability="A", role_group="B", required_proficiency="9",
                          current_aggregate_proficiency="2", priority_weight="5"))
    def test_skills_dataset(self):
        self.assertEqual(len(skills_run()), 7)

if __name__ == "__main__":
    unittest.main()