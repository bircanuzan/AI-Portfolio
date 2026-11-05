import unittest
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from train_model import prepare_data, train_and_evaluate

class MLTests(unittest.TestCase):
    def test_stratified_holdout(self):
        Xtr, Xte, ytr, yte = prepare_data()
        self.assertEqual(len(Xtr), 120)
        self.assertEqual(len(Xte), 30)
        self.assertEqual(set(ytr), set(yte))
    def test_training_and_persistence(self):
        with TemporaryDirectory() as root:
            result = train_and_evaluate(root)
            self.assertTrue((Path(root) / "iris_model.joblib").is_file())
            self.assertGreaterEqual(result["holdout_f1_macro"], 0)
            self.assertLessEqual(result["holdout_f1_macro"], 1)

if __name__ == "__main__":
    unittest.main()
