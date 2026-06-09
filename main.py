import chunker
from embedder import Embedder
import loader

if __name__ == "__main__":
    embedder = Embedder("sentence-transformers/all-MiniLM-L6-v2")
    data: str = loader.load_document("./data/sample.txt")
    chunks: list[str] = chunker.chunk_text(data, 100, 10)
    vectors = embedder.embed(chunks)
