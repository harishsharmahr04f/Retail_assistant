import pandas as pd

orders_df = pd.read_csv("app/data/orders.csv")

def get_order(order_id: str):
    result = orders_df[orders_df["order_id"] == order_id]
    if result.empty:
        return None
    return result.iloc[0].to_dict()