import streamlit as st
from data_loader import load_data
from preprocessing import preprocess_data
import os
from visualizations import plot_bike_rentals_by_day_type_and_season, plot_average_rentals_by_time_bin
from utils import display_summary


def main():
    st.title("Bike Rental Analysis Dashboard")

    st.sidebar.title("Configuration")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    hourly_path = os.path.join(base_dir, "../Data/hour.csv")
    daily_path = os.path.join(base_dir, "../Data/day.csv")

    # Load and preprocess data
    hourly_df, daily_df = load_data(hourly_path, daily_path)
    hourly_df, daily_df = preprocess_data(hourly_df, daily_df)

    # Sidebar navigation
    page = st.sidebar.radio("Select Page", ["Summary", "Visualizations"])

    if page == "Summary":
        display_summary(hourly_df, daily_df)
    elif page == "Visualizations":
        st.subheader("Visualizations")
        plot_bike_rentals_by_day_type_and_season(daily_df)
        plot_average_rentals_by_time_bin(hourly_df)


if __name__ == "__main__":
    main()
