"""Pinecone upsert/query with explicit write opt-in; uses only synthetic vectors."""
import os
from pinecone import Pinecone

VECTORS = [
    {"id": "portfolio-approval-v1", "values": [1.0, 0.0, 0.0],
     "metadata": {"topic": "approvals", "source": "synthetic"}},
    {"id": "portfolio-ai-v1", "values": [0.0, 1.0, 0.0],
     "metadata": {"topic": "ai-risk", "source": "synthetic"}},
]

def main() -> None:
    key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX")
    namespace = os.getenv("PINECONE_NAMESPACE", "portfolio-sandbox")
    if not key or not index_name:
        raise RuntimeError("Set PINECONE_API_KEY and PINECONE_INDEX for an existing 3D index.")
    if os.getenv("CONFIRM_PINECONE_WRITE") != "YES":
        raise RuntimeError("Set CONFIRM_PINECONE_WRITE=YES to opt in to paid external writes.")
    pc = Pinecone(api_key=key)
    idx = pc.Index(index_name)
    idx.upsert(vectors=VECTORS, namespace=namespace)
    result = idx.query(vector=[0.1, 0.9, 0.0], top_k=2,
                       namespace=namespace, include_metadata=True)
    for item in result.matches:
        print(item.id, item.score, item.metadata)

if __name__ == "__main__":
    main()
