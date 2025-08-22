from typing import Dict
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
IMAGES_DIR = BASE_DIR / "resources" / "images"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
    )

    TELEGRAM_BOT_TOKEN: str
    OPENAI_API_KEY: str
    DEEPGRAM_API_KEY: str

    TEMPERATURE: float = 0.8
    MAX_TOKENS: int = 300

    openai_model_name: str = "gpt-3.5-turbo"
    openai_model_temperature: float = 0.8



    messages_path: Path = BASE_DIR / "resources" / "messages.yaml"
    prompts_path: Path = BASE_DIR / "resources" / "prompts.yaml"
    menus_path: Path = BASE_DIR / "resources" / "menus.yaml"
    images_dict: Dict[str, Path] = {str(file.name).split(".")[0]: IMAGES_DIR / file for file in IMAGES_DIR.iterdir()}


settings = Settings()