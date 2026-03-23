from fastapi import APIRouter
from pydantic import BaseModel
from app.services.skill_extractor import extract_skills

router = APIRouter()

class CVRequest(BaseModel):
    text: str

@router.post("/cv")
def analyze_cv(cv: CVRequest):
    skills = extract_skills(cv.text)
    return {
        "skills": skills
    }