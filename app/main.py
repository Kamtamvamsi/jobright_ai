from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# =========================================
# FastAPI App
# =========================================

app = FastAPI()

# =========================================
# Load Embedding Model
# =========================================

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded successfully!")

# =========================================
# Sample Jobs Dataset
# =========================================

jobs = [
    {
        "title": "AI Engineer",
        "description": "Python Machine Learning Deep Learning LangChain OpenAI FastAPI Vector Database"
    },
    {
        "title": "Backend Developer",
        "description": "FastAPI REST API Python SQL Backend Development"
    },
    {
        "title": "Machine Learning Engineer",
        "description": "TensorFlow PyTorch Machine Learning NLP Embeddings AI"
    },
    {
        "title": "Frontend Developer",
        "description": "React JavaScript HTML CSS Frontend UI"
    },
    {
        "title": "Data Scientist",
        "description": "Python Pandas NumPy Data Analysis Machine Learning"
    }
]

# =========================================
# Create Job Embeddings
# =========================================

job_texts = [job["description"] for job in jobs]

job_embeddings = model.encode(job_texts)

job_embeddings = np.array(job_embeddings).astype("float32")

# =========================================
# Create FAISS Index
# =========================================

dimension = job_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(job_embeddings)

print("FAISS index created!")

# =========================================
# Request Model
# =========================================

class ResumeRequest(BaseModel):
    resume: str

# =========================================
# Job Matching Function
# =========================================

def retrieve_jobs(resume_text):

    # Create resume embedding
    resume_embedding = model.encode([resume_text])

    resume_embedding = np.array(resume_embedding).astype("float32")

    # Search similar jobs
    distances, indices = index.search(resume_embedding, 3)

    matched_jobs = []

    for i, idx in enumerate(indices[0]):

        job = jobs[idx]

        similarity_score = round((1 / (1 + distances[0][i])) * 100, 2)

        reason = generate_reason(job["title"], resume_text)

        matched_jobs.append({
            "job_title": job["title"],
            "match_percentage": similarity_score,
            "reason": reason
        })

    return matched_jobs

# =========================================
# Simple Reason Generator
# =========================================

def generate_reason(job_title, resume):

    resume = resume.lower()

    reasons = []

    if "python" in resume:
        reasons.append("Python")

    if "fastapi" in resume:
        reasons.append("FastAPI")

    if "machine learning" in resume:
        reasons.append("Machine Learning")

    if "langchain" in resume:
        reasons.append("LangChain")

    if "react" in resume:
        reasons.append("React")

    if "sql" in resume:
        reasons.append("SQL")

    if len(reasons) == 0:
        return f"Basic skills matched for {job_title}"

    return f"Matched because of skills in: {', '.join(reasons)}"

# =========================================
# Root Route
# =========================================

@app.get("/")
def home():
    return {
        "message": "Mini Jobright AI Backend Running"
    }

# =========================================
# Match Route
# =========================================

@app.post("/match")
def match_jobs(request: ResumeRequest):

    try:

        matched_jobs = retrieve_jobs(request.resume)

        return {
            "success": True,
            "matches": matched_jobs
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }