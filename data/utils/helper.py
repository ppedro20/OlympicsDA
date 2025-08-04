import numpy as np
import pandas as pd

def medal_tally(df):
    # drop duplicates
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    # group by region and sum the medals
    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()

    # add total column
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    # convert to int
    medal_tally['Gold'] = medal_tally['Gold'].astype('int')
    medal_tally['Silver'] = medal_tally['Silver'].astype('int')
    medal_tally['Bronze'] = medal_tally['Bronze'].astype('int')
    medal_tally['Total'] = medal_tally['Total'].astype('int')

    return medal_tally

def country_year_list(df):
    # Ensure Year column is numeric for proper sorting
    df_copy = df.copy()
    df_copy['Year'] = pd.to_numeric(df_copy['Year'], errors='coerce')
    
    years = df_copy['Year'].dropna().unique().tolist()
    years.sort()
    years.insert(0, 'Overall')
    
    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')

    return years, country

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    
    # Ensure Year column is numeric
    medal_df['Year'] = pd.to_numeric(medal_df['Year'], errors='coerce')
    
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()
        x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']

        # convert to int
        x['Gold'] = x['Gold'].astype('int')
        x['Silver'] = x['Silver'].astype('int')
        x['Bronze'] = x['Bronze'].astype('int')
        x['Total'] = x['Total'].astype('int')

    return x
