import streamlit as st

st.header("st.latex")

st.latex(
    r"""
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    """
)
st.latex(
    r"""
    \begin{bmatrix} 1 & 3 & 2\\ 4 & 0 & 1\end{bmatrix} ⨉ \begin{bmatrix} 1 & 3\\ 0 & 1 \\ 5 & 2 \end{bmatrix} = ?
    """
)
