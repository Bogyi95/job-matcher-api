from fastapi import APIRouter
from pydantic import BaseModel
from app.services.matcher import calculate_match, calculate_ai_match
from app.services.skill_extractor import extract_skills
from app.scraper.playwright_scraper import get_jobs_cached

router = APIRouter()

class MatchRequest(BaseModel):
    cv_text: str

@router.post("/match")
def match_jobs(req: MatchRequest):
    cv_skills = extract_skills(req.cv_text)
    jobs = get_jobs_cached()
    results = []

    for job in jobs:
        job_skills = job.get("skills", [])

        skill_score, matched = calculate_match(cv_skills, job_skills)
        #add option to upload cv so ai calculator can better estimate match!
        ai_score = calculate_ai_match(req.cv_text, job["description"])
        score = round(0.5 * ai_score + 0.5 * skill_score, 2)
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
    return results[:20]