from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


# @dp.message_handler(content_types=types.ContentTypes.PHOTO)
@dp.message_handler(content_types="photo")
@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def handle_only_photo(message: types.Message):
    await message.reply("Uzr! Men hozircha faqat text bilan ishlayman.")
