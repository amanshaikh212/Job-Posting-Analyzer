from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

# Import core logic from the new modules
from scraper import scrape_data
from analyzer import analyze_skills
from config import SIMULATED_JOB_POSTINGS_HTML, SKILLS_TO_ANALYZE

# Initialize the FastAPI Application
app = FastAPI(
    title = "Job Posting Analyzer API",
    description="A prototype API to analyze simulated job postings and identify key skills",
    version="1.0.0"
)

# --- API Data Models ---
class SkillAnalysisResponse(BaseModel):
    """
    Pydantic model for the API response.
    It contains a dictionary of skills and their frequencies.
    """
    skill_frequency: Dict[str, int]
    total_jobs_analyzed: int

# -- FastAPI endpoints
@app.get("/", tags=["Home"], summary="Health Check")
def read_root():
    """
    A simple endpoint to confirm the API is running.
    """
    return {"message": "Welcome to the Job Posting Analyzer API. Visit /docs for documentation."}

@app.get(
    "/analyze_jobs",
    response_model=SkillAnalysisResponse,
    tags=["Analysis"],
    summary="Analyze job postings for skills",
    description="Simulates scraping job postings and returns the frequency of key technical skills."
)
async def analyze_job_data():
    """
    Analyzes the simulated job postings for the most frequent skills.

    This function orchestrates the entire process:
    1. Simulates scraping data from a web page.
    2. Analyzes the extracted job descriptions.
    3. Returns the analysis results in a structured JSON format.
    """
    try:
        # Step 1. Simulate Data Scraping
        job_descriptions = scrape_data(SIMULATED_JOB_POSTINGS_HTML)
        
        if not job_descriptions:
            raise HTTPException(status_code=404, detail="No job descriptions found in the simulated data.")
        
        # Step 2. Analyze skills from the descriptions
        skill_counts = analyze_skills(job_descriptions, SKILLS_TO_ANALYZE)

        # Step 3. Return the structured response
        return SkillAnalysisResponse(
            skill_frequency=skill_counts,
            total_jobs_analyzed=len(job_descriptions)
        )

    except Exception as e:
        print(f"An error occured: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during analysis.")