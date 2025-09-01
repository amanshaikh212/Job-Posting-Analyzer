from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List

from scraper import scrape_data
from analyzer import analyze_skills
from config import SIMULATED_JOB_POSTINGS_HTML

app = FastAPI(
    title="Job Posting Analyzer API",
    description="API to analyze simulated job postings for requested skills",
    version="2.1.0"
)

# ----------------- CORS Middleware -----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In dev, allow all origins (can restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------------------------------------

class SkillRequest(BaseModel):
    skills: List[str]

class SkillAnalysisResponse(BaseModel):
    skill_frequency: Dict[str, int]
    total_jobs_analyzed: int

@app.get("/", tags=["Home"])
def read_root():
    return {"message": "Job Posting Analyzer API is running!"}

@app.post(
    "/analyze_jobs",
    response_model=SkillAnalysisResponse,
    tags=["Analysis"],
    summary="Analyze job postings for custom skills"
)
async def analyze_job_data(request: SkillRequest):
    try:
        job_descriptions = scrape_data(SIMULATED_JOB_POSTINGS_HTML)
        if not job_descriptions:
            raise HTTPException(status_code=404, detail="No job descriptions found.")

        # ✅ Normalize + deduplicate skills
        unique_skills = list({skill.strip().lower() for skill in request.skills if skill.strip()})

        if not unique_skills:
            return SkillAnalysisResponse(skill_frequency={}, total_jobs_analyzed=len(job_descriptions))

        # Run analysis with cleaned skills
        skill_counts = analyze_skills(job_descriptions, unique_skills)

        return SkillAnalysisResponse(
            skill_frequency=skill_counts,
            total_jobs_analyzed=len(job_descriptions)
        )
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during analysis.")
