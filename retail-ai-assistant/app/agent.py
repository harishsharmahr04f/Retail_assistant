from app.router import classify_intent
from app.tools.product_tools import search_products
from app.tools.order_tools import get_order
from app.tools.return_tools import evaluate_return


class RetailAgent:

    def handle(self, user_input: str):
        intent = classify_intent(user_input)

        if intent == "shopping":
            return self.handle_shopping(user_input)

        elif intent == "order_status":
            return self.handle_order(user_input)

        elif intent == "return_request":
            return self.handle_return(user_input)

        elif intent == "sizing":
            return "Please refer to our size chart or tell me your measurements."

        else:
            return "I can help with orders, returns, or product recommendations."

    # 🔹 Shopping Agent
    def handle_shopping(self, text):
        filters = {
            "size": "8",
            "max_price": 300,
            "sale": True
        }

        products = search_products(filters)

        if not products:
            return "No matching products found."

        response = "Here are some great options:\n"

        for p in products:
            response += f"- {p['title']} at ${p['price']} (Bestseller Score: {p['bestseller_score']})\n"

        response += "\nThese match your budget, size, and sale preference."

        return response

    # 🔹 Order Support
    def handle_order(self, text):
        num_str = ''.join(filter(str.isdigit, text))
        if not num_str:
            return "Please provide a valid order number."
        order_id = f"O{int(num_str):04d}"
        order = get_order(order_id)

        if not order:
            return "Sorry, I couldn't find your order."

        return f"Order {order_id} is confirmed. Product ID: {order['product_id']}"

    # 🔹 Return Logic
    def handle_return(self, text):
        num_str = ''.join(filter(str.isdigit, text))
        if not num_str:
            return "Please provide a valid order number."
        order_id = f"O{int(num_str):04d}"

        result = evaluate_return(order_id)

        return f"Return Status: {result}"