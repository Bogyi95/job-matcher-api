from fastapi import APIRouter
from pydantic import BaseModel
from app.services.matcher import calculate_match
from app.scraper.jobs_scraper import fetch_jobs
from app.services.skill_extractor import extract_skills

router = APIRouter()

class MatchRequest(BaseModel):
    cv_text: str

@router.post("/match")
def match_jobs(req: MatchRequest):
    cv_skills = extract_skills(req.cv_text)
    jobs = fetch_jobs()
    results = []

    for job in jobs:
        job_skills = job.get("skills", [])

        score, matched = calculate_match(cv_skills, job_skills)
        missing_skills = list(set(job_skills) - set(cv_skills))

        results.append({
            "title": job["title"],
            "company": job["company"],
            "score": score,
            "matched_skills": matched,
            "missing_skills": list(set(job_skills) - set(cv_skills)),
            "improvement_tips": [
                f"Consider learning {skill}" for skill in missing_skills
            ]
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return results[:5]