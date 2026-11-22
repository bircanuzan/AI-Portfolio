"""Compare pretrained baseline and LoRA adapter on untouched synthetic examples."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from train_lora import prompt_for
from validate_data import read_rows


def score(text: str, expected: str) -> tuple[bool, bool]:
    try:
        obj = json.loads(text.strip())
    except (json.JSONDecodeError, TypeError):
        return False, False
    valid = isinstance(obj, dict) and set(obj) == {"intent"} and obj["intent"] in {
        "billing", "technical", "unknown"
    }
    return valid, bool(valid and obj["intent"] == expected)


def run_model(model, tokenizer, rows):
    import torch
    model.eval()
    results = []
    for row in rows:
        tokens = tokenizer(prompt_for(row["message"]), return_tensors="pt")
        device = next(model.parameters()).device
        tokens = {k: v.to(device) for k, v in tokens.items()}
        with torch.no_grad():
            completion = model.generate(
                **tokens, max_new_tokens=24, do_sample=False,
                pad_token_id=tokenizer.pad_token_id,
            )
        response = tokenizer.decode(
            completion[0, tokens["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()
        valid, correct = score(response, row["intent"])
        results.append({"id": row["id"], "expected": row["intent"],
                        "output": response, "valid_json_schema": valid,
                        "correct": correct})
    total = len(results)
    return {
        "schema_validity_pct": round(100 * sum(r["valid_json_schema"] for r in results) / total, 1),
        "exact_intent_accuracy_pct": round(100 * sum(r["correct"] for r in results) / total, 1),
        "items": results,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="Qwen/Qwen2.5-0.5B-Instruct")
    parser.add_argument("--adapter", default="outputs/sft_adapter")
    parser.add_argument("--output", default="outputs/eval.json")
    args = parser.parse_args()

    from transformers import AutoTokenizer, AutoModelForCausalLM
    from peft import PeftModel

    rows = read_rows(Path(__file__).parent / "data/test.jsonl")
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    baseline = AutoModelForCausalLM.from_pretrained(args.model)
    results = {"source": "synthetic", "base_model": args.model,
               "baseline": run_model(baseline, tokenizer, rows)}
    del baseline
    adapted_base = AutoModelForCausalLM.from_pretrained(args.model)
    adapter = PeftModel.from_pretrained(adapted_base, args.adapter)
    results["adapter"] = run_model(adapter, tokenizer, rows)
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps({name: {k: v for k, v in results[name].items() if k != "items"}
                      for name in ("baseline", "adapter")}, indent=2))
    print(f"Evidence written to {path} (no metrics are claimed in this README).")


if __name__ == "__main__":
    main()
