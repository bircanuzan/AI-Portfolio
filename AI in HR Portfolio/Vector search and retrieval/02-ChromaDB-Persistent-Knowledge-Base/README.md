# Persistent local policy retrieval with ChromaDB

**Tool:** ChromaDB
**Project status:** portfolio prototype; not proof of production implementation.

## Scenario
Index fictional HR-process documents with explicitly supplied reproducible toy embeddings.

## What it demonstrates
- Direct usage of ChromaDB in a minimal, self-contained example.
- A synthetic data workflow, not identifiable customer or employee data.
- Explicit failure/permission checks and constraints relevant to this tool.

## Run
```bash
python -m venv .venv
# activate the environment
pip install -r requirements.txt
python main.py  # creates a local .chroma/ collection
```

## Verification and limitations
Confirm the command outputs an expected result on your machine before citing it as a tested project. For external services, configure credentials via environment variables, never in tracked code. Cost, connectivity, quotas, and security differ by service. No actual performance benchmark has been claimed.

