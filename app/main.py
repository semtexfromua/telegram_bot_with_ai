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
async def start(message: Message):
    await message.answer("Hello there!")


@dp.message(Command("help"))
async def get_help(message: Message):
    await message.answer("You need help?")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Goodbye!")