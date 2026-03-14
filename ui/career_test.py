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
    runner_position = int(progress * 100)

    # ----------------------------
    # RUNNER PROGRESS BAR
    # ----------------------------

    st.markdown(
        f"""
        <div style="
            width:100%;
            background:#1e293b;
            border-radius:10px;
            height:22px;
            position:relative;
            margin-bottom:20px;
        ">
            <div style="
                width:{runner_position}%;
                background:#3b82f6;
                height:100%;
                border-radius:10px;
                transition:width 0.4s ease;
            "></div>

            <div style="
                position:absolute;
                left:{runner_position}%;
                transform:translateX(-50%);
                top:-12px;
                font-size:22px;
            ">🚀</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ----------------------------
    # CURRENT QUESTION
    # ----------------------------

    key, q = questions[step]

    st.subheader(q["question"])

    answer = None

    # ----------------------------
    # CARD STYLE OPTIONS
    # ----------------------------

    if q["type"] == "single":

        cols = st.columns(len(q["options"]))

        for i, option in enumerate(q["options"]):

            with cols[i]:

                if st.button(option, key=f"{key}_{i}"):

                    st.session_state.answers[key] = option
                    st.rerun()

        answer = st.session_state.answers.get(key)

    elif q["type"] == "multi":

        answer = st.multiselect(
            "",
            q["options"],
            default=st.session_state.answers.get(key, [])
        )

        st.session_state.answers[key] = answer

    # ----------------------------
    # OPTIONAL AI TEXTBOX
    # ----------------------------

    st.markdown("#### Tell Kareer more about yourself (optional)")

    notes = st.text_area(
        "",
        placeholder="Example: I like startups, technology, building products, helping people, etc.",
        key=f"notes_{key}"
    )

    st.session_state.answers[f"{key}_notes"] = notes

    st.divider()

    # ----------------------------
    # NAVIGATION BUTTONS
    # ----------------------------

    col1, col2, col3 = st.columns([1,2,1])

    with col1:

        if step > 0:

            if st.button("⬅ Previous", use_container_width=True):

                st.session_state.step -= 1
                st.rerun()

    with col3:

        if step < total - 1:

            if st.button("Next ➡", use_container_width=True):

                st.session_state.step += 1
                st.rerun()

        else:

            if st.button("Show My Career Path 🚀", use_container_width=True):

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