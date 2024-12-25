import streamlit as st
import pandas as pd
import numpy as np

# Add a checkbox
if st.checkbox("Show a random data table"):
    data = pd.DataFrame(
        np.random.randn(10, 5),
        columns=["A", "B", "C", "D", "E"]
    )
    st.write(data)