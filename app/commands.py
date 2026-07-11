from app.services.polymarket import get_markets, get_market
from app.services.ai import analyze_market


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
    volume = market.get("volume", "N/A")
    liquidity = market.get("liquidity", "N/A")

    return (
        f"📊 Market Details\n\n"
        f"Question:\n{question}\n\n"
        f"Volume: {volume}\n"
        f"Liquidity: {liquidity}"
    )


async def signal_command(index: int):
    market = await get_market(index)

    if not market:
        return "❌ Invalid market number."

    question = market.get("question", "Unknown")
    volume = market.get("volume", "N/A")
    liquidity = market.get("liquidity", "N/A")

    analysis = await analyze_market(
        question,
        volume,
        liquidity
    )

    return f"🤖 AI Analysis\n\n{analysis}"
