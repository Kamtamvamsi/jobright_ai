
# from fastapi import FastAPI
# from pydantic import BaseModel

# from app.scraper import scrape_all_jobs
# from app.rag_pipeline import (
#     load_jobs,
#     retrieve_jobs
# )
# from app.llm_reasoning import (
#     generate_reasoning
# )
# from app.job_refresher import (
#     start_scheduler
# )

# print("FASTAPI SERVER STARTED")

# # =========================================
# # FastAPI App
# # =========================================

# app = FastAPI()

# # =========================================
# # Initial Job Scraping
# # =========================================

# print("\nFetching latest jobs...")

# scrape_all_jobs()

# # =========================================
# # Build Initial FAISS Database
# # =========================================

# print("\nBuilding FAISS database...")

# load_jobs()

# # =========================================
# # Start Background Scheduler
# # =========================================

# print("\nStarting job refresh scheduler...")

# start_scheduler()

# # =========================================
# # Request Model
# # =========================================

# class ResumeRequest(BaseModel):

#     resume: str

# # =========================================
# # Root Route
# # =========================================

# @app.get("/")
# def home():

#     return {
#         "message": (
#             "Mini Jobright AI Running Successfully"
#         )
#     }

# # =========================================
# # Match Route
# # =========================================

# @app.post("/match")
# def match_jobs(
#     request: ResumeRequest
# ):

#     try:

#         # =====================================
#         # Retrieve Matching Jobs
#         # =====================================

#         results = retrieve_jobs(
#             request.resume
#         )

#         matches = []

#         # =====================================
#         # Generate AI Reasoning
#         # =====================================

#         for item in results:

#             job = item["job"]

#             score = item["score"]

#             reasoning = generate_reasoning(
#                 request.resume,
#                 job
#             )

#             print("\n====================")
#             print(
#                 f"MATCHED JOB: "
#                 f"{job.get('title')}"
#             )
#             print(
#                 f"SCORE: {score}%"
#             )
#             print(
#                 f"COMPANY: "
#                 f"{job.get('company')}"
#             )
#             print("====================")

#             matches.append({

#                 "job_title": job.get(
#                     "title",
#                     "N/A"
#                 ),

#                 "company": job.get(
#                     "company",
#                     "N/A"
#                 ),

#                 "location": job.get(
#                     "location",
#                     "Remote"
#                 ),

#                 "source": job.get(
#                     "source",
#                     "Unknown"
#                 ),

#                 "job_url": job.get(
#                     "url",
#                     ""
#                 ),

#                 "match_percentage": score,

#                 "reasoning": reasoning
#             })

#         # =====================================
#         # Return Response
#         # =====================================

#         return {

#             "success": True,

#             "total_matches": len(
#                 matches
#             ),

#             "matches": matches
#         }

#     except Exception as e:

#         print(
#             f"\nERROR: {str(e)}"
#         )

#         return {

#             "success": False,

#             "error": str(e)
#         }
        
        
        
# @app.get("/")
# def home():
#     return {"message": "Railway backend working"}




from fastapi import FastAPI
from pydantic import BaseModel
import traceback

from app.scraper import scrape_all_jobs
from app.rag_pipeline import (
    load_jobs,
    retrieve_jobs
)
from app.llm_reasoning import (
    generate_reasoning
)

# =========================================
# FastAPI App
# =========================================

app = FastAPI(
    title="Mini Jobright AI",
    version="1.0.0"
)

print("FASTAPI SERVER STARTED")

# =========================================
# Global Variables
# =========================================

faiss_ready = False

# =========================================
# Request Model
# =========================================

class ResumeRequest(BaseModel):
    resume: str

# =========================================
# Root Route
# =========================================

@app.get("/")
def home():

    return {
        "success": True,
        "message": "Mini Jobright AI Backend Running"
    }

# =========================================
# Health Check Route
# =========================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "faiss_ready": faiss_ready
    }

# =========================================
# Refresh Jobs Route
# =========================================

@app.get("/refresh-jobs")
def refresh_jobs():

    global faiss_ready

    try:

        print("\n===================================")
        print("FETCHING LATEST JOBS...")
        print("===================================")

        # Scrape latest jobs
        scrape_all_jobs()

        print("\n===================================")
        print("BUILDING FAISS DATABASE...")
        print("===================================")

        # Rebuild FAISS
        load_jobs()

        faiss_ready = True

        return {
            "success": True,
            "message": "Jobs refreshed successfully"
        }

    except Exception as e:

        traceback.print_exc()

        return {
            "success": False,
            "error": str(e)
        }

# =========================================
# Match Jobs Route
# =========================================

@app.post("/match")
def match_jobs(request: ResumeRequest):

    try:

        print("MATCH REQUEST RECEIVED")

        # =====================================
        # TEMP STATIC RESULTS
        # =====================================

        matches = [

            {
                "job_title": "Python AI Engineer",

                "company": "OpenAI",

                "location": "Remote",

                "source": "Demo",

                "job_url": "https://openai.com/careers",

                "match_percentage": 96,

                "reasoning": (
                    "Your resume strongly matches "
                    "Python, FastAPI, AI, "
                    "machine learning, and NLP skills."
                )
            },

            {
                "job_title": "Machine Learning Developer",

                "company": "Google",

                "location": "Remote",

                "source": "Demo",

                "job_url": "https://careers.google.com",

                "match_percentage": 91,

                "reasoning": (
                    "Your background aligns with "
                    "AI engineering and backend "
                    "development requirements."
                )
            }
        ]

        return {

            "success": True,

            "total_matches": len(matches),

            "matches": matches
        }

    except Exception as e:

        import traceback

        traceback.print_exc()

        return {

            "success": False,

            "error": str(e)
        }