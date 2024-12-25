from PIL import Image
import streamlit as st

# Load and display an image
image = Image.open("images/example.jpg")  # Replace with your image file
st.image(image, caption="Sample Image", use_container_width=True)