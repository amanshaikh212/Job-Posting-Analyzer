# This HTML string simulates a scraped job board page. In a real-world scenario,
# you would use a library like 'requests' to fetch this from a live website.
SIMULATED_JOB_POSTINGS_HTML = """
<!DOCTYPE html>
<html>
<body>
  <div class="job-listing">
    <h2 class="job-title">Senior Python Developer</h2>
    <p class="job-description">We are looking for a skilled Python developer to build robust backend systems. Experience with FastAPI and SQLAlchemy is a plus. Knowledge of AWS and Docker is required.</p>
  </div>
  <div class="job-listing">
    <h2 class="job-title">Data Scientist</h2>
    <p class="job-description">Join our team of data scientists. We use Python, Pandas, and Scikit-learn to analyze large datasets. Previous experience with a Dockerized environment is beneficial.</p>
  </div>
  <div class="job-listing">
    <h2 class="job-title">Backend Engineer</h2>
    <p class="job-description">Build scalable services using Python and FastAPI. Familiarity with cloud platforms like Google Cloud and CI/CD pipelines (Jenkins) is essential. Strong skills in database management are a must.</p>
  </div>
</body>
</html>
"""

# A list of skills to search for. You can easily expand this list.
SKILLS_TO_ANALYZE = [
    "Python", "FastAPI", "SQL", "Docker", "AWS", "Google Cloud",
    "Azure", "Pandas", "Django", "Flask", "Kubernetes"
]