import asyncio
import logging
import platform

from aiogram import Bot, Dispatcher
from app.bot.handlers.commands import router

from app.settings.config import Settings

settings = Settings()
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

bot = Bot(settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Goodbye!")