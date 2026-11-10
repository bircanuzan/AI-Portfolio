# AI Engineer (LLM Focus) — Interview Questions & Answers

## Q1 — Multi-turn AI agent shipped to production
**Question:** Briefly describe the most complex multi-turn AI agent you've shipped to production. What framework did you use, and how did you handle tool-calling failures or infinite reasoning loops? (Max 3 sentences)

**Answer:**
> My most complex documented work is a LangGraph-based multi-turn agent prototype with conditional tool execution, human approval gates, and traceable decisions; it has not yet been deployed to production. My production-hardening approach uses schema validation, tool timeouts, bounded retries, exponential backoff, and safe escalation. To prevent infinite loops, I design explicit termination conditions, iteration limits, and state-based guardrails.

**Evidence note:** Current repository contains *separate* LangGraph conditional-approval, MCP tool-server and LangSmith tracing examples. Their combination into a unified multi-turn tool-calling copilot is an architecture/prototype direction, not a verified shipped agent. Do not characterize the separate samples as one finished production product.

**Capability signals:** LangGraph StateGraph, safe tool use, explicit termination, retries/fallbacks, decision tracing, human oversight. New answers should be added with the same evidence boundary; never fabricate commercial deliveries or metrics.
