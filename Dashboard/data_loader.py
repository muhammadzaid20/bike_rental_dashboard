import pandas as pd

def load_data(hourly_path, daily_path):
    hourly_df = pd.read_csv(hourly_path)
    daily_df = pd.read_csv(daily_path)
    return hourly_df, daily_df
