import asyncio
from openai import AsyncOpenAI

from app.config import Settings

settings = Settings()
client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


async def main() -> None:
    response = await client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=[{"role": "user", "content": "prompt"}],
       max_tokens=settings.MAX_TOKENS,
       temperature=settings.TEMPERATURE)

    print(response.choices[0].message.content)

asyncio.run(main())