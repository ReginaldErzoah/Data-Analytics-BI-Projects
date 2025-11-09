import pandas as pd
import numpy as np

def load_and_prepare_data(path="dirty_cafe_sales.csv"):
    df = pd.read_csv(path)

    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")

    numeric_cols = ["Quantity", "Price Per Unit", "Total Spent"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["valid_total"] = np.isclose(
        df["Total Spent"],
        df["Quantity"] * df["Price Per Unit"],
        atol=0.01,
        equal_nan=False
    )

    placeholders = ["UNKNOWN", "ERROR", "", " ", None, np.nan]

    df["has_error"] = (
        df.isna().any(axis=1) |
        df.isin(placeholders).any(axis=1) |
        (~df["valid_total"])
    )

    return df
