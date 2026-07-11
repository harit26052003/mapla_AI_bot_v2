from app.services.polymarket import get_markets, get_market


async def markets_command():
    markets = await get_markets(5)

    if not markets:
        return "❌ No active markets found."

    message = "🔥 Top Live Polymarket Markets\n\n"

    for i, market in enumerate(markets, start=1):
        title = market.get("question", "Unknown Market")
        message += f"{i}. {title}\n"

    return message


async def details_command(index: int):
    market = await get_market(index)

    if not market:
        return "❌ Invalid market number."

    question = market.get("question", "Unknown")
    
    return (
        f"🤖 AI Signal\n\n"
        f"Question:\n{question}\n\n"
        f"Recommendation: 🟡 WAIT\n"
        f"Confidence: 70%\n\n"
        f"Reason:\n"
        f"• Live analysis not enabled yet\n"
        f"• AI module will be added next"
    )
