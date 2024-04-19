from util import adjust_date
import pandas as pd



def transform_data(df1):
    '''
    This function transforms the extracted weather data to convert time from unix to utc
    and also drop some columns.

    Parameters:
    a dataframe df
    Return value: a dataframe
    return type: a pandas dataframe object
    '''

    df1['reading_date'] = df1.apply(adjust_date, axis=1)

    # drop columns
    clean_df = df1.drop(['date', 'timezone'], axis=1)

    return clean_df