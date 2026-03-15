import streamlit as st
import time


def show_resume_analyzer():

    # Safe imports (prevents app crash if backend fails)
    try:
        from resume_analyzer.analyzer import analyze_resume, generate_summary
        from resume_analyzer.role_skills import list_available_roles
    except Exception as e:
        st.error("Backend module failed to load.")
        st.code(str(e))
        return

    # ==================================================
    # HERO
    # ==================================================

    st.markdown(
        """
        <h1 style="font-size:44px;margin-bottom:5px;">
        AI Resume Skill Analyzer
        </h1>

        <p style="color:#94a3b8;font-size:17px;margin-top:0;">
        Upload your resume and discover your career readiness,
        skill gaps, and interview probability.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

    # ==================================================
    # UPLOAD PANEL
    # ==================================================

    with st.container():

        st.markdown(
            """
            <div style="
                border:1px solid #1e293b;
                padding:28px;
                border-radius:18px;
                background:linear-gradient(180deg,#0f172a,#020617);
            ">
            <h3 style="margin-bottom:6px;">Upload Resume</h3>
            <p style="color:#94a3b8;margin-top:0;">
            Supported formats: PDF, DOCX, JPG, PNG
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        uploaded_file = st.file_uploader(
            " ",
            type=["pdf", "docx", "jpg", "jpeg", "png"]
        )

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    # ==================================================
    # ROLE SELECTION
    # ==================================================

    roles = list_available_roles()

    target_role = st.selectbox(
        "🎯 Target Career",
        roles
    )

    analyze = st.button(
        "🚀 Analyze Resume",
        use_container_width=True
    )

    # ==================================================
    # START ANALYSIS
    # ==================================================

    if analyze:

        if not uploaded_file:
            st.warning("Please upload a resume first.")
            return

        # ==================================================
        # LOADING SIMULATION
        # ==================================================

        progress_bar = st.progress(0)
        status = st.empty()

        steps = [
            "Reading resume...",
            "Extracting skills...",
            "Analyzing career alignment...",
            "Calculating readiness score...",
            "Estimating interview probability...",
            "Generating insights..."
        ]

        for i, step in enumerate(steps):
            status.info(f"⚙️ {step}")
            progress_bar.progress((i + 1) / len(steps))
            time.sleep(0.4)

        status.empty()
        progress_bar.empty()

        # ==================================================
        # RUN ANALYSIS
        # ==================================================

        try:

            analysis = analyze_resume(uploaded_file, target_role)
            summary = generate_summary(analysis)

        except Exception as e:

            st.error("Error analyzing resume.")
            st.code(str(e))
            return

        st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)

        # ==================================================
        # SCORE PANEL
        # ==================================================

        st.markdown("### 📊 Analysis Summary")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Resume Score",
            f"{summary.get('resume_score',0)}%"
        )

        col2.metric(
            "Readiness",
            summary.get("readiness","Unknown")
        )

        col3.metric(
            "Interview Probability",
            summary.get("interview_probability","Unknown")
        )

        st.markdown("---")

        # ==================================================
        # DETECTED SKILLS
        # ==================================================

        st.subheader("🧠 Detected Skills")

        skills = analysis.get("skills", {}).get("skills", [])

        if skills:

            tags = ""

            for skill in skills:
                tags += f"""
                <span style="
                    padding:6px 14px;
                    border-radius:999px;
                    border:1px solid #334155;
                    margin-right:6px;
                    display:inline-block;
                    margin-bottom:8px;
                    font-size:13px;
                    background:#020617;
                ">
                {skill}
                </span>
                """

            st.markdown(tags, unsafe_allow_html=True)

        else:
            st.info("No skills detected in resume.")

        st.markdown("---")

        # ==================================================
        # SKILL GAPS
        # ==================================================

        st.subheader("⚠️ Skill Gaps")

        gaps = summary.get("missing_skills", [])

        if gaps:
            for gap in gaps:
                st.warning(gap)
        else:
            st.success("Your resume already covers required skills.")

        st.markdown("---")

        # ==================================================
        # RECOMMENDED CAREERS
        # ==================================================

        st.subheader("🚀 Recommended Careers")

        rec = summary.get("recommended_roles", [])

        if rec:
            for role in rec:
                st.markdown(f"• **{role.replace('_',' ').title()}**")
        else:
            st.info("No alternative roles detected.")

        st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

        if st.button("Analyze Another Resume", use_container_width=True):
            st.rerun()