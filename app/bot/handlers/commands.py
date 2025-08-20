from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BufferedInputFile

from app.settings.config import Settings
from app.bot.keyboards import main_menu, random_func_keyboard
from app.utils.resource_loader import resources

router = Router()
settings = Settings()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.main, filename="main.jpg"),
        caption=resources.messages.main,
        reply_markup=main_menu,
        parse_mode="Markdown")

@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.main, filename="main.jpg"),
        caption=resources.messages.main,
        reply_markup=main_menu,
        parse_mode="Markdown")

@router.message(Command("random"))
async def random_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.random, filename="random.jpg"),
        caption=resources.messages.random,
        reply_markup=main_menu,
        parse_mode="Markdown")

@router.message(Command("gpt"))
async def gpt_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.gpt, filename="gpt.jpg"),
        caption=resources.messages.gpt,
        reply_markup=main_menu,
        parse_mode="Markdown")

@router.message(Command("talk"))
async def talk_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.talk, filename="talk.jpg"),
        caption=resources.messages.talk,
        reply_markup=main_menu,
        parse_mode="Markdown")

@router.message(Command("quiz"))
async def quiz_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.quiz, filename="quiz.jpg"),
        caption=resources.messages.quiz,
        reply_markup=main_menu,
        parse_mode="Markdown")

@router.message(Command("translate"))
async def translate_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.translate, filename="translate.jpg"),
        caption=resources.messages.translate,
        reply_markup=main_menu,
        parse_mode="Markdown")

@router.message(Command("speech"))
async def speech_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.speech, filename="speech.jpg"),
        caption=resources.messages.speech,
        reply_markup=main_menu,
        parse_mode="Markdown")