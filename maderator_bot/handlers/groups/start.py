from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.filter_group import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}!\n\nGuruhga hush kelibsiz."
    )
    await message.delete()
