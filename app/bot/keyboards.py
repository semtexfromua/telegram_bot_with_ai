from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def create_keyboard(markup: dict) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for callback_data, text in markup.items():
        builder.add(
            InlineKeyboardButton(
                text=text,
                callback_data=callback_data
            ),
        )
    builder.adjust(1)
    return builder.as_markup()

