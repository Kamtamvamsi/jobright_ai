import faiss
import numpy as np

class VectorStore:

    def __init__(self, dimension=384):

        # Create FAISS index
        self.index = faiss.IndexFlatL2(dimension)

        # Metadata storage
        self.metadata = []

    def add_embeddings(self, embeddings, metadata):

        # Convert to NumPy float32
        embeddings = np.array(embeddings).astype('float32')

        # Add embeddings to FAISS
        self.index.add(embeddings)

        # Store metadata
        self.metadata.extend(metadata)

    def search(self, query_embedding, top_k=3):

        query_embedding = np.array([query_embedding]).astype('float32')

        # Similarity search
        distances, indices = self.index.search(query_embedding, top_k)

        results = []

        for idx in indices[0]:
            results.append(self.metadata[idx])

        return results