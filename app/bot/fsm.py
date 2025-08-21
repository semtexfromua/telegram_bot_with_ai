from aiogram.fsm.state import StatesGroup, State


class CurrentState(StatesGroup):
    # GPT функціональність
    gpt_waiting_question = State()
    gpt_processing_context = State()

    # Quiz функціональність
    quiz_waiting_answer = State()
    quiz_processing_context = State()

    # Talk функціональність
    talk_waiting_question = State()
    talk_processing_context = State()

    # Translate функціональність
    translate_waiting_text = State()
    translate_waiting_language_context = State()

    # Speech функціональність
    speech_waiting_audio = State()
    speech_processing_context = State()