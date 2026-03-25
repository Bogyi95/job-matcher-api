from fastapi import FastAPI
from app.api.jobs import router as jobs_router
from app.api.cv import router as cv_router
from app.api.match import router as match_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(jobs_router)
app.include_router(cv_router)
app.include_router(match_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API running!"}