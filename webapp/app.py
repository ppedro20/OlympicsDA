import streamlit as st
import pandas as pd
import sys
import os

# Clear Streamlit cache
st.cache_data.clear()

# Add the parent directory to the path so we can import from data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.utils import helper
from data.utils.preprocess import preprocess

df = pd.read_csv( "data/athlete_events.csv")
regions_df = pd.read_csv( "data/noc_regions.csv")

# Preprocess the data
df = preprocess(df, regions_df)
st.sidebar.title('Olympics Data Analysis')

user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")

    years, country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)

    # title
    if selected_country == 'Overall' and selected_year == 'Overall':
        st.title("Overall Tally")
    elif selected_country == 'Overall' and selected_year != 'Overall':
        st.title(f"{selected_year} Olympics")
    elif selected_country != 'Overall' and selected_year != 'Overall':
        st.title(f"{selected_country} Performance in {selected_year} Olympics")
    elif selected_country != 'Overall' and selected_year == 'Overall':
        st.title(f"{selected_country} Overall Performance")

    st.table(medal_tally)



