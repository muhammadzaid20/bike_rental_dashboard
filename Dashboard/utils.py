import streamlit as st

def display_summary(hourly_df, daily_df):
    st.write("### Summary Statistics")
    st.write("#### Hourly Data")
    st.write(hourly_df.describe())
    st.write("#### Daily Data")
    st.write(daily_df.describe())
