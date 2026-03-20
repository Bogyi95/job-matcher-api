from fastapi import APIRouter
from app.scraper.jobs_scraper import fetch_jobs

router = APIRouter()

@router.get("/jobs")
def get_jobs():
    jobs = fetch_jobs()
    return jobs