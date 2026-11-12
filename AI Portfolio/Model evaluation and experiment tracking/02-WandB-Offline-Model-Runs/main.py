"""W&B demo defaults to offline logging; no external upload required."""
import os
import wandb

def main() -> None:
    mode = os.getenv("WANDB_MODE", "offline")
    for architecture, sample_accuracy in [("baseline", 0.72), ("candidate", 0.78)]:
        with wandb.init(project="synthetic-ai-evaluation", mode=mode,
                        config={"architecture": architecture, "seed": 2026}) as run:
            run.log({"holdout_accuracy": sample_accuracy, "test_samples": 100})
            print(architecture, sample_accuracy)
    print("These figures are illustrative only; no model was trained here.")

if __name__ == "__main__":
    main()
