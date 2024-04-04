from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


python = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="001-dars"),
            KeyboardButton(text="002-dars"),
            KeyboardButton(text="003-dars"),
            KeyboardButton(text="004-dars"),
        ],
        [
            KeyboardButton(text="⬅️ orqaga"),
            KeyboardButton(text="🏠 Asosiy sahifa"),
        ],
    ],
    resize_keyboard=True,
)
