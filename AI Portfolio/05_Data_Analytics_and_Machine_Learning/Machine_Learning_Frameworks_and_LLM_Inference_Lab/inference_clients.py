"""Minimal OpenAI-compatible LLM inference client.

Supply a running vLLM/SGLang/llama.cpp server with chat completions enabled.
No server, weights, or GPU deployment is included in this repository.
"""
import argparse
import json
import os
import time
from urllib.request import Request, urlopen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True, help="e.g., http://localhost:8000/v1")
    parser.add_argument("--model", required=True, help="model identifier exposed by server")
    parser.add_argument("--prompt", default="Explain data leakage in one sentence.")
    args = parser.parse_args()
    payload = json.dumps({
        "model": args.model,
        "messages": [{"role": "user", "content": args.prompt}],
        "max_tokens": 96,
        "temperature": 0,
    }).encode("utf-8")
    req = Request(
        args.base_url.rstrip("/") + "/chat/completions",
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + os.getenv("LLM_API_KEY", "not-needed"),
        },
    )
    start = time.perf_counter()
    with urlopen(req, timeout=90) as response:
        result = json.loads(response.read().decode("utf-8"))
    print(json.dumps({
        "elapsed_seconds": round(time.perf_counter() - start, 3),
        "response": result.get("choices", [{}])[0].get("message", {}).get("content", ""),
        "usage": result.get("usage"),
    }, indent=2))


if __name__ == "__main__":
    main()
