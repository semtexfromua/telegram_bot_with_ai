# Telegram Bot with AI — my first aiogram project 🌱

> **My very first Python project** and first hands-on with **aiogram**. This is where I started — a simple, honestly rough Telegram bot I built while learning. I keep it public on purpose: it's the "before" in my before-and-after.

A Ukrainian-language Telegram bot packed with small AI toys: GPT chat, AI-generated quizzes, translation, voice messages, and chats with historical characters.

## ✨ Features
- 💬 **GPT chat** (OpenAI GPT-3.5)
- 🧠 **AI-generated quizzes** by topic
- 🌐 **Text translation**
- 🎙 **Voice messages** — offline Ukrainian speech recognition (Vosk) + speech synthesis (gTTS)
- 🎭 **Conversations with historical figures**
- 🎲 **Random AI advice**

## 🛠 Stack
`aiogram 3.x` · `OpenAI API` · `Vosk` · `gTTS` · `Pydantic` · FSM (finite state machine)

For a first project, it already does a fair bit — async bot framework, an AI API, and offline voice. The code, though, is deliberately simple. And that's the point.

## 🌱 What this project taught me
It was my first time with async Python and the Telegram API, so the code is far from perfect — and I left it that way on purpose. Building it taught me, the hard way, the things I do properly now:
- **Async matters** — a few operations here block the event loop; I learned to keep blocking and CPU-bound work off it.
- **Don't repeat yourself** — command and callback handlers duplicate logic; my later projects are built around shared services.
- **Tests & error handling** — this bot has neither; my next ones do.

## 📈 Before → after
This was the starting point. To see where I went next, same person a few projects later:
- 🚀 **[ai-post-bot](https://github.com/semtexfromua/ai-post-bot)** — FastAPI service with proper async, Celery, 235 tests, and clean architecture.
- 🛒 **[django-test-shop](https://github.com/semtexfromua/django-test-shop)** — Django + DRF backend with CI and ~95% test coverage.

The contrast between this repo and those is exactly what I want you to see.

## ▶️ Run it (if you're curious)
```bash
git clone https://github.com/semtexfromua/telegram_bot_with_ai
cd telegram_bot_with_ai
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
# create a .env with TELEGRAM_BOT_TOKEN and OPENAI_API_KEY
python app/main.py
```
The Ukrainian Vosk model is bundled. Commands: `/start`, `/gpt`, `/quiz`, `/talk`, `/translate`, `/speech`, `/random`.

## 📄 License
MIT — see [LICENSE](LICENSE).

---
*A learning project, kept public as the first chapter of my Python journey.*
