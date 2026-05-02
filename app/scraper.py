import requests
import json

# =========================================
# Fetch Jobs from RemoteOK
# =========================================

def fetch_remoteok_jobs():

    url = "https://remoteok.com/api"

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20
    )

    data = response.json()

    jobs = []

    for item in data[1:]:

        try:

            job = {
                "title": item.get("position", ""),
                "company": item.get("company", ""),
                "description": item.get("description", "")[:2000],
                "location": item.get("location", "Remote"),
                "source": "RemoteOK",
                "url": item.get("url", "")
            }

            jobs.append(job)

        except Exception:
            pass

    return jobs

# =========================================
# Fetch Jobs from Arbeitnow
# =========================================

def fetch_arbeitnow_jobs():

    url = "https://www.arbeitnow.com/api/job-board-api"

    response = requests.get(
        url,
        timeout=20
    )

    data = response.json()

    jobs = []

    for item in data["data"]:

        try:

            job = {
                "title": item.get("title", ""),
                "company": item.get("company_name", ""),
                "description": item.get("description", "")[:2000],
                "location": item.get("location", ""),
                "source": "Arbeitnow",
                "url": item.get("url", "")
            }

            jobs.append(job)

        except Exception:
            pass

    return jobs

# =========================================
# Clean Jobs
# =========================================

def clean_jobs(jobs):

    cleaned = []

    for job in jobs:

        if (
            len(job["title"]) > 2
            and len(job["description"]) > 20
        ):

            cleaned.append(job)

    return cleaned

# =========================================
# Save Jobs
# =========================================

def save_jobs(jobs):

    with open(
        "data/jobs.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            jobs,
            file,
            indent=4,
            ensure_ascii=False
        )

# =========================================
# Main Scraper Function
# =========================================

def scrape_all_jobs():

    print("Fetching RemoteOK jobs...")

    remoteok_jobs = fetch_remoteok_jobs()

    print(f"Fetched {len(remoteok_jobs)} RemoteOK jobs")

    print("Fetching Arbeitnow jobs...")

    arbeitnow_jobs = fetch_arbeitnow_jobs()

    print(f"Fetched {len(arbeitnow_jobs)} Arbeitnow jobs")

    # Combine jobs
    all_jobs = remoteok_jobs + arbeitnow_jobs

    # LIMIT JOBS
    all_jobs = all_jobs[:100]

    cleaned_jobs = clean_jobs(all_jobs)

    save_jobs(cleaned_jobs)

    print(f"Saved {len(cleaned_jobs)} jobs")

    return cleaned_jobs