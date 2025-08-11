import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.config import Settings

settings = Settings()

bot = Bot(settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello there!")

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())