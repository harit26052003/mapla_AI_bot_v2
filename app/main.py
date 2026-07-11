import os
import httpx
from fastapi import FastAPI

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API = f"https://api.telegram.org/bot{BOT_TOKEN}"


@app.get("/")
async def home():
    return {"status": "Mapla AI Bot Running 🚀"}


@app.post("/webhook")
async def webhook(update: dict):
    try:
        message = update.get("message", {})
        text = message.get("text", "")
        chat = message.get("chat", {})
        chat_id = chat.get("id")

        if text == "/start":
            await httpx.AsyncClient().post(
                f"{API}/sendMessage",
                json={
                    "chat_id": chat_id,
                    "text": "🔥 Vanakkam Mapla!\n\nMapla AI Bot v2 Online 🚀"
                }
            )

        elif text == "/help":
            await httpx.AsyncClient().post(
                f"{API}/sendMessage",
                json={
                    "chat_id": chat_id,
                    "text": "/start\n/help"
                }
            )

    except Exception as e:
        print(e)

    return {"ok": True}
