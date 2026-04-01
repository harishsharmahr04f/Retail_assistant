import pandas as pd

products_df = pd.read_csv("app/data/products.csv")

def search_products(filters: dict):
    df = products_df.copy()

    if "size" in filters:
        df = df[df["sizes_available"].str.contains(str(filters["size"]), na=False)]

    if "max_price" in filters:
        df = df[df["price"] <= filters["max_price"]]

    if "sale" in filters:
        df = df[df["is_sale"] == True]

    df = df.sort_values(by="bestseller_score", ascending=False)

    return df.head(3).to_dict(orient="records")


def get_product(product_id: str):
    result = products_df[products_df["product_id"] == product_id]
    if result.empty:
        return None
    return result.iloc[0].to_dict()