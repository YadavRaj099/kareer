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

st.set_page_config(page_title="Kareer", layout="wide")
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
# 4️⃣ GLOBAL UI STYLES
# =====================================================

st.markdown("""
<style>

/* PAGE WIDTH */
.block-container{
    padding-top:2rem;
    padding-bottom:3rem;
}

/* BRAND */
.brand-title{
    font-size:30px;
    font-weight:800;
    color:#f8fafc;
}

/* HERO */

.hero-title{
    font-size:56px;
    font-weight:800;
    line-height:1.1;
    color:#f8fafc;
    margin-top:30px;
}

.hero-subtitle{
    font-size:18px;
    line-height:1.7;
    color:#94a3b8;
    max-width:750px;
    margin-bottom:30px;
}

/* FEATURE CARDS */

.feature-box{
    background:linear-gradient(180deg,#111827,#020617);
    border:1px solid #1e293b;
    border-radius:18px;
    padding:24px;
    transition:all .25s ease;
    height:180px;
}

.feature-box:hover{
    transform:translateY(-6px);
    border-color:#3b82f6;
    box-shadow:0 20px 40px rgba(0,0,0,.35);
}

.feature-icon{
    font-size:28px;
    margin-bottom:6px;
}

.feature-title{
    font-size:20px;
    font-weight:700;
    color:#f8fafc;
}

.feature-desc{
    font-size:14px;
    color:#94a3b8;
    margin-top:6px;
}

/* MINI TAG */

.mini-tag{
    display:inline-block;
    font-size:11px;
    font-weight:600;
    color:#93c5fd;
    background:rgba(59,130,246,.12);
    border:1px solid rgba(59,130,246,.25);
    border-radius:999px;
    padding:4px 8px;
    margin-right:5px;
    margin-top:6px;
}

/* AI HERO BOX */

.ai-box{
    border:1px solid #1e293b;
    border-radius:20px;
    padding:40px;
    background:linear-gradient(180deg,#0f172a,#020617);
    text-align:center;
}

/* NAVBAR BUTTONS */

.stButton>button{
    border-radius:10px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# 5️⃣ NAVBAR
# =====================================================

nav1, nav2, nav3, nav4, nav5 = st.columns([5,1,1,1,1])

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

st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)


# =====================================================
# 6️⃣ TREND TICKER
# =====================================================

trends = get_trends()

ticker_html = '<div class="ticker-container"><div class="ticker-wrap"><div class="ticker-move">'

for t in trends:
    ticker_html += f'<span class="ticker-item">🔥 {t}</span>'

ticker_html += '</div></div></div>'

st.markdown(ticker_html, unsafe_allow_html=True)

st.markdown("---")


# =====================================================
# 7️⃣ PAGE ROUTER
# =====================================================

page = st.session_state.page


# =====================================================
# 8️⃣ HOME PAGE
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

    st.markdown("<br>", unsafe_allow_html=True)

    # AI HERO FEATURE

    st.markdown("""
    <div class="ai-box">
    <h3>AI Resume Skill Analyzer</h3>
    Upload your resume and instantly discover:

    • Career readiness score  
    • Skills you are missing  
    • Interview probability  
    • Personalized roadmap
    </div>
    """, unsafe_allow_html=True)

    st.button("Upload Resume (Coming Soon)", disabled=True, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

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
# OTHER PAGES
# =====================================================

elif page == "career_test":
    show_career_test()

elif page == "results":
    show_results()

elif page == "explorer":
    show_explorer()

elif page == "insights":
    show_insights()