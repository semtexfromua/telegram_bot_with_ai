import soundfile as sf
from io import BytesIO


def convert_to_wav(byte_array: BytesIO) -> BytesIO:
    data, samplerate = sf.read(byte_array)
    wav_buffer = BytesIO()
    # Записуємо аудіодані у WAV форматі
    sf.write(wav_buffer, data, samplerate, format='WAV', subtype='PCM_16')
    wav_buffer.seek(0)
    return wav_buffer

def convert_to_ogg(byte_array: BytesIO) -> BytesIO:
    data, samplerate = sf.read(byte_array)
    ogg_buffer_out = BytesIO()
    # Записуємо ті ж аудіодані, але вже в OGG форматі (Vorbis)
    sf.write(ogg_buffer_out, data, samplerate, format='OGG', subtype='OPUS')
    ogg_buffer_out.seek(0)
    return ogg_buffer_out