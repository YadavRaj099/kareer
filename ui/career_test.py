import streamlit as st
from engine.recommender import recommend

def show_career_test():

    st.title("Career Path Finder")

    st.write(
        "Answer a few questions so Kareer can determine the best career pathways for you."
    )

    st.divider()

    # =========================
    # STREAM
    # =========================

    stream = st.selectbox(
        "Which academic stream interests you the most?",
        ["Science", "Commerce", "Arts"]
    )

    # =========================
    # WORK STYLE
    # =========================

    work_style = st.selectbox(
        "What type of work do you enjoy?",
        ["Analytical", "Creative", "Helping People"]
    )

    # =========================
    # RISK
    # =========================

    risk = st.selectbox(
        "What is your risk tolerance?",
        ["Low", "Medium", "High"]
    )

    # =========================
    # SKILLS
    # =========================

    skills = st.multiselect(
        "Which skills interest you?",
        [
            "Math",
            "Programming",
            "Design",
            "Communication",
            "Biology",
            "Business"
        ]
    )

    st.divider()

    # =========================
    # SUBMIT
    # =========================

    if st.button("Find My Career Path", use_container_width=True):

        user_answers = {
            "stream": stream.lower(),
            "work_style": work_style.lower(),
            "risk": risk.lower(),
            "skills": [s.lower() for s in skills]
        }

        results = recommend(user_answers)

        st.session_state.results = results
        st.session_state.page = "results"

        st.rerun()