import asyncio
import json

from app.services.polymarket import get_markets
from app.services.database import save_market
from app.services.polymarket import get_markets
from app.services.database import save_market


async def track_markets():

    while True:

        markets = await get_markets(20)

        for market in markets:

            prices = market.get("outcomePrices", "[]")
            try:
                prices = json.loads(prices)
            except Exception:
                prices = []
                yes = float(prices[0]) if len(prices) > 0 else 0
                no = float(prices[1]) if len(prices) > 1 else 0

            save_market(
                str(market.get("id")),
                market.get("question"),
                yes,
                no,
                float(market.get("volume", 0)),
                float(market.get("liquidity", 0))
            )

        print("✅ Market snapshot saved")

        await asyncio.sleep(300)
