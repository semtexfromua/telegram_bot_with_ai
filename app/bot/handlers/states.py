from io import BytesIO

from aiogram import Bot, F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import BufferedInputFile, CallbackQuery, Message

from app.bot.fsm import CurrentState
from app.bot.keyboards import create_keyboard, quiz_keyboard
from app.utils.gpt import AsyncOpenAiClient
from app.utils.quiz import get_question
from app.utils.resource_loader import resources
from app.utils.speech_to_text import speech_to_text as stt
from app.utils.text_to_speech import text_to_speech as tts

states_router = Router()
client = AsyncOpenAiClient()


@states_router.message(CurrentState.gpt_waiting_question)
async def gpt_message_capture(message: Message, state: FSMContext):
    user_id, user_message = message.from_user.id, message.text
    answer = await client.send_message(user_message, resources.prompts.gpt)
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.gpt, filename="gpt.jpg"),
        caption=resources.messages.gpt + "\n" + answer,
        reply_markup=await create_keyboard(markup=resources.menus.gpt),
    )


@states_router.message(CurrentState.talk_person_question)
async def talk_message_caputre(message: Message, state: FSMContext):
    user_id, user_message = message.from_user.id, message.text
    data = await state.get_data()
    persona = data.get("persona")
    answer = await client.send_message(user_message, resources.prompts.talk[persona])
    await message.answer_photo(
        photo=BufferedInputFile(
            getattr(resources.images, persona), filename=f"{persona}.jpg"
        ),
        caption=answer,
        reply_markup=await create_keyboard(markup=resources.menus.talk_util),
    )


@states_router.message(CurrentState.translate_waiting_text)
async def talk_message_caputre(message: Message, state: FSMContext):
    user_id, user_message = message.from_user.id, message.text
    data = await state.get_data()
    language = data.get("language")
    answer = await client.send_message(
        user_message, f"{resources.prompts.translate} Translate to {language}"
    )
    await message.answer_photo(
        photo=BufferedInputFile(resources.images.translate, filename=f"translate.jpg"),
        caption=answer,
        reply_markup=await create_keyboard(markup=resources.menus.talk_util),
    )


@states_router.message(CurrentState.speech_waiting_audio, F.voice)
async def speech_voice_capture(
        message: types.Message,
        state: FSMContext,
        bot: Bot):
    await message.answer(
        "Отримав ваше повідомляння, зачекайте будь ласка, відповідь займе декілька секунд..."
    )

    try:
        ogg_buffer_in = BytesIO()
        await bot.download(message.voice, destination=ogg_buffer_in)
        ogg_buffer_in.seek(0)
    except Exception as e:
        await message.reply(f"Виникла помилка: {e}")

    user_message_text = stt(ogg_buffer_in)
    answer = await client.send_message(user_message_text, resources.prompts.speech)
    voice_message = tts(answer)
    await message.answer_voice(
        voice=BufferedInputFile(file=voice_message.read(), filename="answer.ogg"),
        reply_markup=resources.menus.speech,
    )


@states_router.callback_query(
    CurrentState.quiz_waiting_theme, F.data.startswith("quiz_")
)
async def handle_quiz_clb(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    theme = callback.data
    quiz_question = await get_question(theme)
    await state.update_data(quiz_question=quiz_question)
    await state.set_state(CurrentState.quiz_game_in_progress)
    await callback.message.answer_photo(
        photo=BufferedInputFile(resources.images.quiz, filename=f"quiz.jpg"),
        caption=quiz_question["question"],
        reply_markup=await quiz_keyboard(markup=quiz_question["variants"]),
    )


@states_router.callback_query(
    CurrentState.quiz_game_in_progress, F.data.in_(["win", "lose"])
)
async def handle_quiz_clb(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    quiz_question = data.get("quiz_question")
    score = data.get("score", 0)
    if callback.data == "win":
        score += 1
        await state.update_data(score=score)
        caption = f"✅ Вітаю! Вірна відповідь. Ваш рахунок {score}"
    else:
        correct = quiz_question["correct"]
        caption = f"❌ На жаль ні! Правильна відповідь: {correct}"
    await state.set_state(CurrentState.quiz_waiting_theme)
    await callback.message.answer_photo(
        photo=BufferedInputFile(resources.images.quiz, filename=f"quiz.jpg"),
        caption=caption,
        reply_markup=await create_keyboard(resources.menus.quiz),
    )
