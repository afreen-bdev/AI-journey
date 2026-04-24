import streamlit as st

st.title('This is Title')
st.caption('Using st.title() you can display the text in title format')

st.header('This is header')
st.caption('Using st.title() you can display the text in title format')

st.subheader('This is subheader')
st.caption('Using st.title() you can display the text in title format')

#display the code in page
st.markdown('---')
st.subheader("Generate random numbers")
body = """
import numpy as np

def generate_random(size):
    rand = np.random.random(size=size)
    return rand

number = generate_randowm(10)
"""

st.code(body,language='python')

#Latex
st.subheader("LATEX")
formula = """

a + ar + ar^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} a r^k

"""
st.latex(formula)