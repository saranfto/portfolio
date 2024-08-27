import streamlit as st

# Create a button to show the under development message
if st.button("Diabetes Prediction"):
    st.write("<div style='padding: 20px; background-color: #f8d7da; color: #FF0000; border: 1px solid #f5c6cb; border-radius: 5px;'>This Model is currently under development. Saran will make this available soon, Kindly check Later!</div>", unsafe_allow_html=True)

