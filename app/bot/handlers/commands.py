from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BufferedInputFile

from app.bot.keyboards import create_keyboard
from app.utils.resource_loader import resources
from app.bot.fsm import CurrentState

from app.utils.gpt import AsyncOpenAiClient


command_router = Router()
client = AsyncOpenAiClient()

@command_router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext):
    await state.set_state(None)
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.main, filename="main.jpg"),
        caption=resources.messages.main,
        reply_markup=await create_keyboard(markup=resources.menus.main))

@command_router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.main, filename="main.jpg"),
        caption=resources.messages.main,
        reply_markup=await create_keyboard(markup=resources.menus.main))

@command_router.message(Command("random"))
async def random_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.random, filename="random.jpg"),
        caption=resources.messages.random + "\n" + await client.send_message(resources.prompts.random),
        reply_markup=await create_keyboard(markup=resources.menus.random))

@command_router.message(Command("gpt"))
async def gpt_cmd(message: Message, state: FSMContext):
    await state.set_state(CurrentState.gpt_waiting_question)
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.gpt, filename="gpt.jpg"),
        caption=f"{resources.messages.gpt}",
        reply_markup=await create_keyboard(markup=resources.menus.gpt))

@command_router.message(Command("talk"))
async def talk_cmd(message: Message, state: FSMContext):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.talk, filename="talk.jpg"),
        caption=resources.messages.talk,
        reply_markup=await create_keyboard(markup=resources.menus.talk))

@command_router.message(Command("quiz"))
async def quiz_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.quiz, filename="quiz.jpg"),
        caption=resources.messages.quiz,
        reply_markup=await create_keyboard(markup=resources.menus.quiz))

@command_router.message(Command("translate"))
async def translate_cmd(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.translate, filename="translate.jpg"),
        caption=resources.messages.translate,
        reply_markup=await create_keyboard(markup=resources.menus.translate))

@command_router.message(Command("speech"))
async def speech_cmd(message: Message, state: FSMContext):
    await state.set_state(CurrentState.speech_waiting_audio)
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.speech, filename="speech.jpg"),
        caption=resources.messages.speech,
        reply_markup=await create_keyboard(markup=resources.menus.speech))