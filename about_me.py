import streamlit as st


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("Profile_photo.png", width=230)

with col2:
    st.title("Saran B", anchor=False)
    st.write(
        "An Artificial Intelligence Enthusiasist and a passionate Machine Learning Engineer."
    )
    


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience", anchor=False)
st.write(
    """
    
Operations Manager, Wasl International Exim\n
March 2024 – Present\n
Managing operations at Wasl International Exim, I oversee supply chain logistics, optimize processes, and lead cross-functional teams. My focus is on improving efficiency, negotiating with suppliers, and ensuring compliance with international trade regulations, all to drive company success in a competitive market.

    """
)

st.write("\n")
st.subheader("Qualifications", anchor=False)
st.write(
    """

    
Bachelor’s Degree in Computer Science (In Progress)\n
Government Arts Collage , Karur \n
Currently pursuing a degree in Computer Science, where I’m building expertise in Artificial Intelligence and Machine Learning. This technical knowledge complements my operational experience, helping me integrate business strategies with digital solutions.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Python: Machine learning model development
    - Scikit-learn: Traditional ML algorithms
    - Pandas & NumPy: Data manipulation and analysis
    - SQL: Database querying
    - Mathematics: Linear algebra, probability, optimization
    - Model Deployment: Flask, Docker, cloud platforms
    - Algorithms: Strong foundation in AI and data structures
    - Git : Version Control platform
    """
)

st.write("\n")
st.subheader("Personal Projects", anchor=False)
st.write(
    """
    - A Machine Learning Modal to Predict Diabetics Affection
    - A Machine Learning Modal to Predict Social Media Account Visibility
    """
)

st.write("\n")
st.subheader("Languages", anchor=False)
st.write(
    """
    - Corporate English - Moderate Professional Proficiency
    - Tamil - Native Proficiency
    - Japanese - Elementary level Proficiency
    """
)

