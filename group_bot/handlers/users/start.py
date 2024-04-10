from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.filter_private_chat import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!")
    await message.delete()
