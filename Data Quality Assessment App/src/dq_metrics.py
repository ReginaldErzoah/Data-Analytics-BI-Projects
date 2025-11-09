import pandas as pd
import numpy as np

def compute_quality_metrics(df):
    placeholders = ["UNKNOWN", "ERROR", "", " ", None, np.nan]

    completeness = df.notna().sum() / len(df) * 100
    validity = {col: (~df[col].isin(placeholders)).sum() / len(df) * 100 for col in df.columns}
    validity = pd.Series(validity)

    accuracy_score = df["valid_total"].mean() * 100
    error_rate = df["has_error"].mean() * 100

    dq_summary = pd.DataFrame({
        "Completeness (%)": completeness.round(2),
        "Validity (%)": validity.round(2)
    })
    dq_summary.loc["Overall_Accuracy"] = [None, round(accuracy_score, 2)]

    return dq_summary, accuracy_score, error_rate
