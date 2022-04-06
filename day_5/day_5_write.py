import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

day_x_of = 5

st.title(f"This is day {day_x_of} of: 30 Days of Streamlit")
st.header(f"Day {day_x_of} is 'st.write' day!")
st.write(' ')

# Example 1
st.write('Hello, *world!* :sunglasses:')

# Example 2
st.write(1234)

# Example 3
my_st_df_1 = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

st.write(my_st_df_1)

# Example 4
st.write('Below is a DataFrame: ', my_st_df_1, 'Above is a DataFrame.')

# Example 5
my_st_df_2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(my_st_df_2).mark_circle().encode(
    x='a', y='b', size='c', tooltip=['a', 'b', 'c'])

st.write(c)
st.caption('This is a chart of some rando data.')

# Excample 6

st.markdown('### This is a Markdown title')
st.markdown('This is some markdown body text: some in **bold**, some in *italics*!')

# Example 7

st.latex(r'''
          \begin{bmatrix} 1 & 0 \\ 2 & 5 \\ 3 & 1 \end{bmatrix} + \begin{bmatrix}4 & 0.5 \\2 & 5 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix}5 & 0.5 \\ 4 & 10 \\ 3 & 2 \end{bmatrix}
         ''')
