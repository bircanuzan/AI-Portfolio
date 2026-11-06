"""OpenAI Responses API: extract synthetic incident facts without storing PII."""
import json
import os
from openai import OpenAI

NOTE = "On 4 June, two demo invoices were delayed because the queue was paused; operations restarted the worker."
FIELDS = {"incident_date": "string or null", "problem": "string", "action": "string"}

def extract(note: str) -> dict:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY.")
    result = OpenAI().responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        instructions=("Extract only evidenced facts. Return a JSON object with these keys: "
                      + json.dumps(FIELDS) + ". No markdown. Use null for missing facts."),
        input=note,
    )
    obj = json.loads(result.output_text)
    if set(obj) != set(FIELDS):
        raise ValueError("Unexpected keys in extracted response")
    return obj

if __name__ == "__main__":
    print(json.dumps(extract(NOTE), indent=2))
