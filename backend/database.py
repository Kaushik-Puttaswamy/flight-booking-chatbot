
import json

with open("data/mock_orders.json") as f:
    ORDER_DATA = json.load(f)

with open("data/faq.json") as f:
    FAQ_DATA = json.load(f)

def init_db():
    print("Mock DB loaded.")

def get_order_status(user_id):
    return ORDER_DATA.get(user_id, "Order not found.")

def get_faq(message):
    for q, a in FAQ_DATA.items():
        if q.lower() in message.lower():
            return a
    return "Please contact support for detailed info."
