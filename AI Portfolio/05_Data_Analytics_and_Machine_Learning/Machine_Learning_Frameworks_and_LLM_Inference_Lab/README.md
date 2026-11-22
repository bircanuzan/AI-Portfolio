# Machine Learning Frameworks & LLM Inference Lab

**Portfolio type:** independently authored educational code examples and architecture comparison. **Status:** Code and instructions published; external execution, GPU profiling and LLM-server deployment have not been independently verified.

## Project objective
Explore core numerical computation, model-training frameworks and open-source LLM inference engines, using a small reproducible numerical demo and optional framework exercises. This project is designed to turn an ML job requirement into practical, inspectable learning artifacts; it does **not** represent commissioned work or established professional expertise in every tool.

## Tools explained and project scope

| Tool | What it does | What was added in this repository | Evidence limit |
|---|---|---|---|
| **NumPy** | Fast numerical arrays and linear algebra | Synthetic regression data, vectorized baseline and mean-squared-error calculation in `numerical_baseline.py` | Script provided; no run metrics asserted |
| **SciPy** | Optimization, statistics and scientific computing | Least-squares optimization and residual summary in the same demo | Script provided; no run metrics asserted |
| **PyTorch** | Tensor computation, automatic differentiation and deep-learning model training | Optional gradient-based linear-model training example in `framework_exercises.py` | Requires PyTorch locally; not claimed executed |
| **JAX** | Accelerated array computing, automatic differentiation and JIT compilation | Optional `grad` + `jit` optimization example in `framework_exercises.py` | Requires JAX locally; not claimed executed |
| **vLLM** | High-throughput LLM model serving and inference | API-compatible request example and deployment considerations in `inference_clients.py` | No vLLM server or throughput benchmark claimed |
| **SGLang** | Efficient LLM inference/serving and structured-generation workflows | Shared OpenAI-compatible request example with SGLang endpoint guidance | No SGLang server or GPU benchmark claimed |
| **llama.cpp** | Running quantized GGUF LLMs on local CPU/GPU | Shared OpenAI-compatible request example with local-server guidance | No model download or inference execution claimed |

## What was actually implemented in the repository
1. **Numerical ML baseline:** deterministic synthetic dataset, NumPy vectorized statistics and SciPy least-squares optimization.
2. **Training-loop comparison examples:** equivalent toy regression optimization routines using PyTorch autograd and JAX autodiff/JIT, to run only if installed.
3. **LLM serving test client:** an endpoint-agnostic Python request script designed to interact with vLLM, SGLang or llama.cpp *after the user deploys a compatible server*.
4. **Evaluation plan:** measure training loss, final parameter error, inference latency (p50/p95), tokens/sec, memory use, request errors and response quality in future controlled experiments. These are **proposed metrics, not achieved results**.

## Run instructions

### Numerical baseline (CPU)
```bash
python -m pip install numpy scipy
python numerical_baseline.py
```

### Optional PyTorch or JAX
Install one framework following its official platform-specific guidance, then:
```bash
python framework_exercises.py pytorch
python framework_exercises.py jax
```

### Optional local serving (requires a separately running model server)
```bash
# Example defaults; set API key and base URL for your chosen server
python inference_clients.py --base-url http://localhost:8000/v1 --model YOUR_MODEL_ID
```
For llama.cpp, common local OpenAI-compatible servers use port 8080; for vLLM and SGLang server configurations differ. Specify the actual serving URL and model ID. Do not assume any endpoint is running.

## Research and model-quality approach
- Compare identical small learning objectives across implementations.
- Fix random seeds and document dependency versions.
- Avoid data leakage and treat synthetic toy results as educational.
- For inference, track latency, errors and quality on the **same evaluation prompt set** and report hardware, quantization, context and batch settings before comparing engines.
- Investigate limitations: PyTorch/JAX are training/computation frameworks; vLLM, SGLang and llama.cpp primarily address serving/inference.

## CV and application wording (accurate)
"Developed an educational machine-learning framework comparison portfolio with NumPy/SciPy numerical optimization examples, optional PyTorch/JAX training demonstrations, and API-based test scaffolding for vLLM, SGLang and llama.cpp. Production deployment and benchmark validation are not claimed."

This is a personal learning portfolio: **do not select every listed tool as professional hands-on experience solely because the code examples exist.**
