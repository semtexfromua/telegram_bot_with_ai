from aiogram.fsm.state import State, StatesGroup


class CurrentState(StatesGroup):
    gpt_waiting_question = State()
    quiz_waiting_theme = State()
    quiz_game_in_progress = State()
    talk_person_question = State()
    translate_waiting_text = State()
    speech_waiting_audio = State()
