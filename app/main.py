import asyncio
import logging
import platform

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.bot.handlers.commands import command_router
from app.bot.handlers.callbacks import callback_router
from app.bot.handlers.states import states_router

from app.settings.config import Settings

settings = Settings()
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

bot = Bot(settings.TELEGRAM_BOT_TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher(storage=MemoryStorage())



async def main():
    dp.include_routers(states_router, command_router, callback_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Goodbye!")