from aiogram.fsm.state import StatesGroup, State


class CurrentState(StatesGroup):
    # GPT функціональність
    gpt_waiting_question = State()
    # Quiz функціональність
    quiz_waiting_answer = State()
    # Talk функціональність
    talk_person_question = State()
    # Translate функціональність
    translate_waiting_text = State()
    # Speech функціональність
    speech_waiting_audio = State()