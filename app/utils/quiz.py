import asyncio
import json

from app.utils.gpt import AsyncOpenAiClient
from app.utils.resource_loader import resources

client = AsyncOpenAiClient()


async def get_question(theme: str) -> dict:
    gpt_answer = await client.send_message_and_get_json(theme, resources.prompts.quiz)
    return gpt_answer


async def main():
    question = await get_question("quiz_python")
    for key, value in question.items():
        if isinstance(value, dict):
            print(key + ":")
            for sub_key, sub_value in value.items():
                print(f"\t {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")


if __name__ == "__main__":
    asyncio.run(main())
