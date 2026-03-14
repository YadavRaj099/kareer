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

/* BRAND */

.brand-title{
    font-size:30px;
    font-weight:800;
    color:#f8fafc;
}


/* HERO */

.hero-title{
    font-size:52px;
    font-weight:800;
    line-height:1.05;
    color:#f8fafc;
    margin-top:20px;
}

.hero-subtitle{
    font-size:18px;
    line-height:1.7;
    color:#cbd5e1;
    max-width:760px;
    margin-bottom:30px;
}


/* FEATURE CARDS */

.feature-box{
    background:linear-gradient(180deg,#111827,#0f172a);
    border:1px solid #334155;
    border-radius:22px;
    padding:28px 24px;
    min-height:220px;
    transition:all .25s ease;
}

.feature-box:hover{
    transform:translateY(-8px);
    border-color:#3b82f6;
    box-shadow:0 20px 40px rgba(0,0,0,.35);
}

.feature-icon{
    font-size:34px;
    margin-bottom:10px;
}

.feature-title{
    font-size:24px;
    font-weight:700;
    color:#f8fafc;
}

.feature-desc{
    font-size:15px;
    line-height:1.7;
    color:#cbd5e1;
    margin-bottom:14px;
}

.mini-tag{
    display:inline-block;
    font-size:12px;
    font-weight:600;
    color:#93c5fd;
    background:rgba(59,130,246,.12);
    border:1px solid rgba(59,130,246,.25);
    border-radius:999px;
    padding:6px 10px;
    margin-right:6px;
    margin-top:4px;
}

/* CAREER TEST CONTAINER */

.career-test-card{
    background: linear-gradient(180deg,#0f172a,#020617);
    border:1px solid rgba(59,130,246,0.25);
    border-radius:18px;
    padding:30px;
    margin-top:20px;
    box-shadow:0 10px 30px rgba(0,0,0,0.35);
}

/* QUESTION TITLE */

.question-label{
    font-size:14px;
    font-weight:600;
    color:#cbd5e1;
    margin-bottom:6px;
}

/* FORM SPACING */

.form-section{
    margin-bottom:20px;
}

/* SUBMIT BUTTON */

.stButton > button{
    height:52px;
    font-size:16px;
    font-weight:600;
    border-radius:12px;
}


</style>
""", unsafe_allow_html=True)


# =====================================================
# 5️⃣ TICKER STYLES
# =====================================================

st.markdown("""
<style>

.ticker-container{
    margin-top:12px;
    margin-bottom:30px;
    border:1px solid rgba(59,130,246,.35);
    border-radius:14px;
    overflow:hidden;
    background:linear-gradient(180deg,#0f172a,#020617);
    box-shadow:0 8px 24px rgba(0,0,0,.35), 0 0 10px rgba(59,130,246,.15);
}

.ticker-wrap{
    width:100%;
    overflow:hidden;
    white-space:nowrap;
}

.ticker-move{
    display:inline-block;
    padding-left:100%;
    animation:tickerScroll 55s linear infinite;
    color:#93c5fd;
    font-size:14px;
    font-weight:600;
}

.ticker-container:hover .ticker-move{
    animation-play-state:paused;
}

.ticker-item{
    display:inline-block;
    margin-right:80px;
}

@keyframes tickerScroll{
    0% {transform:translateX(0);}
    100% {transform:translateX(-100%);}
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# 6️⃣ NAVBAR
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


st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)


# =====================================================
# 7️⃣ TREND TICKER
# =====================================================

trends = get_trends()

ticker_html = '<div class="ticker-container"><div class="ticker-wrap"><div class="ticker-move">'

for t in trends:
    ticker_html += f'<span class="ticker-item">🔥 {t}</span>'

ticker_html += '</div></div></div>'

st.markdown(ticker_html, unsafe_allow_html=True)

st.markdown("---")


# =====================================================
# 8️⃣ PAGE ROUTER
# =====================================================

page = st.session_state.page


# =====================================================
# 9️⃣ HOME PAGE
# =====================================================

if page == "home":

    st.markdown(
        '<div class="hero-title">Discover the career path that actually fits you.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'Kareer helps students explore the right future using structured questions, career pathways, '
        'smart matching, and practical guidance.'
        '</div>',
        unsafe_allow_html=True
    )


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
        <span class="mini-tag">Roadmaps</span>
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
        Browse careers and explore what they require.
        </div>
        <span class="mini-tag">Explore</span>
        <span class="mini-tag">Compare</span>
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
        Understand which careers are in demand and what they pay.
        </div>
        <span class="mini-tag">Demand</span>
        <span class="mini-tag">Salary</span>
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
        Find what skills you need for your target career.
        </div>
        <span class="mini-tag">Coming Soon</span>
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