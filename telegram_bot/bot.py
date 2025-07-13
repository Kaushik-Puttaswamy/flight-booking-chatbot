
import os
import requests
from telegram.ext import Updater, MessageHandler, Filters

API_URL = "http://localhost:8000/chat"

def handle_message(update, context):
    user_id = str(update.effective_user.id)
    msg = update.message.text
    res = requests.post(API_URL, json={"user_id": user_id, "message": msg})
    update.message.reply_text(res.json()["response"])

def main():
    updater = Updater(os.getenv("TELEGRAM_BOT_TOKEN"), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
