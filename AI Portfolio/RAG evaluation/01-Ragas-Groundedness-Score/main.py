"""Ragas Faithfulness with remote evaluator model; consumes API credits."""
import asyncio
import os
from openai import AsyncOpenAI
from ragas.llms import llm_factory
from ragas.metrics.collections import Faithfulness

async def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY to use the evaluator model.")
    evaluator = llm_factory(os.getenv("EVAL_MODEL", "gpt-4o-mini"), client=AsyncOpenAI())
    result = await Faithfulness(llm=evaluator).ascore(
        response="The fictional service desk operates Monday to Friday.",
        retrieved_contexts=[
            "Service-desk hours for the demo tenant are Monday to Friday, 09:00-17:00."
        ],
    )
    print({"faithfulness": result.value, "reason": result.reason})

if __name__ == "__main__":
    asyncio.run(main())
