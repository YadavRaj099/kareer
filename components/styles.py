import streamlit as st

def load_styles():

    st.markdown(
        """
        <style>

        /* Main background */

        .stApp {
            background: linear-gradient(135deg,#0f172a,#020617);
            color: #f8fafc;
        }

        /* Title styling */

        h1, h2, h3 {
            color: #f1f5f9;
            font-weight: 700;
        }

        /* Card styling */

        .feature-card {
            background: #1e293b;
            padding: 30px;
            border-radius: 18px;
            border: 1px solid #334155;
            transition: all 0.25s ease;
            cursor: pointer;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            border: 1px solid #3b82f6;
            box-shadow: 0px 10px 25px rgba(0,0,0,0.4);
        }

        /* Card title */

        .card-title {
            font-size: 22px;
            font-weight: 600;
            margin-bottom: 10px;
        }

        /* Card description */

        .card-desc {
            font-size: 15px;
            color: #cbd5f5;
        }

        /* Buttons */

        .stButton button {
            background-color: #3b82f6;
            border-radius: 10px;
            border: none;
            padding: 10px 18px;
            color: white;
            font-weight: 600;
        }

        .stButton button:hover {
            background-color: #2563eb;
        }

        /* Progress bar */

        .stProgress > div > div > div {
            background-color: #3b82f6;
        }

        </style>
        """,
        unsafe_allow_html=True
    )