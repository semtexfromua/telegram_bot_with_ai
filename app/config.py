from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
    )

    TELEGRAM_BOT_TOKEN: str
    OPENAI_API_KEY: str
    MAX_TOKENS: int
    TEMPERATURE: float

    @property
    def main_text(self) -> str:
        with open(Path(__file__).parent.parent / "resources" / "messages" / "main.txt", encoding="UTF-8") as f:
            return f.read()

    @property
    def gpt_text(self) -> str:
        with open(Path(__file__).parent.parent / "resources" / "messages" / "gpt.txt", encoding="UTF-8") as f:
            return f.read()

    @property
    def quiz_text(self) -> str:
        with open(Path(__file__).parent.parent / "resources" / "messages" / "quiz.txt", encoding="UTF-8") as f:
            return f.read()

    @property
    def random_text(self) -> str:
        with open(Path(__file__).parent.parent / "resources" / "messages" / "random.txt", encoding="UTF-8") as f:
            return f.read()

    @property
    def talk_text(self) -> str:
        with open(Path(__file__).parent.parent / "resources" / "messages" / "talk.txt", encoding="UTF-8") as f:
            return f.read()