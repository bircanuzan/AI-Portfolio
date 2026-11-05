"""Open-data machine-learning training lab; no deployment or client data."""
from pathlib import Path
import joblib
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

SEED = 42

def prepare_data():
    data = load_iris()
    return train_test_split(data.data, data.target,
                            test_size=0.20, stratify=data.target, random_state=SEED)

def train_and_evaluate(output_dir="artifacts"):
    X_train, X_test, y_train, y_test = prepare_data()
    models = {
        "baseline": DummyClassifier(strategy="most_frequent"),
        "pipeline": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=1000, random_state=SEED))
        ])
    }
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    scores = {name: float(cross_val_score(m, X_train, y_train, scoring="f1_macro", cv=cv).mean())
              for name, m in models.items()}
    winner = max(scores, key=scores.get)
    selected = models[winner].fit(X_train, y_train)
    predictions = selected.predict(X_test)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    artifact = output / "iris_model.joblib"
    joblib.dump(selected, artifact)
    assert len(joblib.load(artifact).predict(X_test)) == len(X_test)
    return {
        "best_model": winner,
        "cv_f1_macro": scores,
        "holdout_f1_macro": float(f1_score(y_test, predictions, average="macro")),
        "confusion_matrix": confusion_matrix(y_test, predictions).tolist(),
        "classification_report": classification_report(y_test, predictions, zero_division=0),
    }

if __name__ == "__main__":
    for k, v in train_and_evaluate().items():
        print(f"{k}: {v}")
