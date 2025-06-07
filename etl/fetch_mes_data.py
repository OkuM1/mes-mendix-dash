import requests
import pandas as pd
from etl.utils import sanitize_orders

url = "http://localhost:8000/api/v1/workorders"
response = requests.get(url)
orders = response.json()

df = pd.DataFrame(orders)
df = sanitize_orders(df)

pending_orders = df[df["status"] == "pending"]
print("Pending Orders:")
print(pending_orders[["order_id", "line_id", "item_name", "quantity"]])

print("\nKPI Summary:")
print(df["status"].value_counts())
