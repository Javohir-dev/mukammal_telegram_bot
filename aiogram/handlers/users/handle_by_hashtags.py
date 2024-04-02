from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(filters.HashTag("soqqa"))
@dp.message_handler(hashtags="money")
async def handle_only_hashtags(message: types.Message):
    await message.reply("Prichoskala boshqacha a bugun )")
