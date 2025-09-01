document.getElementById("skillForm").addEventListener("submit", async function(e){
    e.preventDefault();

    const skillsInput = document.getElementById("skills").value;
    const skills = skillsInput.split(",").map(s => s.trim()).filter(Boolean);

    const response = await fetch("http://127.0.0.1:8000/analyze_jobs", {
        method: "POST",
        headers: {"Content-type": "application/json"},
        body: JSON.stringify({skills})
    });

    const data = await response.json();

    const resultsDiv = document.getElementById("results");

    if(response.ok) {
        resultsDiv.innerHTML = `
            <h2>Results</h2>
            <p>Total Jobs Analyzed: ${data.total_jobs_analyzed}</p>
            <ul>
                ${Object.entries(data.skill_frequency)
                    .map(([skill, count]) => `<li>${skill}: ${count}</li>`)
                    .join("")}
            `;
    } else {
        resultsDiv.innerHTML = `<p style="color:red;">Error: ${data.detail}</p>`
    }
});