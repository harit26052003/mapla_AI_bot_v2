from app.services.polymarket import get_market

async def details_command(index: int):
    market = await get_market(index)

    if not market:
        return "❌ Invalid market number."

    question = market.get("question", "Unknown")
    yes = market.get("outcomePrices", ["?", "?"])[0]
    no = market.get("outcomePrices", ["?", "?"])[1]
    volume = market.get("volume", "N/A")
    liquidity = market.get("liquidity", "N/A")

    return (
        f"📊 Market Details\n\n"
        f"Question:\n{question}\n\n"
        f"YES : {yes}\n"
        f"NO  : {no}\n\n"
        f"Volume : {volume}\n"
        f"Liquidity : {liquidity}"
    )
