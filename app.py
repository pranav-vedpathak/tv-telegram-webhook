from flask import Flask, request, abort
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
SECRET_KEY = os.environ.get("TV_SECRET")

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_key = request.headers.get("X-Secret-Key")

    if incoming_key != SECRET_KEY:
        abort(403)

    data = request.json
    message = data.get("message", "TradingView Alert")

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, json=payload)

    return "ok"

@app.route("/")
def home():
    return "Webhook is running"
