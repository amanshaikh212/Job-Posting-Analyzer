import re
from typing import Dict

def analyze_skills(job_descriptions: list, skills_to_find: list) -> Dict[str, int]:
    """
    Analyzes a list of job descriptions to count the frequency of specific skills.

    Args:
        job_descriptions (list): A list of job description strings.
        skills_to_find (list): A list of skills (strings) to search for.

    Returns:
        Dict[str, int]: A dictionary mapping each skill to its frequency count.
    """
    skill_counts = {skill.lower(): 0 for skill in skills_to_find}
    for description in job_descriptions:
        # Normalize text to lowercase for case-insensitive matching
        normalized_description = description.lower()

        for skill in skills_to_find:
            # Use regex to find whole words to avoid matching substrings
            # e.g., 'python' in 'cython'. The \b is for word boundaries.
            if re.search(r'\b' + re.escape(skill.lower()) + r'\b', normalized_description):
                skill_counts[skill.lower()] += 1
    return skill_counts