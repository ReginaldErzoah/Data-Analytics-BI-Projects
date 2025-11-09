import seaborn as sns
import matplotlib.pyplot as plt

def plot_error_by_payment(df):
    error_by_payment = df.groupby("Payment Method")["has_error"].mean() * 100
    fig, ax = plt.subplots()
    sns.barplot(x=error_by_payment.values, y=error_by_payment.index, palette="coolwarm", ax=ax)
    ax.set_title("Error Rate by Payment Method")
    ax.set_xlabel("Error Rate (%)")
    return fig

def plot_error_by_location(df):
    error_by_location = df.groupby("Location")["has_error"].mean() * 100
    fig, ax = plt.subplots()
    sns.barplot(x=error_by_location.values, y=error_by_location.index, palette="coolwarm", ax=ax)
    ax.set_title("Error Rate by Location")
    ax.set_xlabel("Error Rate (%)")
    return fig

def plot_error_heatmap(df):
    error_pivot = df.pivot_table(values="has_error", index="Location", columns="Payment Method", aggfunc="mean") * 100
    fig, ax = plt.subplots(figsize=(7,5))
    sns.heatmap(error_pivot, annot=True, fmt=".1f", cmap="Reds", ax=ax)
    ax.set_title("Error Clusters by Location × Payment Method")
    return fig

def plot_error_trend(df):
    df["Month"] = df["Transaction Date"].dt.to_period("M")
    error_by_month = df.groupby("Month")["has_error"].mean() * 100
    fig, ax = plt.subplots()
    error_by_month.plot(marker="o", color="crimson", ax=ax)
    ax.set_title("Error Rate Over Time")
    ax.set_xlabel("Month")
    ax.set_ylabel("Error Rate (%)")
    return fig
