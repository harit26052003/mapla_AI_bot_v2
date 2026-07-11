import os
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

async def analyze_market(question: str, volume, liquidity):
    prompt = f"""
You are an expert Polymarket analyst.

Market:
{question}

Volume:
{volume}

Liquidity:
{liquidity}

Give only:

Recommendation:
Confidence:
Reason:
Risk:
"""

    response = await client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "system",
                "content": "You are an expert prediction market analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
