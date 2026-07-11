import os
import httpx
from fastapi import FastAPI
from app.commands import markets_command

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

        async with httpx.AsyncClient() as client:

            if text == "/start":
                await client.post(
                    f"{API}/sendMessage",
                    json={
                        "chat_id": chat_id,
                        "text": "🔥 Vanakkam Mapla!\n\nMapla AI Bot v2 Online 🚀"
                    }
                )

            elif text == "/help":
                await client.post(
                    f"{API}/sendMessage",
                    json={
                        "chat_id": chat_id,
                        "text": "/start\n/help\n/markets"
                    }
                )

            elif text == "/markets":
                result = await markets_command()

                await client.post(
                    f"{API}/sendMessage",
                    json={
                        "chat_id": chat_id,
                        "text": result
                    }
                )

    except Exception as e:
        print("Webhook Error:", e)

    return {"ok": True}
