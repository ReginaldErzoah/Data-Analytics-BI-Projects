import streamlit as st
import pandas as pd
from src.data_loader import load_and_prepare_data
from src.dq_metrics import compute_quality_metrics
from src.dq_visuals import (
    plot_error_by_payment,
    plot_error_by_location,
    plot_error_heatmap,
    plot_error_trend
)
import matplotlib.pyplot as plt  # needed for plt.close()

# --- Page Config ---
st.set_page_config(page_title="Data Quality & Error Cluster Dashboard", layout="wide")

st.title("Data Quality & Error Cluster Analysis Dashboard")
st.markdown("""
Explore data completeness, validity, and accuracy across transactions.
Identify recurring error clusters by **Location** and **Payment Method**, 
and track data quality trends over time.
""")

# --- Load Data ---
@st.cache_data
def load_data():
    return load_and_prepare_data("dirty_cafe_sales.csv")

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("Filter Data")
selected_location = st.sidebar.multiselect(
    "Select Location(s):", options=df["Location"].dropna().unique(), default=df["Location"].dropna().unique()
)
selected_payment = st.sidebar.multiselect(
    "Select Payment Method(s):", options=df["Payment Method"].dropna().unique(), default=df["Payment Method"].dropna().unique()
)

filtered_df = df[df["Location"].isin(selected_location) & df["Payment Method"].isin(selected_payment)]

# --- Metrics ---
dq_summary, accuracy_score, error_rate = compute_quality_metrics(filtered_df)

col1, col2, col3 = st.columns(3)
col1.metric("Overall Accuracy", f"{accuracy_score:.2f}%")
col2.metric("Error Rate", f"{error_rate:.2f}%")
col3.metric("Records Analyzed", f"{len(filtered_df):,}")

st.divider()

# --- Data Quality Summary Table ---
with st.expander("View Data Quality Summary Table"):
    st.dataframe(dq_summary.style.format("{:.2f}"))

# --- Charts ---
st.subheader("Error Rate by Payment Method")
plot_error_by_payment(filtered_df)

st.subheader("Error Rate by Location")
plot_error_by_location(filtered_df)

st.subheader("Error Cluster Heatmap (Location × Payment Method)")
plot_error_heatmap(filtered_df)

st.subheader("Error Rate Over Time")
plot_error_trend(filtered_df)


# --- Download Buttons ---
st.divider()
st.markdown("### Export Options")

csv_all = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download Filtered Data (CSV)", csv_all, "filtered_cafe_sales.csv", "text/csv")

error_data = filtered_df[filtered_df["has_error"]]
csv_errors = error_data.to_csv(index=False).encode("utf-8")
st.download_button("Download Only Error Records (CSV)", csv_errors, "error_records.csv", "text/csv")

