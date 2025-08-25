from io import BytesIO

from gtts import gTTS

from app.utils.voice_format_converter import convert_to_ogg


def text_to_speech(text_to_speak: str, language: str = "uk") -> BytesIO:
    try:
        tts = gTTS(text=text_to_speak, lang=language, slow=False)

        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)

        audio_buffer.seek(0)
        voice_message_ready = convert_to_ogg(audio_buffer)
        return voice_message_ready

    except Exception as e:
        print(f"Помилка під час генерації мовлення: {e}")
        return None
