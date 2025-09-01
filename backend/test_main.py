from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """
    Test the health check endpoint at '/'.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Job Posting Analyzer API is running!"}

def test_analyze_job_data_with_skills():
    """
    Test the analysis endpoint at '/analyze_jobs' with a custom skill list.
    """
    payload = {"skills": ["Python", "FastAPI", "Docker"]}
    response = client.post("/analyze_jobs", json=payload)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "skill_frequency" in data
    assert "total_jobs_analyzed" in data
    assert isinstance(data["skill_frequency"], dict)
    assert isinstance(data["total_jobs_analyzed"], int)
    assert data["total_jobs_analyzed"] > 0

    # Check that requested skills exist in the response
    for skill in payload["skills"]:
        assert skill.lower() in data["skill_frequency"]

def test_analyze_job_data_with_empty_skills():
    """
    Test the analysis endpoint when no skills are provided.
    """
    payload = {"skills": []}
    response = client.post("/analyze_jobs", json=payload)
    
    assert response.status_code == 200
    
    data = response.json()
    # No skills means the dictionary should be empty
    assert data["skill_frequency"] == {}
    assert isinstance(data["total_jobs_analyzed"], int)
    assert data["total_jobs_analyzed"] > 0
