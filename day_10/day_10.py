import streamlit as st

st.header("st.selectbox")

option = st.selectbox(
    "What is your favorite colour?",
    ("Magenta", "Cyan", "Ecru", "Prussian Military Grey", "Vermillion"),
)

st.write("Your favorite color is ", option)
