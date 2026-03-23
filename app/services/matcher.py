def calculate_match(cv_skills, job_skills):
    if not job_skills:
        return 0
    matched = set(cv_skills) & set(job_skills)
    base_score = len(matched) / len(job_skills)

    bonus = 0.1 if "python" in matched else 0 

    score = min((base_score + bonus) * 100, 100)

    return round(score, 2), list(matched)