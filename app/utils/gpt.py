import asyncio
import platform

from openai import AsyncOpenAI, OpenAIError
from app.settings.config import Settings
from app.utils.resource_loader import resources

settings = Settings()
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class AsyncOpenAiClient:
    def __init__(self):
        self._client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def send_message(self, message: str, sys_prompt: str = "You are basic assistant") -> str:
        try:
            response = await self._client.chat.completions.create(
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": message}
                ],
                model="gpt-3.5-turbo",
                temperature=settings.TEMPERATURE,
                max_tokens=settings.MAX_TOKENS
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            return "Sorry, temporary OpenAI API call failed."


async def main():
    client = AsyncOpenAiClient()
    try:
        test_reply = await client.send_message(resources.prompts.random)
        print(test_reply)
    except KeyboardInterrupt as e:
        print("Goodbye")


if __name__ == '__main__':
    asyncio.run(main())