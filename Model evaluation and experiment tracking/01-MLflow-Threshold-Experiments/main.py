"""MLflow local experiment tracking for synthetic model-score comparisons."""
import mlflow

SCORES = [0.12, 0.88, 0.77, 0.42, 0.91, 0.33]
LABELS = [0, 1, 1, 0, 1, 1]

def metrics(threshold: float) -> tuple[float, float]:
    predicted = [int(score >= threshold) for score in SCORES]
    tp = sum(p == y == 1 for p, y in zip(predicted, LABELS))
    fp = sum(p == 1 and y == 0 for p, y in zip(predicted, LABELS))
    fn = sum(p == 0 and y == 1 for p, y in zip(predicted, LABELS))
    return tp / max(tp + fp, 1), tp / max(tp + fn, 1)

if __name__ == "__main__":
    mlflow.set_tracking_uri("file:./mlruns")
    mlflow.set_experiment("synthetic-threshold-comparison")
    for threshold in (0.4, 0.6, 0.8):
        with mlflow.start_run(run_name=f"threshold-{threshold}"):
            precision, recall = metrics(threshold)
            mlflow.log_param("threshold", threshold)
            mlflow.log_metrics({"precision": precision, "recall": recall})
            print(threshold, precision, recall)
    print("Use mlflow ui --backend-store-uri ./mlruns to inspect runs.")
