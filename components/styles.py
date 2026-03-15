import streamlit as st


def load_styles():

    st.markdown("""
    <style>

    /* =========================================
       GLOBAL PAGE
    ========================================= */

    html, body, [class*="css"] {
        font-family: Inter, system-ui, -apple-system, sans-serif;
        background: radial-gradient(circle at top, #0b1220, #020617);
        color:#f8fafc;
    }

    .block-container{
        padding-top:2rem;
        padding-bottom:3rem;
        max-width:1200px;
    }


    /* =========================================
       NAVBAR
    ========================================= */

    .brand-title{
        font-size:28px;
        font-weight:800;
        letter-spacing:-0.5px;
        color:#f8fafc;
    }

    .nav-spacing{
        height:12px;
    }


    /* =========================================
       HERO SECTION
    ========================================= */

    .hero-badge{
        display:inline-block;
        font-size:12px;
        font-weight:600;
        padding:6px 12px;
        border-radius:999px;
        background:rgba(59,130,246,.15);
        border:1px solid rgba(59,130,246,.35);
        color:#93c5fd;
        margin-bottom:10px;
    }

    .hero-title{
        font-size:56px;
        font-weight:800;
        line-height:1.05;
        color:#f8fafc;
        margin-top:10px;
        margin-bottom:10px;
        letter-spacing:-1px;
    }

    .hero-subtitle{
        font-size:18px;
        line-height:1.7;
        color:#94a3b8;
        max-width:720px;
        margin-bottom:30px;
    }


    /* =========================================
       BUTTONS
    ========================================= */

    .stButton>button{
        border-radius:12px;
        height:46px;
        font-weight:600;
        border:1px solid rgba(59,130,246,.35);
        background:linear-gradient(180deg,#3b82f6,#2563eb);
        color:white;
        transition:all .2s ease;
    }

    .stButton>button:hover{
        transform:translateY(-2px);
        box-shadow:0 10px 24px rgba(0,0,0,.45);
        border-color:#60a5fa;
    }


    /* =========================================
       AI HERO BOX
    ========================================= */

    .ai-box{
        border:1px solid rgba(59,130,246,.25);
        border-radius:22px;
        padding:40px;
        background:linear-gradient(180deg,#0f172a,#020617);
        text-align:center;
        margin-top:10px;
        margin-bottom:30px;
        box-shadow:0 25px 50px rgba(0,0,0,.45);
    }

    .ai-box h3{
        font-size:26px;
        font-weight:700;
        margin-bottom:10px;
    }


    /* =========================================
       FEATURE CARDS
    ========================================= */

    .feature-box{
        background:linear-gradient(180deg,#0f172a,#020617);
        border:1px solid #1e293b;
        border-radius:20px;
        padding:26px;
        min-height:170px;
        transition:all .25s ease;
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


    /* =========================================
       TAGS
    ========================================= */

    .mini-tag{
        display:inline-block;
        font-size:11px;
        font-weight:600;
        color:#93c5fd;
        background:rgba(59,130,246,.12);
        border:1px solid rgba(59,130,246,.25);
        border-radius:999px;
        padding:4px 8px;
        margin-right:6px;
        margin-top:8px;
    }


    /* =========================================
       TICKER
    ========================================= */

    .ticker-container{
        margin-top:10px;
        margin-bottom:25px;
        border:1px solid rgba(59,130,246,.35);
        border-radius:12px;
        overflow:hidden;
        background:linear-gradient(180deg,#0f172a,#020617);
        box-shadow:0 8px 20px rgba(0,0,0,.3);
    }

    .ticker-wrap{
        width:100%;
        overflow:hidden;
        white-space:nowrap;
    }

    .ticker-move{
        display:inline-block;
        padding-left:100%;
        animation:tickerScroll 45s linear infinite;
        font-size:14px;
        color:#93c5fd;
    }

    .ticker-item{
        margin-right:70px;
        font-weight:600;
    }

    .ticker-container:hover .ticker-move{
        animation-play-state:paused;
    }

    @keyframes tickerScroll{
        0% {transform:translateX(0);}
        100% {transform:translateX(-100%);}
    }


    /* =========================================
       SPACING HELPERS
    ========================================= */

    .section-space{
        height:30px;
    }

    .section-divider{
        margin-top:12px;
        margin-bottom:24px;
        border-bottom:1px solid #1e293b;
    }


    /* =========================================
       MOBILE OPTIMIZATION
    ========================================= */

    @media (max-width: 768px){

        .hero-title{
            font-size:36px;
        }

        .hero-subtitle{
            font-size:16px;
        }

        .feature-box{
            min-height:150px;
        }

        .ai-box{
            padding:30px;
        }

    }

    </style>
    """, unsafe_allow_html=True)