import json
import wave
from io import BytesIO

from vosk import Model, KaldiRecognizer

from app.utils.voice_format_converter import convert_to_wav

_vosk_model = None

def _get_vosk_model() -> Model:
    global _vosk_model
    if _vosk_model is None:
        # Ініціалізація моделі лише при першому зверненні
        from app.settings.config import Settings
        _vosk_model = Model(Settings().vosk_model_path)
    return _vosk_model



def speech_to_text(bytes_array: BytesIO) -> str:
    wav_data = convert_to_wav(bytes_array)
    model = _get_vosk_model()
    with wave.open(wav_data, "rb") as wf:
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            rec.AcceptWaveform(data)

        result_json = rec.FinalResult()

    result_dict = json.loads(result_json)
    return result_dict.get('text', '')