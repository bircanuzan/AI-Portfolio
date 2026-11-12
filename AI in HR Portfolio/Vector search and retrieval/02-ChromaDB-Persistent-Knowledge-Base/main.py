"""Chroma persistent collection with small synthetic keyword-derived embeddings."""
from pathlib import Path
import chromadb

VOCAB = ("approval", "skills", "risk", "learning")

def embed(text: str) -> list[float]:
    lower = text.lower()
    return [float(lower.count(word)) for word in VOCAB]

DOCS = [
    ("approval-policy", "Manager approval is required before any business travel."),
    ("skills-catalog", "The skills inventory tracks python and data literacy."),
    ("agent-risk", "AI agent risk review requires explicit human oversight."),
]
if __name__ == "__main__":
    client = chromadb.PersistentClient(path=str(Path(__file__).parent / ".chroma"))
    collection = client.get_or_create_collection("synthetic_knowledge_notes")
    collection.upsert(
        ids=[item[0] for item in DOCS],
        documents=[item[1] for item in DOCS],
        embeddings=[embed(item[1]) for item in DOCS],
    )
    query = "approval manager travel"
    result = collection.query(query_embeddings=[embed(query)], n_results=2)
    print(result["ids"][0])
    assert "approval-policy" in result["ids"][0]
    print("Toy embeddings for retrieval mechanics only; replace with production vectors.")
