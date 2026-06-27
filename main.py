import chunker
from embedder import Embedder
import loader
from vector_store import VectorStore as Store
from retriever import Retriever
from generator import Generator
import os

GENERATOR_MODEL = "llama-3.1-8b-instant"
GROQ_API_KEY = os.environ["GROQ_API_KEY"]
SENTENCE_TRANSFORMER_MODEL="sentence-transformers/all-MiniLM-L6-v2"

if __name__ == "__main__":
    embedder = Embedder("sentence-transformers/all-MiniLM-L6-v2")
    data: str = loader.load_document("./data/sample.txt")
    chunks: list[str] = chunker.chunk_text(data, 400, 40)
    vectors = embedder.embed(chunks)
    store = Store("vectors", "main")
    store.store(chunks, vectors)
    retriever = Retriever(store, embedder)
    generator = Generator(GENERATOR_MODEL, GROQ_API_KEY)
    while True:
        question = input("your question here > ")
        found = retriever.retrieve(question, top_k=3)
        answers = generator.generate(question, found)
        print(answers)