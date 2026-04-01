def classify_intent(user_input: str):
    text = user_input.lower()

    if "order" in text and "return" in text:
        return "return_request"
    elif "order" in text:
        return "order_status"
    elif "size" in text or "fit" in text:
        return "sizing"
    elif "recommend" in text or "need" in text:
        return "shopping"
    else:
        return "general"