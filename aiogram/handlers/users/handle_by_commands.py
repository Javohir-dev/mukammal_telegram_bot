from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command("til"))
async def handle_change_lang(message: types.Message):
    await message.reply(f"{message.get_command()} o'zgartirildi.")
