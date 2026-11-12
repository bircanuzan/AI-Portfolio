"""FAISS exact nearest-neighbor similarity search on synthetic vectors."""
import faiss
import numpy as np

DOCUMENTS = ["Expense approval policy", "Recruitment process checklist",
             "AI agent risk controls", "Learning pathway template"]
VECTORS = np.asarray([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0],
], dtype=np.float32)
QUERY = np.asarray([[0.02, 0.01, 0.91, 0.01]], dtype=np.float32)

def search(k: int = 2) -> list[dict]:
    index = faiss.IndexFlatL2(VECTORS.shape[1])
    index.add(VECTORS)
    distances, neighbors = index.search(QUERY, k)
    return [{"document": DOCUMENTS[int(i)], "distance": round(float(d), 4)}
            for i, d in zip(neighbors[0], distances[0])]

if __name__ == "__main__":
    result = search()
    print(result)
    assert result[0]["document"] == "AI agent risk controls"
    print("Synthetic vectors only; semantic embeddings require an embedding model.")
