from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
    )

    BASE_DIR = Path(__file__).parent.parent.parent
    TELEGRAM_BOT_TOKEN: str
    OPENAI_API_KEY: str

    openai_model_name: str = "gpt-3.5-turbo"
    openai_model_temperature: float = 0.8

    images_dir: Path = BASE_DIR / "images"
    messages_path: Path = BASE_DIR / "messeges.yaml"
    prompts_path: Path = BASE_DIR / "prompts.yaml"


settings = Settings()