import pandas as pd
import os

def preprocess(df, regions_df):
    # filter for summer season
    df = df[df['Season'] == 'Summer']

    # merge with regions_df
    df = df.merge(regions_df, on='NOC', how='left')

    # drop duplicates
    df.drop_duplicates(inplace=True)

    # convert medals to dummy variables
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    
    return df