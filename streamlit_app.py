import streamlit as st

st.header('st.button')
if st.button('Say Yo!'):
    st.write("Say yo to you!")
else:
    st.write("Good-day Sir!")
