import streamlit as st
st.config.show_svg = True

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("Profile_photo.png", width=230)

with col2:
    st.title("Saran B", anchor=False)
    st.write(
        "An Artificial Intelligence Enthusiasist and a passionate Machine Learning Engineer.\n\n"
    )
st.markdown("<hr>", unsafe_allow_html=True)

# Set the width of the images
width = '24'

# Set the file names for the SVG files
linkedin_file = 'linkedin.svg'
instagram_file = 'instagram.svg'
google_cloud_file = 'google_cloud.svg'
mail_file = 'gmail.svg'
whatsapp_file = 'whatsapp.svg'
twitter_file = 'x.svg'

# Set your social media handles
your_linkedin_handle = 'https://www.linkedin.com/in/saranfto/'
your_instagram_handle = 'https://www.instagram.com/saran_fto/'
your_google_cloud_handle = 'https://www.cloudskillsboost.google/public_profiles/47173567-3175-4d63-8b40-42de9e71c1d2'
your_mail_handle = 'mailto:saran290901@gmail.com'
your_whatsapp_handle = 'https://wa.me/message/ZAN73OXLJFWPE1'
your_twitter_handle = 'https://x.com/saran_fto'

# Create a single row with all the social media links
row = st.columns([1, 1, 1, 1, 1, 1])

# Add the social media links to the row
with row[0]:
    st.markdown(f"<a href='https://www.linkedin.com/in/saranfto/'><img src='linkedin.svg' width='{width}'></a>", unsafe_allow_html=True)

with row[1]:
    st.markdown(f"<a href='https://www.instagram.com/saran_fto/'><img src='instagram.svg' width='{width}'></a>", unsafe_allow_html=True)

with row[2]:
    st.markdown(f"<a href='https://www.cloudskillsboost.google/public_profiles/47173567-3175-4d63-8b40-42de9e71c1d2'><img src='google_cloud.svg' width='{width}'></a>", unsafe_allow_html=True)

with row[3]:
    st.markdown(f"<a href='mailto:saran290901@gmail.com'><img src='gmail.svg' width='{width}'></a>", unsafe_allow_html=True)

with row[4]:
    st.markdown(f"<a href='https://wa.me/message/ZAN73OXLJFWPE1'><img src='whatsapp.svg' width='{width}'></a>", unsafe_allow_html=True)

with row[5]:
    st.markdown(f"<a href='https://x.com/saran_fto/'><img src='x.svg' width='{width}'></a>", unsafe_allow_html=True)