import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/diabetes_modal.py",
    title="Diabetes Prediction Modal",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/socialmedia_modal.py",
    title="Diabetes Prediction Modal",
    icon=":material/bar_chart:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---


pg = st.navigation(
    {    
        "Info": [about_page],
        "Projects": [project_1_page,project_2_page],
    }
)


st.sidebar.markdown("Site Under Development")

# --- RUN NAVIGATION ---
pg.run()
