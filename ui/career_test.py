import streamlit as st
from engine.recommender import recommend
from engine.questions import get_questions


def show_career_test():

    st.title("Career Path Finder")

    st.write(
        "Answer a few questions so Kareer can determine the best career pathways for you."
    )

    st.divider()

    questions = get_questions()

    answers = {}

    for key, q in questions.items():

        if q["type"] == "single":

            answers[key] = st.selectbox(
                q["question"],
                q["options"]
            )

        elif q["type"] == "multi":

            answers[key] = st.multiselect(
                q["question"],
                q["options"]
            )

    st.divider()

    if st.button("Find My Career Path", use_container_width=True):

        user_answers = {}

        for k, v in answers.items():

            if isinstance(v, list):
                user_answers[k] = [str(x).lower() for x in v]
            else:
                user_answers[k] = str(v).lower()

        results = recommend(user_answers)

        st.session_state.results = results
        st.session_state.page = "results"

        st.rerun()