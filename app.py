# =====================================================
# 1️⃣ IMPORTS
# =====================================================

import streamlit as st

from components.styles import load_styles

from ui.career_test import show_career_test
from ui.explorer import show_explorer
from ui.insights import show_insights
from ui.results import show_results

from engine.trends import get_trends


# =====================================================
# 2️⃣ PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Kareer",
    layout="wide"
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

nav1, nav2, nav3, nav4, nav5 = st.columns([4,1.2,1.2,1.2,1.2])

with nav1:
    st.markdown('<div class="brand-title">Kareer</div>', unsafe_allow_html=True)

with nav2:
    if st.button("Home", use_container_width=True):
        go("home")

with nav3:
    if st.button("Path Finder", use_container_width=True):
        go("career_test")

with nav4:
    if st.button("Insights", use_container_width=True):
        go("insights")

with nav5:
    if st.button("Explorer", use_container_width=True):
        go("explorer")


st.markdown("<div class='nav-spacing'></div>", unsafe_allow_html=True)


# =====================================================
# 5️⃣ TREND TICKER
# =====================================================

trends = get_trends()

ticker_html = '<div class="ticker-container"><div class="ticker-wrap"><div class="ticker-move">'

for t in trends:
    ticker_html += f'<span class="ticker-item">🔥 {t}</span>'

ticker_html += '</div></div></div>'

st.markdown(ticker_html, unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# =====================================================
# 6️⃣ PAGE ROUTER
# =====================================================

page = st.session_state.page


# =====================================================
# 7️⃣ HOME PAGE
# =====================================================

if page == "home":

    st.markdown(
        '<div class="hero-title">Discover the career path that actually fits you.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'AI-powered career intelligence that helps students discover the right career path, skills, and roadmap.'
        '</div>',
        unsafe_allow_html=True
    )

    if st.button("🚀 Start Career Test", use_container_width=True):
        go("career_test")

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    # AI FEATURE BOX

    st.markdown("""
    <div class="ai-box">
        <h3>AI Resume Skill Analyzer</h3>
        <p>
        Upload your resume and instantly discover:
        </p>

        <p>
        • Career readiness score<br>
        • Skills you are missing<br>
        • Interview probability<br>
        • Personalized roadmap
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.button("Upload Resume (Coming Soon)", disabled=True, use_container_width=True)

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    # FEATURE CARDS

    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    with c1:

        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Career Path Finder</div>
            <div class="feature-desc">
                Answer targeted questions and get your best career match.
            </div>
            <span class="mini-tag">Best Match</span>
            <span class="mini-tag">Alternatives</span>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Career Path Finder", use_container_width=True):
            go("career_test")

    with c2:

        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📚</div>
            <div class="feature-title">Career Explorer</div>
            <div class="feature-desc">
                Explore careers and what they require.
            </div>
            <span class="mini-tag">Explore</span>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Career Explorer", use_container_width=True):
            go("explorer")

    with c3:

        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Job Demand Insights</div>
            <div class="feature-desc">
                Discover which careers are growing and what they pay.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Job Insights", use_container_width=True):
            go("insights")

    with c4:

        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Skill Gap Analyzer</div>
            <div class="feature-desc">
                Analyze your resume and find missing skills.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.button("Coming Soon", disabled=True, use_container_width=True)


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