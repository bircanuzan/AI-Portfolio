"""LlamaIndex source-grounded document QA; requires model/embedding provider credentials."""
import os
from pathlib import Path
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("LlamaIndex defaults here need OPENAI_API_KEY for embedding and generation.")
    source = Path(__file__).parent / "data"
    documents = SimpleDirectoryReader(input_dir=str(source), required_exts=[".md"]).load_data()
    engine = VectorStoreIndex.from_documents(documents).as_query_engine(similarity_top_k=2)
    response = engine.query("Who approves the example travel request?")
    print("Answer:", response)
    for item in response.source_nodes:
        print("Source:", item.node.metadata.get("file_name"), "score:", item.score)

if __name__ == "__main__":
    main()
