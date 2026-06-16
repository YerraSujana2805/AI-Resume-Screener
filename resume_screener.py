resumes = [
    {"name": "John", "skills": ["Python", "ML", "SQL"]},
    {"name": "Alice", "skills": ["Java", "HTML", "CSS"]},
    {"name": "Bob", "skills": ["Python", "Data Science", "ML"]}
]

required_skills = ["Python", "ML"]

print("Suitable Candidates:")

for candidate in resumes:
    score = 0

    for skill in required_skills:
        if skill in candidate["skills"]:
            score += 1

    if score >= 2:
        print(candidate["name"], "- Selected")