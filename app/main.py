import os
import httpx
from fastapi import FastAPI
from app.commands import markets_command, details_command, signal_command

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
                        "text": "/start\n/help\n/markets\n/details 1\n/signal 1"
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

            elif text.startswith("/details"):

                try:
                    index = int(text.split()[1])

                    result = await details_command(index)

                    await client.post(
                        f"{API}/sendMessage",
                        json={
                            "chat_id": chat_id,
                            "text": result
                        }
                    )

                except Exception:
                    await client.post(
                        f"{API}/sendMessage",
                        json={
                            "chat_id": chat_id,
                            "text": "Usage:\n/details 1"
                        }
                    )
            elif text.startswith("/signal"):

                try:
                    index = int(text.split()[1])

                    result = await signal_command(index)

                    await client.post(
                        f"{API}/sendMessage",
                        json={
                            "chat_id": chat_id,
                            "text": result
                        }
                    )

                except Exception as e:
                    print(e)
                    
                    await client.post(
                        f"{API}/sendMessage",
                        json={
                            "chat_id": chat_id,
                            "text": str(e)
        }
    )
    except Exception as e:
        print("Webhook Error:", e)

    return {"ok": True}
