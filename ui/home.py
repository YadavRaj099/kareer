import streamlit as st


def show_home(go):

    st.markdown("""
    <style>

    .hero-title {
        font-size:48px;
        font-weight:800;
        line-height:1.1;
        margin-top:30px;
    }

    .hero-sub {
        font-size:18px;
        color:#94a3b8;
        margin-top:10px;
        margin-bottom:30px;
    }

    .section-title{
        font-size:28px;
        font-weight:700;
        margin-top:40px;
        margin-bottom:20px;
    }

    .feature-card{
        border:1px solid #1e293b;
        border-radius:16px;
        padding:24px;
        background:linear-gradient(180deg,#0f172a,#020617);
        transition:0.25s;
    }

    .feature-card:hover{
        transform:translateY(-6px);
        border:1px solid #3b82f6;
    }

    .feature-title{
        font-size:20px;
        font-weight:600;
        margin-top:8px;
    }

    .feature-desc{
        font-size:14px;
        color:#94a3b8;
        margin-top:6px;
        margin-bottom:16px;
    }

    .ai-box{
        border:1px solid #1e293b;
        border-radius:18px;
        padding:40px;
        background:linear-gradient(180deg,#0f172a,#020617);
        margin-top:30px;
        text-align:center;
    }

    </style>
    """, unsafe_allow_html=True)

    # HERO SECTION
    st.markdown('<div class="hero-title">Discover the career path that actually fits you.</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="hero-sub">AI-powered career intelligence to help students and professionals choose the right path.</div>',
        unsafe_allow_html=True
    )

    if st.button("🚀 Start Career Test", use_container_width=True):
        go("career_test")

    st.markdown("---")

    # AI HERO FEATURE
    st.markdown('<div class="section-title">AI Resume Skill Analyzer</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="ai-box">
    Upload your resume and instantly discover:

    • Career readiness score  
    • Skills you are missing  
    • Interview probability  
    • Personalized learning roadmap
    </div>
    """, unsafe_allow_html=True)

    st.button("Upload Resume (Coming Soon)", disabled=True, use_container_width=True)

    st.markdown("---")

    # FEATURE CARDS
    st.markdown('<div class="section-title">Explore Kareer Tools</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
        🎯
        <div class="feature-title">Career Path Finder</div>
        <div class="feature-desc">
        Answer targeted questions and discover the careers that match your skills, interests, and personality.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Career Path Finder", use_container_width=True):
            go("career_test")

    with col2:
        st.markdown("""
        <div class="feature-card">
        📚
        <div class="feature-title">Career Explorer</div>
        <div class="feature-desc">
        Explore hundreds of careers and understand what skills, education, and experience they require.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Career Explorer", use_container_width=True):
            go("explorer")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="feature-card">
        📊
        <div class="feature-title">Job Demand Insights</div>
        <div class="feature-desc">
        Discover which careers are growing fast and what salary ranges they offer.
        </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Job Insights", use_container_width=True):
            go("insights")

    with col4:
        st.markdown("""
        <div class="feature-card">
        🧠
        <div class="feature-title">Skill Gap Analyzer</div>
        <div class="feature-desc">
        Analyze your resume and see what skills you need to land your dream job.
        </div>
        </div>
        """, unsafe_allow_html=True)

        st.button("Coming Soon", disabled=True, use_container_width=True)