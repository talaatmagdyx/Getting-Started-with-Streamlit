import streamlit as st

# Add a dropdown menu
option = st.selectbox(
    "What's your favorite programming language?",
    ["Python", "JavaScript", "C++", "Java"]
)
st.write(f"You selected: {option}")