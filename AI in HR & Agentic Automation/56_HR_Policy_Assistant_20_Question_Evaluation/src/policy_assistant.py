"""Project 56: runnable local fictional HR policy assistant (NO LLM/API/real employee data)."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "fictional_policy_catalog.json"

def load_policies(path=SOURCE):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data["policies"]

def respond(prompt, policies=None):
    """Deterministic rule-based routing. Never provide personalized HR decisions."""
    q = prompt.lower()
    policies = load_policies() if policies is None else policies
    third_party = any(s in q for s in (
        "colleague", "another person", "another employee", "someone else", "coworker"
    ))
    sensitive = any(s in q for s in ("salary", "pay", "medical", "passport", "emirates id"))
    if third_party and sensitive:
        return {
            "route": "REFUSE", "policy_id": "PRIVACY", "citation": None,
            "answer": "I cannot provide another person's private information. Contact HR through an approved confidential channel if there is a legitimate need.",
            "needs_human": False
        }
    if any(s in q for s in (
        "appeal", "exception", "harassment", "dispute", "urgent", "emergency",
        "override", "accommodation", "my leave balance", "how many days", "entitled to"
    )):
        return {
            "route": "ESCALATE", "policy_id": "HUMAN", "citation": None,
            "answer": "This requires a human HR review or authenticated employee-service verification. Please raise a confidential HR case. Do not share personal information in this chat.",
            "needs_human": True
        }
    for policy in policies:
        if any(keyword in q for keyword in policy["keywords"]):
            return {
                "route": "ANSWER", "policy_id": policy["id"],
                "citation": policy["source"] + "@" + policy["version"],
                "answer": policy["response"], "needs_human": False
            }
    return {
        "route": "UNKNOWN", "policy_id": "NONE", "citation": None,
        "answer": "I cannot find that topic in this fictional approved policy catalogue. Please contact your HR team for guidance.",
        "needs_human": True
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--question", help="Run exactly one question")
    args = parser.parse_args()
    if args.question:
        print(json.dumps(respond(args.question), indent=2, ensure_ascii=False))
        return
    print("Fictional HR policy assistant. Type 'exit' to quit; do not enter personal data.")
    while True:
        try:
            query = input("HR question > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if query.lower() in ("quit", "exit"):
            break
        if query:
            print(json.dumps(respond(query), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
