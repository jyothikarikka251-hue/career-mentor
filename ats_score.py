def calculate_ats_score(skills, resume_text):

    score = 0
    suggestions = []

    # Skills Score (max 50)
    skill_score = min(len(skills) * 5, 50)
    score += skill_score

    # Resume Length Score (max 20)
    word_count = len(resume_text.split())

    if word_count >= 300:
        score += 20
    elif word_count >= 200:
        score += 15
    elif word_count >= 100:
        score += 10
    else:
        score += 5
        suggestions.append(
            "Add more details about your education, projects, and experience."
        )

    # Projects Check
    if "project" in resume_text.lower():
        score += 10
    else:
        suggestions.append(
            "Add a Projects section to showcase practical work."
        )

    # Education Check
    if "education" in resume_text.lower():
        score += 10
    else:
        suggestions.append(
            "Include an Education section."
        )

    # Contact Information Check
    if "@" in resume_text:
        score += 5
    else:
        suggestions.append(
            "Add a professional email address."
        )

    # GitHub Check
    if "github" in resume_text.lower():
        score += 5
    else:
        suggestions.append(
            "Add your GitHub profile link."
        )

    # LinkedIn Check
    if "linkedin" in resume_text.lower():
        score += 5
    else:
        suggestions.append(
            "Add your LinkedIn profile."
        )

    # Cap score at 100
    if score > 100:
        score = 100

    return score, suggestions