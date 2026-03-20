from app.services.skill_extractor import extract_skills

def fetch_jobs():

    jobs = [
        {
            "title": "Python Backend Developer",
            "company": "TechCorp",
            "description": "Looking for Python developer with FastAPI and Docker"
        }
    ]
    
    for job in jobs:
        job["skills"] = extract_skills(job["description"])

    return jobs