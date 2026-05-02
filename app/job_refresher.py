from apscheduler.schedulers.background import (
    BackgroundScheduler
)

from app.scraper import scrape_all_jobs
from app.rag_pipeline import load_jobs

# =========================================
# Refresh Jobs + FAISS
# =========================================

def refresh_jobs():

    print("\nRefreshing jobs...")

    scrape_all_jobs()

    load_jobs()

    print("Refresh completed!")

# =========================================
# Start Scheduler
# =========================================

def start_scheduler():

    scheduler = BackgroundScheduler()

    # Every 30 minutes
    scheduler.add_job(
        refresh_jobs,
        "interval",
        minutes=30
    )

    scheduler.start()

    print(
        "Job refresh scheduler started!"
    )