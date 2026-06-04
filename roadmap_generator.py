import google.generativeai as genai

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_roadmap(skills, role):

    prompt = f"""
Student Skills:
{skills}

Target Role:
{role}

Create a detailed 12-week roadmap.
"""

    response = model.generate_content(prompt)

    return response.text