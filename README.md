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
