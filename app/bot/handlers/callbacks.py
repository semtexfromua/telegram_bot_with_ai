from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, BufferedInputFile

from app.bot.keyboards import create_keyboard
from app.utils.resource_loader import resources
from app.bot.fsm import CurrentState

from app.utils.gpt import AsyncOpenAiClient

callback_router = Router()
client = AsyncOpenAiClient()

@callback_router.callback_query(F.data == "start")
async def start_cmd(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await callback.answer("")

    await callback.message.answer_photo(
        photo=BufferedInputFile(resources.images.main, filename="main.jpg"),
        caption=resources.messages.main,
        reply_markup=await create_keyboard(markup=resources.menus.main))


@callback_router.callback_query(F.data =="help")
async def help_cmd(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer_photo(
        photo=BufferedInputFile(resources.images.main, filename="main.jpg"),
        caption=resources.messages.main,
        reply_markup=await create_keyboard(markup=resources.menus.main))

@callback_router.callback_query(F.data =="random")
async def random_cmd(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer_photo(
        photo=BufferedInputFile(resources.images.random, filename="random.jpg"),
        caption=resources.messages.random + "\n" + await client.send_message(resources.prompts.random),
        reply_markup=await create_keyboard(markup=resources.menus.random))

@callback_router.callback_query(F.data =="gpt")
async def gpt_cmd(callback: CallbackQuery, state: FSMContext):
    await state.set_state(CurrentState.gpt_waiting_question)
    await callback.answer("")
    await callback.message.answer_photo(
        photo=BufferedInputFile(resources.images.gpt, filename="gpt.jpg"),
        caption=resources.messages.gpt,
        reply_markup=await create_keyboard(markup=resources.menus.gpt))

@callback_router.callback_query(F.data =="talk")
async def talk_cmd(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer_photo(
        photo=BufferedInputFile(resources.images.talk, filename="talk.jpg"),
        caption=resources.messages.talk,
        reply_markup=await create_keyboard(markup=resources.menus.talk))

@callback_router.callback_query(F.data =="quiz")
async def quiz_cmd(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer_photo(
        photo=BufferedInputFile(resources.images.quiz, filename="quiz.jpg"),
        caption=resources.messages.quiz,
        reply_markup=await create_keyboard(markup=resources.menus.quiz))

@callback_router.callback_query(F.data =="translate")
async def translate_cmd(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer_photo(
        photo=BufferedInputFile(resources.images.translate, filename="translate.jpg"),
        caption=resources.messages.translate,
        reply_markup=await create_keyboard(markup=resources.menus.translate))

@callback_router.callback_query(F.data =="speech")
async def speech_cmd(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer_photo(
        photo=BufferedInputFile(resources.images.speech, filename="speech.jpg"),
        caption=resources.messages.speech,
        reply_markup=await create_keyboard(markup=resources.menus.speech))