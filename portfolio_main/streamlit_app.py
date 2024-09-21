import streamlit as st
#The below code to hide the hamburger icon on the top right side in our web page,,,,,,,,,, header {visibility : hidden ;} is commended because we need header !
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            </style>
            """
            #header {visibility: hidden;}


# --- PAGE SETUP ---
about_page = st.Page(
    "about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

certificates_page = st.Page(
    "cert_lic.py",
    title="Licences and Certifications",
    icon=":material/thumb_up:",
    
    )
contact_page = st.Page(
    "contact.py",
    title="Contact",
    icon=":material/contacts:",
    
    )
project_1_page = st.Page(
    "diabetes_modal.py",
    title="Diabetes Prediction Modal",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "socialmedia_modal.py",
    title="Diabetes Prediction Modal",
    icon=":material/bar_chart:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---


pg = st.navigation(
    {    
        "Info": [about_page,certificates_page,contact_page],
        "Projects": [project_1_page,project_2_page],
    }
)


st.sidebar.markdown("Site Under Development")

# --- RUN NAVIGATION ---
pg.run()
