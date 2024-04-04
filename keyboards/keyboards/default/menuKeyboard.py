from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="Telegram Bot"),
        ],
        [
            KeyboardButton(text="Django"),
            KeyboardButton(text="JavaScript"),
        ],
        [
            KeyboardButton(text="Golang"),
        ],
    ],
    resize_keyboard=True,
)
