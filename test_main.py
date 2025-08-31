from fastapi.testclient import TestClient
from main import app

# Create a TestClient instance for your FastAPI application
client = TestClient(app)

def test_read_root():
    """
    Test the health check endpoint at '/'.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Job Posting Analyzer API. Visit /docs for documentation."}

def test_analyze_job_data():
    """
    Test the main analysis endpoint at '/analyze_jobs'.
    """
    response = client.get("/analyze_jobs")
    assert response.status_code == 200
    # Check that the response contains the expected keys and types
    data = response.json()
    assert "skill_frequency" in data
    assert "total_jobs_analyzed" in data
    assert isinstance(data["skill_frequency"], dict)
    assert isinstance(data["total_jobs_analyzed"], int)
    assert data["total_jobs_analyzed"] > 0
    
