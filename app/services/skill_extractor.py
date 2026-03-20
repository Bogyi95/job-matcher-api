SKILLS = [
    "python",
    "docker",
    "aws",
    "fastapi",
    "sql",
    "api"
]

def extract_skills(text):
    text = text.lower()

    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found