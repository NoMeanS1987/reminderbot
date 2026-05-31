import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send_message(text: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    resp = requests.post(url, json={"chat_id": CHAT_ID, "text": text})
    print(f"HTTP {resp.status_code}: {resp.text}")
    print(f"chat_id used (repr): {CHAT_ID!r}")
    resp.raise_for_status()


if __name__ == "__main__":
    send_message("⏰ Напоминание! Прошло 30 минут.")
