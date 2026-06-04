import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_interview_questions(role):

    prompt = f"""
Generate 10 interview questions for a {role}.

Include:
- Beginner questions
- Intermediate questions
- Advanced questions
- HR questions
"""

    response = model.generate_content(prompt)

    return response.text