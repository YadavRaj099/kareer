# =====================================================
# 1️⃣ IMPORTS
# =====================================================

import streamlit as st

from components.styles import load_styles

from ui.career_test import show_career_test
from ui.explorer import show_explorer
from ui.insights import show_insights
from ui.results import show_results
from ui.resume_analyzer import show_resume_analyzer

from engine.trends import get_trends


# =====================================================
# 2️⃣ PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Kareer",
    layout="wide",
    page_icon="🧭"
)

load_styles()


# =====================================================
# 3️⃣ SESSION STATE
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


def go(page_name: str):
    st.session_state.page = page_name
    st.rerun()


# =====================================================
# 4️⃣ NAVBAR
# =====================================================

nav_brand, nav_home, nav_resume, nav_finder, nav_explorer, nav_insights = st.columns(
    [5, 1.2, 1.5, 1.4, 1.4, 1.4]
)

with nav_brand:
    st.markdown(
        """
        <div style="
            font-size:32px;
            font-weight:800;
            letter-spacing:-0.5px;
        ">
        Kareer
        </div>
        """,
        unsafe_allow_html=True
    )

with nav_home:
    if st.button("Home", use_container_width=True):
        go("home")

with nav_resume:
    if st.button("Resume AI", use_container_width=True):
        go("resume_analyzer")

with nav_finder:
    if st.button("Path Finder", use_container_width=True):
        go("career_test")

with nav_explorer:
    if st.button("Explorer", use_container_width=True):
        go("explorer")

with nav_insights:
    if st.button("Insights", use_container_width=True):
        go("insights")

st.markdown("<div class='nav-spacing'></div>", unsafe_allow_html=True)


# =====================================================
# 5️⃣ TREND TICKER
# =====================================================

trends = get_trends()

ticker_html = """
<div class="ticker-container">
<div class="ticker-wrap">
<div class="ticker-move">
"""

for trend in trends:
    ticker_html += f'<span class="ticker-item">{trend}</span>'

ticker_html += """
</div>
</div>
</div>
"""

st.markdown(ticker_html, unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# =====================================================
# 6️⃣ ROUTER
# =====================================================

page = st.session_state.page


# =====================================================
# 7️⃣ HOME PAGE
# =====================================================

if page == "home":

    # HERO
    st.markdown(
        '<div class="hero-title">AI Career Intelligence for Students</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'Analyze your resume, discover missing skills, and find the career path that fits you.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    # =================================================
    # MAIN PRODUCT
    # =================================================

    st.markdown(
        """
        <div class="ai-box">

        <h3>AI Resume Skill Analyzer</h3>

        <p>Upload your resume and instantly discover:</p>

        <ul style="list-style:none;padding:0;margin-top:10px;color:#94a3b8">
        <li>Career readiness score</li>
        <li>Skills you are missing</li>
        <li>Interview probability</li>
        <li>Personalized learning roadmap</li>
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Analyze My Resume", use_container_width=True):
        go("resume_analyzer")

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    # =================================================
    # SECONDARY FEATURE
    # =================================================

    st.markdown(
        '<div class="section-title">Discover Your Ideal Career</div>',
        unsafe_allow_html=True
    )

    if st.button("Take Career Path Test", use_container_width=True):
        go("career_test")

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    # =================================================
    # FEATURE CARDS
    # =================================================

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="feature-box">
                <div class="feature-icon">🎯</div>
                <div class="feature-title">Career Path Finder</div>
                <div class="feature-desc">
                    Discover careers that match your personality and skills.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Open Career Path Finder", use_container_width=True):
            go("career_test")

    with col2:

        st.markdown(
            """
            <div class="feature-box">
                <div class="feature-icon">📚</div>
                <div class="feature-title">Career Explorer</div>
                <div class="feature-desc">
                    Explore career requirements, skills and growth paths.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Open Career Explorer", use_container_width=True):
            go("explorer")

    with col3:

        st.markdown(
            """
            <div class="feature-box">
                <div class="feature-icon">📊</div>
                <div class="feature-title">Job Demand Insights</div>
                <div class="feature-desc">
                    Discover which careers are growing and their salary trends.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Open Job Insights", use_container_width=True):
            go("insights")

    with col4:

        st.markdown(
            """
            <div class="feature-box">
                <div class="feature-icon">🧠</div>
                <div class="feature-title">Skill Gap Analyzer</div>
                <div class="feature-desc">
                    Identify missing skills for your dream job.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Open Resume Analyzer", use_container_width=True):
            go("resume_analyzer")


# =====================================================
# 8️⃣ OTHER PAGES
# =====================================================

elif page == "career_test":
    show_career_test()

elif page == "results":
    show_results()

elif page == "explorer":
    show_explorer()

elif page == "insights":
    show_insights()

elif page == "resume_analyzer":
    show_resume_analyzer()