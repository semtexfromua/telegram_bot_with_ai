from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BufferedInputFile

from app.bot.keyboards import create_keyboard
from app.utils.resource_loader import resources
from app.bot.fsm import CurrentState

from app.utils.gpt import AsyncOpenAiClient


states_router = Router()
client = AsyncOpenAiClient()

@states_router.message(CurrentState.gpt_waiting_question)
async def gpt_message_capture(message: Message, state: FSMContext):
    user_id, user_message = message.from_user.id, message.text
    answer = await client.send_message(user_message, resources.prompts.gpt)
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.gpt, filename="gpt.jpg"),
        caption=resources.messages.gpt + "\n" + answer,
        reply_markup=await create_keyboard(markup=resources.menus.gpt))
