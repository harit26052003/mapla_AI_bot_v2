import httpx

BASE_URL = "https://gamma-api.polymarket.com"


async def get_markets(limit: int = 5):
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(
            f"{BASE_URL}/markets",
            params={
                "closed": "false",
                "limit": limit
            }
        )

        response.raise_for_status()
        return response.json()
async def get_market(index: int):
    markets = await get_markets(10)

    if index < 1 or index > len(markets):
        return None

    return markets[index - 1]
