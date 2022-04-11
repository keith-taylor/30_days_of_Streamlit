import streamlit as st
from datetime import time, datetime

st.header("st.slider")

# Example 1
st.subheader("My Slider")

age = st.slider("How old are you?", 0, 130, 35)
st.write("I'm ", age, "years old")

# Example 2

st.subheader("My Range slider")

default_number = 250.0
values = st.slider(
    "Select a range of values", 0.0, 1000.0, (default_number, default_number + 100)
)
st.write("Values:", values)

# Example 3

st.subheader("My Range time slider")

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader("Datetime slider")

start_time = st.slider(
    "When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm"
)
st.write("Start time:", start_time)
