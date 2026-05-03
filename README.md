# 🚀 AI Job Matching Agent (RAG + LLM + FastAPI)

An end-to-end AI system that matches resumes to relevant jobs using semantic search, Retrieval-Augmented Generation (RAG), and LLM-based reasoning — inspired by real-world platforms like Jobright.

---

## 🎯 Problem Statement

Traditional job search is inefficient and keyword-based. This system demonstrates how AI can:
- Understand candidate profiles semantically
- Match them with relevant opportunities
- Provide explainable reasoning for each match

---

## ⚡ Key Features

✔ Resume → Embedding pipeline (semantic understanding)  
✔ Vector Database (FAISS) for similarity search  
✔ RAG-based job retrieval system  
✔ LLM-powered reasoning: “Why this job fits”  
✔ FastAPI backend for production-style APIs  
✔ Modular and scalable architecture  

---

## 🧠 System Architecture
Resume Input → Embedding Model → Vector DB (FAISS) ↓ Job Dataset Embeddings ↓ Similarity Search ↓ LLM Reasoning Layer ↓ API Response (FastAPI)

---

## 🧩 Tech Stack

- **Backend:** FastAPI  
- **Embeddings:** Sentence Transformers  
- **Vector DB:** FAISS  
- **LLM:** OpenAI API  
- **Language:** Python  
- **Optional UI:** Streamlit  

---

## 🧪 How It Works

1. Resume text is converted into embeddings  
2. Job descriptions are pre-embedded and stored in FAISS  
3. Semantic similarity search retrieves top matching jobs  
4. LLM analyzes resume + job and generates reasoning  
5. API returns structured job matches + explanations  

---

## 📊 Example Output

**Input:** Resume with Python, ML, API development  

**Output:**


Job: AI Engineer
Reason:
Strong alignment with Python and ML experience
Experience with APIs fits backend AI systems
Exposure to AI workflows matches role requirements

---

## 🛠️ Setup Instructions

```bash
# Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Mini_jobright.git

cd Mini_jobright
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Project

## Start FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```bash
http://127.0.0.1:8000
```

---

## Start Streamlit Frontend

Open a new terminal and run:

```bash
streamlit run ui/streamlit_app.py
```

Frontend URL:

```bash
http://localhost:8501
```

---

# Project Workflow

1. User enters resume text
2. Backend converts resume into embeddings
3. FAISS performs vector similarity search
4. System finds best matching jobs
5. AI returns matching score and fit explanation

---

# Technologies Used

* Python
* FastAPI
* Streamlit
* Sentence Transformers
* FAISS
* Pandas
* NumPy

---

# Current Status

✅ Localhost working version completed

❌ No deployment yet

Currently NOT deployed on:

* Render
* Railway
* GCP
* AWS
* Azure

---

# Future Improvements

* Cloud Deployment
* Docker Support
* Authentication
* Pinecone Integration
* Real-time Job Scraping
* RAG Pipeline
* LLM-based Reasoning
