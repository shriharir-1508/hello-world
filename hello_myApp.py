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
# Button
if st.button("Submit"):
    st.write(f"Hello, **{name}**! 🎉 You love **{favorite_subject}**.")
    st.write(f"Your excitement level is: {excitement_level}/10.")

# Checkbox
if st.checkbox("Do you like interactive apps?"):
    st.write("Streamlit is perfect for creating interactive applications!")
