import streamlit as st
import time

## progress bar
st.header('st.progress')
st.caption('Display a progress bar')

def progress_bar():
    for percent_Complete in range(1,121,20):
        time.sleep(0.5)
        percent_Complete = min(percent_Complete,100)
        my_bar.progress(percent_Complete)

##Spinner
with st.spinner("Something is processing..."):
    my_bar = st.progress(0)
    progress_bar()
