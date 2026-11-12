"""LangChain policy assistant — synthetic policy; OpenAI key required."""
import os
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage

POLICY = "Annual leave requires manager approval. Employee requests must be recorded in the HR system."

def answer(question: str) -> str:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY in your environment.")
    model = init_chat_model(os.getenv("OPENAI_MODEL", "openai:gpt-4o-mini"), temperature=0)
    system = ("Answer only using the following example policy. "
              "If the information is absent, say 'Not specified in the policy'. "
              "Policy: " + POLICY)
    reply = model.invoke([SystemMessage(content=system), HumanMessage(content=question)])
    return str(reply.content)

if __name__ == "__main__":
    print(answer("How is annual leave approved?"))
