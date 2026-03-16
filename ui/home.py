import streamlit as st


def show_home(go):

    st.markdown("""
    <style>

    /* =========================
       HERO
    ========================= */

    .hero-title{
        font-size:52px;
        font-weight:800;
        line-height:1.1;
        margin-top:40px;
        text-align:center;
        letter-spacing:-0.5px;
    }

    .hero-sub{
        font-size:18px;
        color:#94a3b8;
        margin-top:14px;
        margin-bottom:40px;
        text-align:center;
        max-width:720px;
        margin-left:auto;
        margin-right:auto;
    }


    /* =========================
       SECTION TITLES
    ========================= */

    .section-title{
        font-size:28px;
        font-weight:700;
        margin-top:60px;
        margin-bottom:26px;
        text-align:center;
    }


    /* =========================
       GLASS CARD
    ========================= */

    .glass-card{
        border-radius:18px;
        padding:28px;

        background: rgba(30,41,59,0.45);
        backdrop-filter: blur(12px);

        border:1px solid rgba(148,163,184,0.15);

        transition:0.25s;
        height:100%;
    }

    .glass-card:hover{
        transform: translateY(-6px);
        border:1px solid rgba(20,184,166,0.6);
    }


    /* =========================
       FEATURE CARD CONTENT
    ========================= */

    .feature-icon{
        font-size:26px;
        margin-bottom:10px;
    }

    .feature-title{
        font-size:20px;
        font-weight:600;
        margin-bottom:8px;
    }

    .feature-desc{
        font-size:14px;
        color:#94a3b8;
        margin-bottom:16px;
    }


    /* =========================
       AI BOX
    ========================= */

    .ai-box{
        border-radius:22px;
        padding:36px;

        background: rgba(30,41,59,0.45);
        backdrop-filter: blur(12px);

        border:1px solid rgba(148,163,184,0.15);

        text-align:center;
        max-width:720px;
        margin:auto;
    }

    .ai-box ul{
        list-style:none;
        padding:0;
        margin-top:18px;
        color:#94a3b8;
        font-size:15px;
    }

    .ai-box li{
        margin-bottom:8px;
    }

    </style>
    """, unsafe_allow_html=True)

    # =================================================
    # HERO SECTION
    # =================================================

    st.markdown(
        '<div class="hero-title">Discover the career path that actually fits you.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-sub">AI-powered career intelligence that helps students discover the right career path, required skills, and learning roadmap.</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns([1,2,1])

    with c2:
        if st.button("Start Career Test", use_container_width=True):
            go("career_test")


    # =================================================
    # AI RESUME ANALYZER
    # =================================================

    st.markdown(
        '<div class="section-title">AI Resume Skill Analyzer</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="ai-box">

    Upload your resume and instantly discover:

    <ul>
    <li>Career readiness score</li>
    <li>Missing skills for your target role</li>
    <li>Interview probability</li>
    <li>Personalized learning roadmap</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1,2,1])

    with c2:
        if st.button("Analyze Resume", use_container_width=True):
            go("resume_analyzer")


    # =================================================
    # FEATURES
    # =================================================

    st.markdown(
        '<div class="section-title">Explore Kareer Tools</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="glass-card">

        <div class="feature-icon">🎯</div>

        <div class="feature-title">
        Career Path Finder
        </div>

        <div class="feature-desc">
        Answer targeted questions and discover the careers that match your skills, interests, and personality.
        </div>

        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Career Path Finder", use_container_width=True):
            go("career_test")


    with col2:

        st.markdown("""
        <div class="glass-card">

        <div class="feature-icon">📚</div>

        <div class="feature-title">
        Career Explorer
        </div>

        <div class="feature-desc">
        Explore careers and understand what skills, education, and experience they require.
        </div>

        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Career Explorer", use_container_width=True):
            go("explorer")


    col3, col4 = st.columns(2)

    with col3:

        st.markdown("""
        <div class="glass-card">

        <div class="feature-icon">📊</div>

        <div class="feature-title">
        Job Demand Insights
        </div>

        <div class="feature-desc">
        Discover which careers are growing and what salary ranges they offer.
        </div>

        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Job Insights", use_container_width=True):
            go("insights")


    with col4:

        st.markdown("""
        <div class="glass-card">

        <div class="feature-icon">🧠</div>

        <div class="feature-title">
        Skill Gap Analyzer
        </div>

        <div class="feature-desc">
        Analyze your resume and discover the skills required for your dream job.
        </div>

        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Resume Analyzer", use_container_width=True):
            go("resume_analyzer")