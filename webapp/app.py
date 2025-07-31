import streamlit as st
import pandas as pd

st.sidebar.title('Olympics Data Analysis')

page = st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis')
)



