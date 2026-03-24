SKILLS = [
    "python", "django", "flask", "fastapi",
    "sql", "postgresql", "mysql",
    "docker", "kubernetes",
    "aws", "azure", "gcp",
    "git", "ci/cd",
    "react", "typescript",
    "pytorch", "tensorflow",
    "microservices", "api"
]

def extract_skills(text):
    text = text.lower()

    found = set()

    for skill in SKILLS:
        if skill in text:
            found.add(skill)

    return list(found)