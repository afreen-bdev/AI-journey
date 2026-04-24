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

# info
st.subheader('st.info')
st.info('This information message')

st.subheader('st.success')
st.success('This is success message')

st.subheader('st.warning')
st.warning('This is warning')

st.subheader('st.error')
st.error('this is the error')

time.sleep(2)
st.balloons()