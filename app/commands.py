from app.services.polymarket import get_markets

async def markets_command():
    markets = await get_markets(5)

    if not markets:
        return "❌ No active markets found."

    message = "🔥 *Top Live Polymarket Markets*\n\n"

    for i, market in enumerate(markets, start=1):
        title = market.get("question", "Unknown Market")
        message += f"{i}. {title}\n"

    return message
