

import streamlit as st
from components.styles import load_styles
from ui.career_test import show_career_test
from ui.explorer import show_explorer
from ui.insights import show_insights
from ui.results import show_results

st.set_page_config(page_title="Kareer", layout="wide")
load_styles()

# -----------------------------
# STATE
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

def go(page_name: str):
    st.session_state.page = page_name

# -----------------------------
# EXTRA PAGE STYLES
# -----------------------------
st.markdown("""
<style>
.topbar-wrap{
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(2, 6, 23, 0.88);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(59, 130, 246, 0.12);
    border-radius: 18px;
    padding: 14px 18px;
    margin-bottom: 28px;
}

.brand-title{
    font-size: 30px;
    font-weight: 800;
    color: #f8fafc;
    letter-spacing: -0.5px;
}

.hero-title{
    font-size: 52px;
    font-weight: 800;
    line-height: 1.05;
    color: #f8fafc;
    margin-top: 20px;
    margin-bottom: 14px;
}

.hero-subtitle{
    font-size: 18px;
    line-height: 1.7;
    color: #cbd5e1;
    max-width: 760px;
    margin-bottom: 28px;
}

.feature-box{
    background: linear-gradient(180deg, #111827 0%, #0f172a 100%);
    border: 1px solid #334155;
    border-radius: 22px;
    padding: 28px 24px;
    min-height: 220px;
    transition: all 0.28s ease;
    box-shadow: 0 8px 30px rgba(0,0,0,0.18);
}

.feature-box:hover{
    transform: translateY(-8px) scale(1.01);
    border-color: #3b82f6;
    box-shadow: 0 20px 40px rgba(0,0,0,0.35);
}

.feature-icon{
    font-size: 34px;
    margin-bottom: 10px;
}

.feature-title{
    font-size: 24px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 10px;
}

.feature-desc{
    font-size: 15px;
    line-height: 1.7;
    color: #cbd5e1;
    margin-bottom: 16px;
}

.mini-tag{
    display: inline-block;
    font-size: 12px;
    font-weight: 600;
    color: #93c5fd;
    background: rgba(59,130,246,0.12);
    border: 1px solid rgba(59,130,246,0.20);
    border-radius: 999px;
    padding: 6px 10px;
    margin-right: 8px;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TOP BAR
# -----------------------------
nav1, nav2, nav3, nav4 = st.columns([5, 1, 1, 1])

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

# -----------------------------
# PAGE ROUTING
# -----------------------------
page = st.session_state.page

if page == "home":
    st.markdown('<div class="hero-title">Discover the career path that actually fits you.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">'
        'Kareer helps students explore the right future using structured questions, career pathways, '
        'smart matching, and practical guidance. Start with the path finder or explore careers manually.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2, gap="large")
    c3, c4 = st.columns(2, gap="large")

    with c1:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Career Path Finder</div>
            <div class="feature-desc">
                Answer targeted questions and get your best career match, strong alternatives,
                and roadmap-based direction instead of vague suggestions.
            </div>
            <span class="mini-tag">Best Match</span>
            <span class="mini-tag">Alternatives</span>
            <span class="mini-tag">Roadmaps</span>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Career Path Finder", key="open_pathfinder", use_container_width=True):
            go("career_test")

    with c2:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📚</div>
            <div class="feature-title">Career Explorer</div>
            <div class="feature-desc">
                Browse careers directly and study what they require, how long they take,
                and where they can lead you.
            </div>
            <span class="mini-tag">Explore</span>
            <span class="mini-tag">Search</span>
            <span class="mini-tag">Compare</span>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Career Explorer", key="open_explorer", use_container_width=True):
            go("explorer")

    with c3:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Job Demand Insights</div>
            <div class="feature-desc">
                Understand which careers are in demand, what they pay, and how opportunities vary
                by role and city over time.
            </div>
            <span class="mini-tag">Demand</span>
            <span class="mini-tag">Salary</span>
            <span class="mini-tag">Cities</span>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Job Insights", key="open_insights", use_container_width=True):
            go("insights")

    with c4:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Skill Gap Analyzer</div>
            <div class="feature-desc">
                Find out what skills you are missing for your target career and what you should focus on next.
                This module is reserved for future updates.
            </div>
            <span class="mini-tag">Coming Soon</span>
            <span class="mini-tag">Skill Plan</span>
        </div>
        """, unsafe_allow_html=True)
        st.button("Coming Soon", key="coming_skill_gap", use_container_width=True, disabled=True)

elif page == "career_test":
    show_career_test()

elif page == "results":
    show_results()

elif page == "explorer":
    show_explorer()

elif page == "insights":
    show_insights()