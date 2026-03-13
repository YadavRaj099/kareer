import streamlit as st

from components.styles import load_styles

from ui.home import show_home
from ui.career_test import show_career_test
from ui.results import show_results
from ui.explorer import show_explorer
from ui.insights import show_insights


st.set_page_config(
    page_title="Kareer",
    layout="wide"
)

load_styles()

# Navigation state
if "page" not in st.session_state:
    st.session_state.page = "home"

page = st.session_state.page


if page == "home":
    show_home()

elif page == "career_test":
    show_career_test()

elif page == "results":
    show_results()

elif page == "explorer":
    show_explorer()

elif page == "insights":
    show_insights()