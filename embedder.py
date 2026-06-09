from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self, model_name: str):
        self.model_name: str = model_name
        self.model: SentenceTransformer = SentenceTransformer(self.model_name)

    def embed(self, chunks: list[str]) -> list[list[float]]:
        embeddings = self.model.encode(chunks)
        return embeddings.tolist()
