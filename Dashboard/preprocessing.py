import pandas as pd
import streamlit as st

def preprocess_data(hourly_df, daily_df):
    # Mapping dictionaries
    season_map = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    yr_map = {0: '2011', 1: '2012'}
    mnth_map = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    weekday_map = {
        0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
        4: 'Thursday', 5: 'Friday', 6: 'Saturday'
    }
    weathersit_map = {
        1: 'Clear, Few clouds, Partly cloudy, Partly cloudy',
        2: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
        3: 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
        4: 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog',
    }
    daytype_map = {1: 'Weekend', 2: 'Holiday', 3: 'Workingday'}

    # Fungsi untuk menentukan jenis hari
    def determine_day_type(row):
        if row['weekday'] in ['Saturday', 'Sunday']:  # Weekend
            return 'Weekend'
        elif row.get('holiday', 0) == 1:  # Holiday
            return 'Holiday'
        else:
            return 'Workingday'

    # Tambahkan kolom 'day_type'
    daily_df['day_type'] = daily_df.apply(determine_day_type, axis=1)
    hourly_df['day_type'] = hourly_df.apply(determine_day_type, axis=1)

    # Apply mappings
    for df in [hourly_df, daily_df]:
        df['season'] = df['season'].map(season_map)
        df['yr'] = df['yr'].map(yr_map)
        df['mnth'] = df['mnth'].map(mnth_map)
        df['weekday'] = df['weekday'].map(weekday_map)
        df['weathersit'] = df['weathersit'].map(weathersit_map)
        df['weathersit'] = df['weathersit'].replace({
            'Clear, Few clouds, Partly cloudy, Partly cloudy': 'Clear, Partly cloudy',
            'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist': 'Mist, Cloudy',
            'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds': 'Light Snow, Light Rain, Thunderstorm',
            'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog': 'Heavy Rain, Ice Pellets, Snow, Fog',
        })

    # Apply denormalization
    hourly_df['temp'] = hourly_df['temp'] * 41
    daily_df['temp'] = daily_df['temp'] * 41
    hourly_df['atemp'] = hourly_df['atemp'] * 50
    daily_df['atemp'] = daily_df['atemp'] * 50
    hourly_df['hum'] = hourly_df['hum'] * 100
    daily_df['hum'] = daily_df['hum'] * 100
    hourly_df['windspeed'] = hourly_df['windspeed'] * 67
    daily_df['windspeed'] = daily_df['windspeed'] * 67

    # Remove irrelevant columns
    hourly_df.drop(columns=['instant', 'holiday', 'workingday'], inplace=True)
    daily_df.drop(columns=['instant', 'holiday', 'workingday'], inplace=True)

    return hourly_df, daily_df
