from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def create_keyboard(markup: dict) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for callback_data, text in markup.items():
        builder.add(
            InlineKeyboardButton(text=text, callback_data=callback_data),
        )
    builder.adjust(1)
    return builder.as_markup()


async def quiz_keyboard(markup: dict) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for text, callback_data in markup.items():
        builder.add(
            InlineKeyboardButton(text=text, callback_data=callback_data),
        )
    builder.adjust(2)
    return builder.as_markup()
