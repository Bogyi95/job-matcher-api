from fastapi import FastAPI
from app.api.jobs import router as jobs_router
from app.api.cv import router as cv_router
from app.api.match import router as match_router

app = FastAPI()
app.include_router(jobs_router)
app.include_router(cv_router)
app.include_router(match_router)

@app.get("/")
def root():
    return {"message": "API running!"}