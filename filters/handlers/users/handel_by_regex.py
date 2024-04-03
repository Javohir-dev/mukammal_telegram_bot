from aiogram import types
from aiogram.dispatcher.filters import Text, Regexp

from loader import dp

# https://ihateregex.io/
URL = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
EMAIL = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
PHONE_NUMBER = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
COMMANDS_EMAIL_REGEX = r"/email:" + EMAIL


@dp.message_handler(Regexp(URL))
async def handle_only_url(message: types.Message):
    await message.reply("url tashlash taqiqlangan!")


@dp.message_handler(regexp_commands=[COMMANDS_EMAIL_REGEX])
async def handle_only_url(message: types.Message):
    await message.reply("Email (2) raqam qabul qilindi")


@dp.message_handler(Regexp(EMAIL))
async def handle_only_url(message: types.Message):
    await message.reply("Email qabul qilindi")


@dp.message_handler(Regexp(PHONE_NUMBER))
async def handle_only_url(message: types.Message):
    await message.reply("Telefon raqam qabul qilindi")
