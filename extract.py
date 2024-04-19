import pandas as pd
import requests



def extract_data(file, api_key):
    '''
    This is a function to current weather condition from cities from all location on a file openweather API
    the file contains longitude and latitude

    parameters:
    - file - an xlsx file
    -api_key - openweathermap api_key

    return value: a pandas df
    type: pandas df object
    
    '''
    df1 = pd.read_excel(file)
    # initialize an empty list to hold the rows

    rows = []

    for index, row in df1.iterrows():
        lat = row['latitude']
        lon = row['longitude']
        
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
        
        response = requests.get(url)
        data = response.json()

        condition = data['weather'][0]['description']
        temp = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        city = data['name']
        date = data['dt']
        timezone = data['timezone']

        rows.append((city, condition, temp, pressure, humidity, wind_speed, date, timezone))
    weather_df = pd.DataFrame(rows, columns = ['city', 'condition', 'temp', 'pressure', 'humidity', 'wind_speed', 'date', 'timezone'])

    return weather_df       