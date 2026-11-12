"""Ollama local inference. Run 'ollama pull llama3.2' before this script."""
import os
from ollama import Client

SYSTEM = ("You analyze fictional business processes. Suggest improvements, "
          "but do not claim measured results or invent source facts.")
PROCESS = ("A fictional approvals queue has three manual handoffs "
           "and no defined owner for exception requests.")

def main() -> None:
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "llama3.2")
    reply = Client(host=host).chat(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": "Identify two process risks and two controls: " + PROCESS},
        ],
    )
    print(reply.message.content)
    print("Check the suggestions manually; local models can hallucinate.")

if __name__ == "__main__":
    main()
