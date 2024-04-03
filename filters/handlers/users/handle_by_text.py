from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(Text(equals="salom", ignore_case=True))
async def handle_by_salom(message: types.Message):
    await message.answer("Assalomu alaykum!")


@dp.message_handler(Text(contains="rasvo", ignore_case=True))
async def handle_by_salom(message: types.Message):
    await message.answer("@Javohir_4422 /ban")
