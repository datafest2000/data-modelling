from dotenv import dotenv_values
from datetime import datetime
from sqlalchemy import create_engine



def get_api_key():

    '''
    This is a function to retrieve openweather API key from a .env file

    parameters: No parameters
    Return value: an API KEY
    Return Type: String
    '''
    config = dict(dotenv_values('.env'))
    api_key = config.get('API_KEY')
    
    return api_key

    '''
    util.py is an helper function
    '''

def adjust_date(row):
    '''
    This is a helper function to convert the unix_datetime to a utc datetime while factoring in the timezone offset

    parameters:
    a dataframe row
    return value: a utc datetime
    return type: a datetime
    '''
    actual_unix_date = row['date'] - row['timezone']

    #convert to utc datetime
    utc_date = datetime.fromtimestamp(actual_unix_date)
    return utc_date


def get_engine():
   
    config = dict(dotenv_values('.env'))
    db_username = config.get('DB_USERNAME')
    db_password = config.get('DB_PASSWORD')
    db_host = config.get('DB_HOST')
    db_port = config.get('DB_PORT')
    db_name = config.get('DB_NAME')

    engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

    return engine
   