from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import bot.keyboards as kb

from app.config import Settings
from bot.keyboards import main_menu, random_func_keyboard

router = Router()
settings = Settings()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(settings.main_text, reply_markup=main_menu)

@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(settings.main_text)

@router.message(Command("gpt"))
async def gpt_cmd(message: Message):
    await message.answer(settings.gpt_text)

@router.message(Command("quiz"))
async def quiz_cmd(message: Message):
    await message.answer(settings.quiz_text)

@router.message(Command("random"))
async def random_cmd(message: Message):
    await message.answer(settings.random_text, reply_markup=random_func_keyboard)

@router.message(Command("talk"))
async def talk_cmd(message: Message):
    await message.answer(settings.talk_text)