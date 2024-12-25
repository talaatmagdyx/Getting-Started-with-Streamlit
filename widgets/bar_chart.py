import streamlit as st
import pandas as pd
import numpy as np
data = pd.DataFrame(
    np.random.randint(1, 100, size=(10, 3)),
    columns=["A", "B", "C"]
)
st.bar_chart(data)