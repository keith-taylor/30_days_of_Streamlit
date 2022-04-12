import streamlit as st

st.header("st.multiselect")

options = st.multiselect(
    "What are your favorite colours?",
    [
        "Magenta",
        "Cyan",
        "Ecru",
        "Prussian Military Grey",
        "Vermillion",
        "Mongolian Yellow",
        "Italian Peach",
    ],
    ["Vermillion", "Ecru"],
)

st.write("You selected:", options)
