import streamlit as st
import pandas as pd
import sys
import os

# Add the parent directory to the path so we can import from data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.utils import helper, preprocess

# Get the absolute path to the data directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(os.path.dirname(os.path.dirname(current_dir)), 'data')

df = pd.read_csv(os.path.join(data_dir, "athlete_events.csv"))
regions_df = pd.read_csv(os.path.join(data_dir, "noc_regions.csv"))

# Preprocess the data
df = preprocess(df, regions_df)

st.sidebar.title('Olympics Data Analysis')

st.dataframe(df)

user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis')
)

if user_menu == 'Medal Tally':
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)




