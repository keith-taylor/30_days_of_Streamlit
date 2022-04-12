from optparse import Values
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("Line chart")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])


cat_data = {
    "name": ["domestic cat", "osselot", "cheeta", "leopard", "lion", "tiger"],
    "height": [20, 45, 75, 120, 160, 180],
}

dog_data = {
    "name": [
        "chiwawa",
        "fox hound",
        "dobberma",
        "timber wolf",
        "grey wolf",
        "great dane",
    ],
    "height": [22, 57, 70, 125, 150, 175],
}


animal_df = pd.DataFrame(
    {
        "cat_data": pd.Series(cat_data["height"]),
        "dog_data": pd.Series(dog_data["height"]),
    }
)

st.line_chart(animal_df)


st.line_chart(chart_data)
