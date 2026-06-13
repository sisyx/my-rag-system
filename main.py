import chunker
from embedder import Embedder
import loader
from vector_store import VectorStore as Store
from retriever import Retriever

if __name__ == "__main__":
    embedder = Embedder("sentence-transformers/all-MiniLM-L6-v2")
    data: str = loader.load_document("./data/sample.txt")
    chunks: list[str] = chunker.chunk_text(data, 400, 40)
    vectors = embedder.embed(chunks)
    store = Store("vectors", "main")
    store.store(chunks, vectors)
    retriever = Retriever(store, embedder)
    found = retriever.retrieve("overlap", top_k=3)
    for found_item in found:
        print(found_item)