import json

from app.embeddings import get_embedding
from app.vector_store import VectorStore

# Create vector database
vector_db = VectorStore()

def load_jobs():

    with open("data/jobs.json", "r") as file:
        jobs = json.load(file)

    embeddings = []

    for job in jobs:

        # Convert description into vector
        embedding = get_embedding(job["description"])

        embeddings.append(embedding)

    # Store embeddings
    vector_db.add_embeddings(embeddings, jobs)

def retrieve_jobs(resume_text):

    # Convert resume into vector
    resume_embedding = get_embedding(resume_text)

    # Find top matching jobs
    results = vector_db.search(resume_embedding)

    return results

