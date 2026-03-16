import streamlit as st
import plotly.express as px
import pandas as pd
import json


def show_resume_analyzer():

    # ==================================================
    # SAFE IMPORTS
    # ==================================================

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

    st.markdown("""
    <h1 style="font-size:44px;margin-bottom:5px;">
    AI Resume Skill Analyzer
    </h1>

    <p style="color:#94a3b8;font-size:17px;margin-top:0;">
    Upload your resume and discover career readiness,
    skill gaps, and interview probability.
    </p>
    """, unsafe_allow_html=True)

    st.caption(
        "Analysis is based on skill matching and may not fully reflect recruiter evaluation."
    )

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)


    # ==================================================
    # UPLOAD PANEL
    # ==================================================

    st.markdown("""
    <div style="
        border:1px solid #1e293b;
        padding:24px;
        border-radius:18px;
        background:linear-gradient(180deg,#0f172a,#020617);
    ">
    <h3 style="margin-bottom:6px;">Upload Resume</h3>
    <p style="color:#94a3b8;margin-top:0;">
    Supported formats: PDF, DOCX (Max 5MB)
    </p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        " ",
        type=["pdf", "docx"]
    )

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)


    # ==================================================
    # ROLE SELECTION
    # ==================================================

    try:
        roles = sorted(list_available_roles())
    except Exception as e:
        st.error("Failed to load roles database.")
        st.code(str(e))
        return

    if not roles:
        st.warning("No roles available in the career database.")
        return

    # Debug line (remove later if desired)
    # st.write("Loaded roles:", roles)

    st.caption(f"{len(roles)} careers supported")

    st.markdown("### 🎯 Target Career")

    target_role = st.selectbox(
        "Search or select a career role",
        options=roles,
        format_func=lambda x: x.replace("_", " ").title(),
        index=0
    )

    analyze = st.button("Analyze Resume", use_container_width=True)


    # ==================================================
    # START ANALYSIS
    # ==================================================

    if analyze:

        if not uploaded_file:
            st.warning("Please upload a resume first.")
            return

        if uploaded_file.size > 5 * 1024 * 1024:
            st.error("File too large. Please upload a file under 5MB.")
            return

        with st.spinner("Analyzing resume..."):

            try:
                analysis = analyze_resume(uploaded_file, target_role)
                summary = generate_summary(analysis)
            except Exception as e:
                st.error("Error analyzing resume.")
                st.code(str(e))
                return

        st.success("Analysis completed")

        st.markdown("---")


        # ==================================================
        # SCORE PANEL
        # ==================================================

        st.markdown("### 📊 Analysis Summary")

        col1, col2, col3 = st.columns(3)

        score = summary.get("resume_score", 0)

        col1.metric("Resume Score", f"{score}%")
        col2.metric("Readiness", summary.get("readiness", "Unknown"))
        col3.metric("Interview Probability", summary.get("interview_probability", "Unknown"))

        if score < 40:
            st.warning("Your resume needs improvement for this role.")
        elif score < 70:
            st.info("Your resume is partially aligned with this role.")
        else:
            st.success("Your resume is well aligned with this role.")

        st.markdown("---")


        # ==================================================
        # SKILL RADAR
        # ==================================================

        categories = summary.get("skill_categories", {})

        if categories:

            st.subheader("🧠 Skill Intelligence")

            df = pd.DataFrame({
                "Category": list(categories.keys()),
                "Score": list(categories.values())
            })

            fig = px.line_polar(
                df,
                r="Score",
                theta="Category",
                line_close=True
            )

            fig.update_traces(fill="toself")

            fig.update_layout(
                template="plotly_dark",
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)

            st.markdown("---")


        # ==================================================
        # RESUME METRICS
        # ==================================================

        metrics = analysis.get("analysis_metrics", {})

        if metrics:

            st.subheader("📈 Resume Metrics")

            m1, m2, m3 = st.columns(3)

            m1.metric("Resume Length", f"{metrics.get('resume_length_words',0)} words")
            m2.metric("Skills Detected", metrics.get("skills_detected",0))
            m3.metric("Skill Density", f"{metrics.get('skill_density_percent',0)}%")

            st.markdown("---")


        # ==================================================
        # DETECTED SKILLS
        # ==================================================

        st.subheader("🧠 Detected Skills")

        skills = analysis.get("skills", {}).get("skills", [])

        if skills:

            cols = st.columns(4)

            for i, skill in enumerate(skills):

                cols[i % 4].markdown(
                    f"""
                    <div style="
                        padding:8px 12px;
                        border-radius:999px;
                        border:1px solid #334155;
                        font-size:13px;
                        background:#020617;
                        text-align:center;
                        margin-bottom:8px;
                    ">
                    {skill}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

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
                st.info(role.replace("_", " ").title())

        else:
            st.info("No alternative roles detected.")


        # ==================================================
        # DOWNLOAD RESULTS
        # ==================================================

        st.markdown("---")

        st.download_button(
            "Download Analysis",
            data=json.dumps(summary, indent=2),
            file_name="resume_analysis.json",
            mime="application/json"
        )

        st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

        if st.button("Analyze Another Resume", use_container_width=True):
            st.rerun()