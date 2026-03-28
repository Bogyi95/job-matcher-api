from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_match(cv_skills, job_skills):
    if not job_skills:
        return 0
    matched = set(cv_skills) & set(job_skills)
    base_score = len(matched) / len(job_skills)

    score = min((base_score) * 100, 100)

    return round(score, 2), list(matched)

def calculate_ai_match(cv_text, job_description):
    cv_embedding = model.encode(cv_text, convert_to_tensor=True)
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    similarity = util.cos_sim(cv_embedding, job_embedding).item()

    score = round(similarity * 100, 2)
    return score