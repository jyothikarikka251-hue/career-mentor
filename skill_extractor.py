def extract_skills(resume_text):

    skills_db = [
        "Python",
        "Java",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "SQL",
        "Git",
        "Docker",
        "TensorFlow",
        "PyTorch",
        "Machine Learning",
        "Deep Learning"
    ]

    found = []

    for skill in skills_db:

        if skill.lower() in resume_text.lower():
            found.append(skill)

    return found