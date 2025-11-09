import streamlit as st
import pandas as pd
from dq_visuals import plot_error_by_payment, plot_error_by_location, plot_error_heatmap, plot_error_trend

# Load your data
df = pd.read_csv("your_data.csv", parse_dates=["Transaction Date"])

st.title("Data Quality Dashboard")

# Plot: Error by Payment Method
st.subheader("Error Rate by Payment Method")
fig1 = plot_error_by_payment(df)
st.pyplot(fig1)

# Plot: Error by Location
st.subheader("Error Rate by Location")
fig2 = plot_error_by_location(df)
st.pyplot(fig2)

# Plot: Error Heatmap
st.subheader("Error Clusters by Location × Payment Method")
fig3 = plot_error_heatmap(df)
st.pyplot(fig3)

# Plot: Error Trend
st.subheader("Error Rate Over Time")
fig4 = plot_error_trend(df)
st.pyplot(fig4)
