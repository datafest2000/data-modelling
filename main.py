from util import get_engine, get_api_key
from extract import extract_data
from transform import transform_data 
from load import load_data


def main():
    engine = get_engine()
    api_key = get_api_key()

    # extract data
    weather_df = extract_data(file='cities.xlsx', api_key=api_key)
    print('data extracted successfully')

    # transform data
    df = transform_data(weather_df)
    print('data tranformed successfully')

    # load data
    load_data(df=df, engine=engine, table='weather')
    print('data loaded successfully')


if __name__ == '__main__':
    main()
    print('pipeline ran successfully')