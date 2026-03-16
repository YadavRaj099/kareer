import streamlit as st


def show_results():

    st.title("Career Results")

    # =========================
    # SAFETY CHECK
    # =========================

    if "results" not in st.session_state:
        st.warning("No results available. Please take the career test first.")
        return

    results = st.session_state.results

    matches = results.get("matches", [])
    similar = results.get("similar_careers", [])

    if not matches:
        st.error("No career matches found.")
        return

    best = matches[0]

    career_name = best.get("career", "Unknown Career")
    score = best.get("score", 0)
    classification = best.get("classification", "Match")

    confidence = min(95, int(60 + score * 5))

    st.markdown("---")

    # =========================
    # HERO MATCH
    # =========================

    st.markdown(
        f"""
        <div style="
            text-align:center;
            padding:35px;
            border-radius:16px;
            background:linear-gradient(145deg,#0f172a,#020617);
            border:1px solid #334155;
        ">

        <div style="font-size:40px;">🏆</div>

        <div style="font-size:32px;font-weight:700;margin-top:10px;">
        {career_name}
        </div>

        <div style="color:#93c5fd;margin-top:6px;">
        {classification}
        </div>

        <div style="margin-top:15px;font-size:18px;">
        Match Confidence: <b>{confidence}%</b>
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =========================
    # WHY THIS FITS YOU
    # =========================

    st.subheader("Why this fits you")

    st.markdown(
        """
• Strong alignment with your interests  
• Your preferred work style matches this career  
• Your selected skills support this path  
• Your environment preferences align well  
"""
    )

    st.write("")

    # =========================
    # ACTION BUTTONS
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("🧭 View Career Roadmap"):

            top_match = matches[0]
            career_data = top_match.get("data")

            if career_data:
                st.session_state.roadmap = career_data
                st.session_state.page = "roadmap"
                st.rerun()

    with col2:
        st.button("📤 Share Result")

    with col3:
        st.button("📸 Screenshot")

    st.markdown("---")

    # =========================
    # ALTERNATIVE CAREERS
    # =========================

    st.subheader("Alternative Careers")

    alt_matches = matches[1:4]

    if alt_matches:

        cols = st.columns(len(alt_matches))

        for i, m in enumerate(alt_matches):

            with cols[i]:

                name = m.get("career", "Career")
                classification = m.get("classification", "")

                st.markdown(
                    f"""
                    <div style="
                        padding:20px;
                        border-radius:12px;
                        border:1px solid #334155;
                        background:#020617;
                        text-align:center;
                    ">

                    <div style="font-weight:600;font-size:18px;">
                    {name}
                    </div>

                    <div style="margin-top:6px;color:#94a3b8;">
                    {classification}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown("---")

    # =========================
    # CAREER DNA
    # =========================

    st.subheader("Your Career DNA")

    dna = {
        "Analytical": 8,
        "Creativity": 5,
        "Technical": 7,
        "Leadership": 6,
        "Communication": 4
    }

    st.bar_chart(dna)

    st.markdown("---")

    # =========================
    # SIMILAR CAREERS
    # =========================

    if similar:

        st.subheader("Careers You May Also Like")

        cols = st.columns(3)

        for i, career in enumerate(similar):

            with cols[i % 3]:

                # SAFE name extraction
                if isinstance(career, dict):
                    name = career.get("name", "Career")
                else:
                    name = str(career).replace("_", " ").title()

                st.markdown(
                    f"""
                    <div style="
                        padding:16px;
                        border-radius:10px;
                        border:1px solid #334155;
                        background:#020617;
                        text-align:center;
                    ">
                    {name}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown("---")

    # =========================
    # RETAKE TEST
    # =========================

    if st.button("🔁 Take Career Test Again"):

        st.session_state.step = 0
        st.session_state.answers = {}
        st.session_state.page = "career_test"

        st.rerun()