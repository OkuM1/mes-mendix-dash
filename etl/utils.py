import pandas as pd

def sanitize_orders(df):
    df = df.dropna(subset=["order_id", "line_id", "item_name", "quantity", "status"])
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0).astype(int)
    df["status"] = df["status"].str.lower().str.strip()
    return df


def compute_kpis(df):
    """Return KPI summary counts for each order status."""
    return df["status"].value_counts()
