from vector_store import VectorStore
from embedder import Embedder

class Retriever:
    def __init__(self, vector_store: VectorStore, embedder: Embedder):
        self.store = vector_store
        self.embedder = embedder

    def retrieve(self, query: str, top_k: int) -> list[str]:
        embedded_query = self.embedder.embed([query])
        return self.store.search(embedded_query[0], top_k)