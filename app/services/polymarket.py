import httpx

BASE_URL = "https://gamma-api.polymarket.com"


async def get_markets():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/markets",
            params={"closed": "false"}
        )

        response.raise_for_status()

        return response.json()
