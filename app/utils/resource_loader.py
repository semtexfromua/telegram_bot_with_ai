from types import SimpleNamespace
from yaml import safe_load
from app.settings.config import settings


class Resources:
    def __init__(self):
        self.load_messages()
        self.load_prompts()
        self.load_menus()
        self.load_images()

    def load_messages(self):
        with open(settings.messages_path, encoding="utf-8") as f:
            data = safe_load(f)
        self.messages = SimpleNamespace(**data)


    def load_prompts(self):
        with open(settings.prompts_path, encoding="utf-8") as f:
            data = safe_load(f)

        self.prompts = SimpleNamespace()

        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self.prompts, key, SimpleNamespace(**value))
            else:
                setattr(self.prompts, key, value)

    def load_menus(self):
        with open(settings.menus_path, encoding="utf-8") as f:
            data = safe_load(f)
        self.menus = SimpleNamespace(**data)


    def load_images(self):
        self.images = SimpleNamespace()
        for key, value in settings.images_dict.items():
            with open(value, mode="rb") as f:
                data = f.read()
            setattr(self.images, key, data)


resources = Resources()
