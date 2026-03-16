import streamlit as st


def load_styles():

    st.markdown("""
    <style>


    /* =========================================
       GLOBAL PAGE
    ========================================= */

    html, body, [class*="css"] {
        font-family: Inter, system-ui, -apple-system, sans-serif;
        background: radial-gradient(circle at top, #0f172a, #020617);
        color:#e2e8f0;
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

        background:rgba(20,184,166,.15);
        border:1px solid rgba(20,184,166,.35);
        color:#5eead4;

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
       BUTTONS (TRUST CALM TEAL)
    ========================================= */

    .stButton>button{
        border-radius:12px;
        height:46px;
        font-weight:600;

        background:#14b8a6;
        border:none;
        color:white;

        transition:all .2s ease;
    }

    .stButton>button:hover{
        background:#0d9488;
        transform:translateY(-2px);
        box-shadow:0 10px 25px rgba(0,0,0,.4);
    }



    /* =========================================
       GLASS AI BOX
    ========================================= */

    .ai-box{

        border-radius:22px;
        padding:40px;

        background: rgba(30,41,59,0.45);
        backdrop-filter: blur(14px);

        border:1px solid rgba(148,163,184,0.15);

        text-align:center;

        margin-top:10px;
        margin-bottom:30px;

        box-shadow:0 20px 40px rgba(0,0,0,.35);
    }

    .ai-box h3{
        font-size:26px;
        font-weight:700;
        margin-bottom:10px;
    }



    /* =========================================
       FEATURE CARDS (GLASS)
    ========================================= */

    .feature-box{

        background: rgba(30,41,59,0.45);
        backdrop-filter: blur(14px);

        border:1px solid rgba(148,163,184,0.15);

        border-radius:20px;
        padding:26px;

        min-height:170px;

        transition:all .25s ease;
    }

    .feature-box:hover{
        transform:translateY(-6px);
        border-color:rgba(20,184,166,0.6);
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

        color:#5eead4;
        background:rgba(20,184,166,.12);

        border:1px solid rgba(20,184,166,.25);

        border-radius:999px;
        padding:4px 8px;

        margin-right:6px;
        margin-top:8px;
    }



    /* =========================================
       TREND TICKER
    ========================================= */

    .ticker-container{
        margin-top:10px;
        margin-bottom:25px;

        border-radius:14px;

        background: rgba(30,41,59,0.45);
        backdrop-filter: blur(14px);

        border:1px solid rgba(148,163,184,0.15);

        overflow:hidden;
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
        color:#5eead4;
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
        border-bottom:1px solid rgba(148,163,184,0.15);
    }



    /* =========================================
       MOBILE OPTIMIZATION
    ========================================= */

    @media (max-width:768px){

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