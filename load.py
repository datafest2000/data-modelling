import pandas as df



def load_data(df, engine, table):
    '''
    this is function that loads data to a table on postgres database

    parameters:
    - df - a dataframe
    - engine - a sqlalchemy engine
    - table - a database table from postgres
    - return value - null 
    - return type - null
    '''

    df.to_sql('table', con=engine, if_exists='append', index=False)