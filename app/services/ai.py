from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def analyze_market(question: str):
    prompt = f"""
You are a professional Polymarket analyst.

Market:
{question}

Respond in this format:

Recommendation:
Confidence:
Reason:
Risk:
"""

    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a prediction market analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
