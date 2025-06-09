import requests
import pandas as pd
from etl.utils import sanitize_orders, compute_kpis

def fetch_orders(api_url: str) -> pd.DataFrame:
    """Fetch orders from the API and return a sanitized DataFrame."""
    response = requests.get(api_url)
    response.raise_for_status()
    orders = response.json()
    df = pd.DataFrame(orders)
    return sanitize_orders(df)


def main(api_url: str = "http://localhost:8000/api/v1/workorders"):
    df = fetch_orders(api_url)
    pending_orders = df[df["status"] == "pending"]
    print("Pending Orders:")
    print(pending_orders[["order_id", "line_id", "item_name", "quantity"]])

    print("\nKPI Summary:")
    print(compute_kpis(df))


if __name__ == "__main__":
    main()
