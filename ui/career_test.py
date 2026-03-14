import streamlit as st
from engine.questions import get_questions
from engine.recommender import recommend


def show_career_test():

    questions = list(get_questions().items())

    if "step" not in st.session_state:
        st.session_state.step = 0

    if "answers" not in st.session_state:
        st.session_state.answers = {}

    step = st.session_state.step
    total = len(questions)

    st.title("Career Path Finder")

    progress = (step + 1) / total

    # Runner Progress
    runner_position = int(progress * 100)

    st.markdown(
        f"""
        <div style="
            width:100%;
            background:#1e293b;
            border-radius:10px;
            height:22px;
            position:relative;
        ">
            <div style="
                width:{runner_position}%;
                background:#3b82f6;
                height:100%;
                border-radius:10px;
            "></div>
            <div style="
                position:absolute;
                left:{runner_position}%;
                top:-8px;
                font-size:22px;
            ">🚀</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    key, q = questions[step]

    st.subheader(q["question"])

    if q["type"] == "single":

        answer = st.radio(
            "",
            q["options"],
            index=None
        )

    elif q["type"] == "multi":

        answer = st.multiselect(
            "",
            q["options"]
        )

    st.session_state.answers[key] = answer

    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        if step > 0:
            if st.button("⬅ Previous"):
                st.session_state.step -= 1
                st.rerun()

    with col3:
        if step < total - 1:

            if st.button("Next ➡"):
                st.session_state.step += 1
                st.rerun()

        else:

            if st.button("Show My Career Path 🚀"):

                user_answers = {}

                for k, v in st.session_state.answers.items():

                    if isinstance(v, list):
                        user_answers[k] = [str(x).lower() for x in v]
                    else:
                        user_answers[k] = str(v).lower()

                results = recommend(user_answers)

                st.session_state.results = results
                st.session_state.page = "results"

                st.rerun()