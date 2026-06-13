import chromadb
import uuid

class VectorStore:
    def __init__(self, path: str, collection_name: str):
        self.path: str = path
        self.collection_name: str = collection_name
        self.db = chromadb.PersistentClient(self.path)
        self.collection = self.db.get_or_create_collection(name=self.collection_name)

    def store(self, chunks: list[str], vectors: list[list[float]]) -> None:
        """Stores Chunks and vectors in Chroma DB"""
        ids = [str(uuid.uuid4()) for _ in chunks]
        self.collection.add(ids=ids, embeddings=vectors, documents=chunks)

    def count(self) -> int:
        """returns how many entries are in the collection"""
        return self.collection.count()

    def search(self, vector: list[float], top_k: int) -> list[str]:
        results = self.collection.query(query_embeddings=[vector], n_results=top_k)
        return results["documents"][0]