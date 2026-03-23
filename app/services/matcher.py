def calculate_match(cv_skills, job_skills):
    if not job_skills:
        return 0
    matched = set(cv_skills) & set(job_skills)
    score = len(matched) / len(job_skills) * 100
    return round(score, 2), list(matched)