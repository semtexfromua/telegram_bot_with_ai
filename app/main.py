import asyncio
import logging


from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.config import Settings

settings = Settings()

bot = Bot(settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(settings.main_text)

@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(settings.main_text)

@dp.message(Command("gpt"))
async def gpt_cmd(message: Message):
    await message.answer(settings.gpt_text)

@dp.message(Command("quiz"))
async def quiz_cmd(message: Message):
    await message.answer(settings.quiz_text)

@dp.message(Command("random"))
async def random_cmd(message: Message):
    await message.answer(settings.random_text)

@dp.message(Command("talk"))
async def talk_cmd(message: Message):
    await message.answer(settings.talk_text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Goodbye!")