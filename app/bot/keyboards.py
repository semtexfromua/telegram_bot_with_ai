from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Main Menu')],
        [KeyboardButton(text='One more fact')]],
    resize_keyboard=True,
    input_field_placeholder='Choose something from menu, or write the command')

random_func_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Main Menu', callback_data='start')],
        [InlineKeyboardButton(text='One more fact', callback_data='random')],
    ]
)