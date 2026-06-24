# Telegram Bot with AI

A Ukrainian-language Telegram bot with several AI features: GPT chat, AI-generated quizzes, text translation, voice messages, conversations with historical characters, and random advice.

## Features

- GPT chat (OpenAI GPT-3.5)
- AI-generated quizzes by topic
- Text translation
- Voice messages — offline Ukrainian speech recognition (Vosk) and synthesis (gTTS)
- Conversations with historical figures
- Random AI advice

## Stack

aiogram 3.x, OpenAI API, Vosk, gTTS, Pydantic, FSM (finite state machine).

## Run

```bash
git clone https://github.com/semtexfromua/telegram_bot_with_ai
cd telegram_bot_with_ai
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
# create a .env with TELEGRAM_BOT_TOKEN and OPENAI_API_KEY
python app/main.py
```

The Ukrainian Vosk model is bundled.

Commands: `/start`, `/gpt`, `/quiz`, `/talk`, `/translate`, `/speech`, `/random`.

## License

MIT — see [LICENSE](LICENSE).
