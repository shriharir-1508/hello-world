import streamlit as st

# Title and Header
st.title("Welcome to Streamlit!")
st.header("Interactive Demo for Students")

# Text Input
name = st.text_input("Enter your name:", "")

# Selectbox
favorite_subject = st.selectbox("What's your favorite subject?", ["Math", "Science", "History", "Art", "Computer Science"])

# Slider
excitement_level = st.slider("How excited are you to learn Streamlit?", 0, 10, 5)
