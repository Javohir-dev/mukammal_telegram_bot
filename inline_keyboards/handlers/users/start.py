import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from keyboards.default.startMenuKeyboard import menuStart
from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    # logging.info(message)
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}!", reply_markup=menuStart
    )
    await message.delete()


@dp.callback_query_handler(Text(equals="main"))
async def call_bot_start(call: types.CallbackQuery):
    # logging.info(call)
    await call.message.answer(
        f"Assalomu alaykum, {call.from_user.full_name}!", reply_markup=menuStart
    )
    await call.message.delete()
