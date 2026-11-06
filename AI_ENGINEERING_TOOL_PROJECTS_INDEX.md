# AI Engineering & LLM Toolkit — 20 Technology Projects

This index maps each of the 20 named technologies to a **separate example project** inside the existing AI-in-HR Portfolio.

**Status notice:** these are source-level educational prototypes/templates, authored for demonstration. No claim is made that all 20 were executed, integrated with paid accounts, independently benchmarked, or deployed to production. Some projects require cloud keys, model downloads, Docker, or hosted vector infrastructure.

| Technology | Project | Application |
|---|---|---|
| LangChain | [01-LangChain-Policy-Assistant](LLM%20application%20development/01-LangChain-Policy-Assistant/README.md) | LLM application development |
| LlamaIndex | [02-LlamaIndex-Document-QA](LLM%20application%20development/02-LlamaIndex-Document-QA/README.md) | LLM application development |
| OpenAI API | [03-OpenAI-API-Structured-Extraction](LLM%20application%20development/03-OpenAI-API-Structured-Extraction/README.md) | LLM application development |
| LangGraph | [01-LangGraph-Human-Approval-Workflow](Agentic%20AI%20Orchestration/01-LangGraph-Human-Approval-Workflow/README.md) | Agentic AI Orchestration |
| Model Context Protocol (MCP) | [02-MCP-Skill-Inventory-Tools](Agentic%20AI%20Orchestration/02-MCP-Skill-Inventory-Tools/README.md) | Agentic AI Orchestration |
| Hugging Face Transformers | [01-HuggingFace-Transformers-Feedback-Classifier](AI%20models%20and%20evaluation/01-HuggingFace-Transformers-Feedback-Classifier/README.md) | AI models and evaluation |
| PyTorch | [02-PyTorch-Skills-Gap-Classifier](AI%20models%20and%20evaluation/02-PyTorch-Skills-Gap-Classifier/README.md) | AI models and evaluation |
| TensorFlow | [03-TensorFlow-Workload-Forecast](AI%20models%20and%20evaluation/03-TensorFlow-Workload-Forecast/README.md) | AI models and evaluation |
| Ragas | [01-Ragas-Groundedness-Score](RAG%20evaluation/01-Ragas-Groundedness-Score/README.md) | RAG evaluation |
| DeepEval | [02-DeepEval-Response-Quality](RAG%20evaluation/02-DeepEval-Response-Quality/README.md) | RAG evaluation |
| LangSmith | [01-LangSmith-Agent-Decision-Traces](Agent%20tracing%20and%20testing/01-LangSmith-Agent-Decision-Traces/README.md) | Agent tracing and testing |
| MLflow | [01-MLflow-Threshold-Experiments](Model%20evaluation%20and%20experiment%20tracking/01-MLflow-Threshold-Experiments/README.md) | Model evaluation and experiment tracking |
| Weights & Biases (W&B) | [02-WandB-Offline-Model-Runs](Model%20evaluation%20and%20experiment%20tracking/02-WandB-Offline-Model-Runs/README.md) | Model evaluation and experiment tracking |
| FastAPI | [01-FastAPI-Decision-Service](AI%20application%20and%20API%20development/01-FastAPI-Decision-Service/README.md) | AI application and API development |
| Pydantic | [02-Pydantic-Structured-AI-Validation](AI%20application%20and%20API%20development/02-Pydantic-Structured-AI-Validation/README.md) | AI application and API development |
| Docker | [03-Docker-Containerized-Scoring-API](AI%20application%20and%20API%20development/03-Docker-Containerized-Scoring-API/README.md) | AI application and API development |
| FAISS | [01-FAISS-Similarity-Index](Vector%20search%20and%20retrieval/01-FAISS-Similarity-Index/README.md) | Vector search and retrieval |
| ChromaDB | [02-ChromaDB-Persistent-Knowledge-Base](Vector%20search%20and%20retrieval/02-ChromaDB-Persistent-Knowledge-Base/README.md) | Vector search and retrieval |
| Pinecone | [03-Pinecone-Managed-Vector-Search](Vector%20search%20and%20retrieval/03-Pinecone-Managed-Vector-Search/README.md) | Vector search and retrieval |
| Ollama | [01-Ollama-Offline-Process-Assistant](Local%20LLM%20inference/01-Ollama-Offline-Process-Assistant/README.md) | Local LLM inference |

## Categories
- [LLM application development](LLM%20application%20development/README.md) — 3 standalone projects
- [Agentic AI Orchestration](Agentic%20AI%20Orchestration/README.md) — 2 standalone projects
- [AI models and evaluation](AI%20models%20and%20evaluation/README.md) — 3 standalone projects
- [RAG evaluation](RAG%20evaluation/README.md) — 2 standalone projects
- [Agent tracing and testing](Agent%20tracing%20and%20testing/README.md) — 1 standalone projects
- [Model evaluation and experiment tracking](Model%20evaluation%20and%20experiment%20tracking/README.md) — 2 standalone projects
- [AI application and API development](AI%20application%20and%20API%20development/README.md) — 3 standalone projects
- [Vector search and retrieval](Vector%20search%20and%20retrieval/README.md) — 3 standalone projects
- [Local LLM inference](Local%20LLM%20inference/README.md) — 1 standalone projects

## Verification checklist
- [ ] Create a clean Python environment for each individual project, then install its listed requirements.
- [ ] Run each project using its README command; capture terminal output and note relevant dependency versions.
- [ ] Where model APIs are used, set keys in your environment rather than committing secrets.
- [ ] Review service charges and data handling before calling hosted models or vector services.
- [ ] Test relevant error paths, safety checks, and ground-truth scenarios before treating examples as production ready.
- [ ] Record reproducible benchmarks only after actual execution; do not advertise illustrative test outputs as empirical results.

**Suggested next step:** add CI smoke tests and dependency lock files after selecting the projects to use for freelancing applications.

