"""Optional sovereign/OpenAI-compatible HTTPS summarisation, never tool control."""
import json
import os
from urllib.parse import urlparse
from urllib.request import Request,urlopen

class ProviderUnavailable(Exception):
    pass

def summarize(result):
    url=os.getenv("HCIA_LLM_ENDPOINT","")
    key=os.getenv("HCIA_LLM_API_KEY","")
    model=os.getenv("HCIA_LLM_MODEL","")
    allowed={h.strip().lower() for h in os.getenv("HCIA_LLM_HOST_ALLOWLIST","").split(",") if h.strip()}
    parsed=urlparse(url)
    if not (url and key and model and parsed.scheme=="https" and parsed.hostname
            and parsed.hostname.lower() in allowed and not parsed.username and not parsed.password):
        raise ProviderUnavailable("Operator model gateway not configured")
    payload={"model":model,"temperature":0,"max_tokens":320,"messages":[
      {"role":"system","content":"Only describe these fictional aggregate metrics. Never invent facts, determine HR outcomes or request tools. Highlight limits."},
      {"role":"user","content":json.dumps(result)[:12000]}]}
    req=Request(url,data=json.dumps(payload).encode(),method="POST",headers={
       "Authorization":"Bearer "+key,"Content-Type":"application/json"})
    try:
        with urlopen(req,timeout=8) as response:
            value=json.loads(response.read(128000))["choices"][0]["message"]["content"]
        if not isinstance(value,str) or not value.strip():
            raise ValueError("Empty response")
    except Exception as ex:
        raise ProviderUnavailable("LLM unavailable; use source metrics") from ex
    return {"mode":"configured_live_llm","model":model,"text":value[:3000],
            "review":"Human must verify against cited metrics"}
