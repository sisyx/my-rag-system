import chunker
from embedder import Embedder
import loader
from vector_store import VectorStore as Store

if __name__ == "__main__":
    embedder = Embedder("sentence-transformers/all-MiniLM-L6-v2")
    data: str = loader.load_document("./data/sample.txt")
    chunks: list[str] = chunker.chunk_text(data, 100, 10)
    vectors = embedder.embed(chunks)
    store = Store("vectors", "main")
    store.store(chunks, vectors)
    print(store.count())