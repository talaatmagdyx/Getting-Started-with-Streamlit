import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Welcome to My First Streamlit App 🎉")
# Input box for user name
name = st.text_input("What's your name?")
# Display a personalized greeting
if name:
    st.write(f"Hello, {name}! Streamlit is amazing, isn't it?")
# Add a slider for selecting a number
number = st.slider("Pick a number between 1 and 100", 1, 100)
st.write(f"You selected: {number}")
# Generate and display a random chart
st.write("Here's a random chart:")
data = pd.DataFrame(
    np.random.randn(20, 3),  # Generate random data
    columns=['A', 'B', 'C']
)
st.line_chart(data)






