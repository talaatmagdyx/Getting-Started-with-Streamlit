import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["X", "Y", "Z"]
)
st.line_chart(data)