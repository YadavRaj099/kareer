import streamlit as st
from engine.questions import get_questions
from engine.recommender import recommend


def show_career_test():

    questions = list(get_questions().items())

    # -----------------------------
    # SESSION STATE
    # -----------------------------

    if "step" not in st.session_state:
        st.session_state.step = 0

    if "answers" not in st.session_state:
        st.session_state.answers = {}

    step = st.session_state.step
    total = len(questions)

    # -----------------------------
    # PAGE TITLE
    # -----------------------------

    st.title("Career Path Finder")

    # -----------------------------
    # STEP INDICATOR
    # -----------------------------

    st.caption(f"Question {step + 1} of {total}")

    # -----------------------------
    # PROGRESS BAR
    # -----------------------------

    progress = (step + 1) / total
    runner_position = int(progress * 100)

    st.markdown(
        f"""
<div style="width:100%;background:#1e293b;border-radius:12px;height:24px;position:relative;margin-bottom:35px;">

<div style="width:{runner_position}%;background:#22c55e;height:100%;border-radius:12px;transition:width .4s ease;"></div>

<div style="position:absolute;left:{runner_position}%;transform:translateX(-50%);top:-14px;font-size:22px;">
🚀
</div>

</div>
""",
        unsafe_allow_html=True
    )

    # -----------------------------
    # CURRENT QUESTION
    # -----------------------------

    key, q = questions[step]

    st.markdown(
        f"""
        <div style="font-size:22px;font-weight:600;margin-bottom:20px;">
        {q["question"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------
    # SINGLE SELECT (MCQ STYLE)
    # -----------------------------

    if q["type"] == "single":

        selected = st.session_state.answers.get(key)

        for i, option in enumerate(q["options"]):

            is_selected = selected == option

            button_label = option

            if is_selected:
                button_label = f"✅ {option}"

            if st.button(
                button_label,
                use_container_width=True,
                key=f"{key}_{i}"
            ):
                st.session_state.answers[key] = option
                st.rerun()

    # -----------------------------
    # MULTI SELECT
    # -----------------------------

    elif q["type"] == "multi":

        answer = st.multiselect(
            "",
            q["options"],
            default=st.session_state.answers.get(key, [])
        )

        st.session_state.answers[key] = answer

    # -----------------------------
    # OPTIONAL NOTES
    # -----------------------------

    st.write("")
    st.markdown("##### Tell Kareer more about yourself (optional)")

    notes = st.text_area(
        "",
        placeholder="Example: I enjoy building things, solving problems, startups, technology, etc.",
        key=f"notes_{key}"
    )

    st.session_state.answers[f"{key}_notes"] = notes

    st.write("")
    st.divider()

    # -----------------------------
    # NAVIGATION BUTTONS
    # -----------------------------

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