import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_bike_rentals_by_day_type_and_season(daily_df):
    grouped_data = daily_df.groupby(['season', 'day_type'])['cnt'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', hue='day_type', data=grouped_data, palette='Set1')
    plt.title('Average Bike Rentals by Day Type and Season', fontsize=16)
    plt.xlabel('Season', fontsize=14)
    plt.ylabel('Average Rentals (cnt)', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def plot_average_rentals_by_time_bin(hourly_df):
    hourly_df['time_bin'] = hourly_df['hr'].apply(lambda hr: 'Pagi (6-10)' if 6 <= hr < 10 else
                                                 'Siang (10-14)' if 10 <= hr < 14 else
                                                 'Sore (14-18)' if 14 <= hr < 18 else
                                                 'Malam (18-22)' if 18 <= hr < 22 else
                                                 'Tengah Malam (22-6)')
    grouped = hourly_df.groupby('time_bin')['cnt'].mean().reset_index().sort_values(by='cnt', ascending=False)
    highlight_color = 'gold'
    colors = ['gold' if bin == 'Sore (14-18)' else 'gray' for bin in grouped['time_bin']]
    plt.figure(figsize=(10, 6))
    sns.barplot(data=grouped, x='time_bin', y='cnt', palette=colors)
    plt.title('Average Bike Rentals by Time of Day', fontsize=16)
    plt.xlabel('Time of Day', fontsize=14)
    plt.ylabel('Average Rentals (cnt)', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
