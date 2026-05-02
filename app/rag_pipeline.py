import json

from app.embeddings import get_embedding
from app.vector_store import VectorStore

# =========================================
# Vector Database
# =========================================

vector_db = VectorStore()

# =========================================
# Build/Rebuild FAISS
# =========================================

def load_jobs():

    print("Loading jobs into FAISS...")

    # Reset FAISS
    vector_db.reset()

    with open(
        "data/jobs.json",
        "r",
        encoding="utf-8"
    ) as file:

        jobs = json.load(file)

    embeddings = []

    metadata = []

    # Safety limit
    jobs = jobs[:100]

    for job in jobs:

        combined_text = f"""
        {job['title']}
        {job['description']}
        """

        embedding = get_embedding(
            combined_text
        )

        embeddings.append(
            embedding
        )

        metadata.append(job)

    vector_db.add_embeddings(
        embeddings,
        metadata
    )

    print(
        f"FAISS rebuilt with {len(jobs)} jobs"
    )

# =========================================
# Retrieve Jobs
# =========================================

def retrieve_jobs(resume_text):

    resume_embedding = get_embedding(
        resume_text
    )

    results = vector_db.search(
        resume_embedding,
        top_k=5
    )

    return results