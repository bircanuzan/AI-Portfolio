"""Transformers inference on synthetic sample feedback; model downloads on first run."""
from transformers import pipeline

EXAMPLES = [
    "The onboarding instructions were clear and helpful.",
    "The system failed repeatedly and support was unavailable.",
]

def main() -> None:
    classifier = pipeline("sentiment-analysis",
                          model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
    for text, result in zip(EXAMPLES, classifier(EXAMPLES)):
        print({"input": text, "label": result["label"],
               "confidence": round(result["score"], 3)})
    print("Note: sentiment labels do not establish employee satisfaction or causation.")

if __name__ == "__main__":
    main()
