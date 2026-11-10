# AI Engineer (LLM Focus) — Interview Questions & Answers

## Q1 — Multi-turn AI agent shipped to production
**Question:** Briefly describe the most complex multi-turn AI agent you've shipped to production. What framework did you use, and how did you handle tool-calling failures or infinite reasoning loops? (Max 3 sentences)

**Answer:**
> My most complex documented work is a LangGraph-based multi-turn agent prototype with conditional tool execution, human approval gates, and traceable decisions; it has not yet been deployed to production. My production-hardening approach uses schema validation, tool timeouts, bounded retries, exponential backoff, and safe escalation. To prevent infinite loops, I design explicit termination conditions, iteration limits, and state-based guardrails.

**Evidence note:** Current repository contains *separate* LangGraph conditional-approval, MCP tool-server and LangSmith tracing examples. Their combination into a unified multi-turn tool-calling copilot is an architecture/prototype direction, not a verified shipped agent. Do not characterize the separate samples as one finished production product.

**Capability signals:** LangGraph StateGraph, safe tool use, explicit termination, retries/fallbacks, decision tracing, human oversight. New answers should be added with the same evidence boundary; never fabricate commercial deliveries or metrics.

## Q2 — Most advanced agentic workflow and multi-turn context
**Question:** What is the most advanced agentic workflow you've built from scratch? Describe your approach to managing long-term context retention and state across multi-turn interactions.

**Interview answer:**
> I developed a prototype Human Capital Intelligence Agent combining LLM-driven analysis, multi-step workflows, tool integration, and human-in-the-loop decision controls. For multi-turn state management, my architecture separates short-term conversation history from persistent structured memory, using session identifiers, state checkpoints, and retrieval-based context recovery. To prevent context drift, I use summarization, relevance-based retrieval, bounded context windows, and explicit state validation, with access controls for sensitive data.

**Evidence boundary:** This describes a prototype and a state-management architecture approach, not a verified production deployment. Long-term memory, session checkpoint persistence, context recovery, and access-control mechanisms must be tested and evidenced before presenting them as implemented capabilities.
