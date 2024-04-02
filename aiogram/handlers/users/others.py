from aiogram import types
from aiogram.dispatcher import filters

from loader import dp, bot


@dp.message_handler(is_reply=True, commands="user_id")
async def hendle_reply(message: types.Message):
    await message.answer(message.reply_to_message.from_user.id)
