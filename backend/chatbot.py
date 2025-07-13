
from backend.intents import classify_intent
from backend.database import get_order_status, get_faq
from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def handle_message(user_id, message):
    intent = classify_intent(message)

    if intent == "track_order":
        return get_order_status(user_id)
    elif intent == "faq":
        faq_answer = get_faq(message)
        return faq_answer
    else:
        return gpt_fallback(message)

def gpt_fallback(message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion.choices[0].message["content"]
