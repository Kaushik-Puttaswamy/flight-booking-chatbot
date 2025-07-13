
def classify_intent(msg):
    msg = msg.lower()
    if "track" in msg or "where is my order" in msg:
        return "track_order"
    elif "refund" in msg or "cancel" in msg:
        return "refund"
    elif "return policy" in msg or "how long" in msg:
        return "faq"
    else:
        return "fallback"
