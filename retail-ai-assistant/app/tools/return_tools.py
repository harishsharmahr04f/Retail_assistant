from datetime import datetime
from app.tools.order_tools import get_order
from app.tools.product_tools import get_product

with open("app/data/policy.txt") as f:
    policy_text = f.read()


def evaluate_return(order_id: str):
    order = get_order(order_id)

    if not order:
        return "Order not found"

    product = get_product(order["product_id"])
    if not product:
        return "Product not found"

    order_date = datetime.strptime(order["order_date"], "%Y-%m-%d")
    days = (datetime.now() - order_date).days

    is_sale = product.get("is_sale", False)
    
    if is_sale:
        if days <= 7:
            return "Eligible for store credit only (Sale Item)"
        else:
            return f"Not eligible for return (Sale Items must be returned within 7 days. It has been {days} days)"
    else:
        if days <= 14:
            return "Eligible for full refund"
        else:
            return f"Not eligible for return (Normal Items must be returned within 14 days. It has been {days} days)"