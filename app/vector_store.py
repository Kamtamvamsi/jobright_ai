import faiss
import numpy as np
import pickle
import os

class VectorStore:

    
    # =========================================
    # Reset Index
    # =========================================  
    def reset(self):
        self.index = faiss.IndexFlatL2(
            self.dimension
        )
        self.metadata = []
        print("FAISS reset successfully!")
    
    def __init__(self, dimension=384):

        self.dimension = dimension

        self.index_path = "data/faiss.index"

        self.metadata_path = "data/metadata.pkl"

        self.metadata = []

        # =========================================
        # Load Existing FAISS
        # =========================================

        if os.path.exists(self.index_path):

            print("Loading existing FAISS index...")

            self.index = faiss.read_index(
                self.index_path
            )

            if os.path.exists(self.metadata_path):

                with open(
                    self.metadata_path,
                    "rb"
                ) as file:

                    self.metadata = pickle.load(file)

            print("FAISS loaded successfully!")

        else:

            print("Creating new FAISS index...")

            self.index = faiss.IndexFlatL2(
                dimension
            )

    # =========================================
    # Add Embeddings
    # =========================================

    def add_embeddings(self, embeddings, metadata):

        embeddings = np.array(
            embeddings
        ).astype("float32")

        self.index.add(embeddings)

        self.metadata.extend(metadata)

        self.save()

    # =========================================
    # Save FAISS + Metadata
    # =========================================

    def save(self):

        faiss.write_index(
            self.index,
            self.index_path
        )

        with open(
            self.metadata_path,
            "wb"
        ) as file:

            pickle.dump(
                self.metadata,
                file
            )

        print("FAISS index saved!")

    # =========================================
    # Search
    # =========================================

    def search(self, query_embedding, top_k=5):

        query_embedding = np.array(
            [query_embedding]
        ).astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for i, idx in enumerate(indices[0]):

            if idx < len(self.metadata):

                job = self.metadata[idx]

                similarity_score = round(
                    (1 / (1 + distances[0][i])) * 100,
                    2
                )

                results.append({
                    "job": job,
                    "score": similarity_score
                })

        return results