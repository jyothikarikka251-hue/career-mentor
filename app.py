import streamlit as st

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from ai_analyzer import analyze_career
from roadmap_generator import generate_roadmap
from interview_generator import generate_interview_questions
from ats_score import calculate_ats_score

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="CareerAI",
    page_icon="🫶",
    layout="wide"
)

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:
    st.title("🫶 CareerAI")

    st.markdown("""
    ### Your Career Growth Partner

    🌱 Learn

    🎯 Focus

    📈 Grow

    🚀 Succeed

    ---
    
    CareerAI helps you:

    ✅ Analyze resumes
    
    ✅ Find skill gaps
    
    ✅ Build learning roadmaps
    
    ✅ Prepare for interviews
    
    ✅ Improve ATS readiness
    """)

# -----------------------------
# HEADER
# -----------------------------

st.title("🫶 CareerAI")

st.markdown("""
## Your Supportive AI Career Mentor

Helping you discover opportunities, build skills, and grow confidently toward your dream career.
""")

st.success("""
🌟 Welcome to CareerAI

You're not just uploading a resume.

You're taking the next step in your career journey.

Upload your resume and let AI guide your growth.
""")

# -----------------------------
# UPLOAD
# -----------------------------

st.markdown("## 📄 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload PDF Resume",
    type=["pdf"]
)

# -----------------------------
# TARGET ROLE
# -----------------------------

st.markdown("## 🎯 Choose Your Dream Career")

target_role = st.selectbox(
    "",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Generative AI Engineer",
        "Prompt Engineer",
        "Software Engineer",
        "Java Developer",
        "Python Developer",
        "Frontend Developer",
        "Backend Developer",
        "Full Stack Developer",
        "Cloud Engineer",
        "DevOps Engineer",
        "Cyber Security Analyst",
        "Blockchain Developer",
        "Mobile App Developer",
        "UI/UX Designer",
        "Product Manager",
        "Game Developer"
    ]
)

analyze_btn = st.button(
    "🚀 Analyze My Career Path",
    use_container_width=True
)

# -----------------------------
# ANALYSIS
# -----------------------------

if uploaded_file and analyze_btn:

    with st.spinner("Analyzing your resume..."):

        resume_text = extract_resume_text(uploaded_file)

        skills = extract_skills(resume_text)

        analysis = analyze_career(
            skills,
            target_role
        )

        roadmap = generate_roadmap(
            skills,
            target_role
        )

        questions = generate_interview_questions(
            target_role
        )

        ats_score, suggestions = calculate_ats_score(
            skills,
            resume_text
        )

    # -----------------------------
    # METRICS
    # -----------------------------

    st.markdown("## 📊 Career Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🧠 Skills",
            len(skills)
        )

    with col2:
        st.metric(
            "📄 ATS Score",
            ats_score
        )

    with col3:
        st.metric(
            "🎯 Target Role",
            target_role
        )

    with col4:
        st.metric(
            "💡 Suggestions",
            len(suggestions)
        )

    # -----------------------------
    # CAREER READINESS
    # -----------------------------

    st.markdown("## 🚀 Career Readiness")

    st.progress(ats_score / 100)

    st.write(
        f"Career Readiness Score: {ats_score}%"
    )

    # -----------------------------
    # ENCOURAGEMENT
    # -----------------------------

    if ats_score >= 80:

        st.balloons()

        st.success("""
        🌟 Excellent Progress

        Your resume is already strong.

        Focus on advanced projects,
        networking,
        and interview preparation.
        """)

    elif ats_score >= 60:

        st.info("""
        🌱 You're Growing Well

        A few improvements can significantly increase
        your opportunities.
        """)

    else:

        st.warning("""
        💪 Every Expert Started Somewhere

        Follow the roadmap and keep learning.
        Growth happens one step at a time.
        """)

    # -----------------------------
    # TABS
    # -----------------------------

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📊 Career Analysis",
            "🧠 Skills",
            "🛣️ Roadmap",
            "🎤 Interview",
            "📄 ATS"
        ]
    )

    with tab1:
        st.write(analysis)

    with tab2:
        st.write(skills)

    with tab3:
        st.write(roadmap)

    with tab4:
        st.write(questions)

    with tab5:

        if ats_score >= 80:
            st.success(
                f"ATS Score: {ats_score}/100"
            )

        elif ats_score >= 60:
            st.warning(
                f"ATS Score: {ats_score}/100"
            )

        else:
            st.error(
                f"ATS Score: {ats_score}/100"
            )

        st.subheader("💡 Improvement Suggestions")

        for item in suggestions:
            st.write(f"✅ {item}")

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.markdown("""
### 💖 Our Mission

CareerAI exists to support learners and professionals
through every stage of their growth journey.

We believe everyone deserves clear guidance,
personalized learning paths,
and confidence in their future.
""")

st.caption(
    "🫶 CareerAI • Supporting Every Step of Your Career Journey"
)