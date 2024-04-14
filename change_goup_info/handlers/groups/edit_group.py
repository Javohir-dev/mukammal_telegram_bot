import io
from aiogram import types
from aiogram.dispatcher.filters import Command
from filters.filter_group import IsGroup
from filters.filter_admin import AdminFilter
from loader import dp, bot


# Handler to set a new photo for the chat
@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    if not source_message or not source_message.photo:
        await message.reply(
            "Please reply to a message with a photo to set a new chat photo."
        )
        return

    photo = source_message.photo[-1]
    photo = await photo.download(destination_file=io.BytesIO())
    input_file = types.InputFile(photo)
    await message.chat.set_photo(photo=input_file)


# Handler to set a new title for the chat
@dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    if not source_message or not source_message.text:
        await message.reply("Please reply to a message with the new title text.")
        return

    title = source_message.text
    await bot.set_chat_title(message.chat.id, title=title)


# Handler to set a new description for the chat
@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    if not source_message or not source_message.text:
        await message.reply("Please reply to a message with the new description text.")
        return

    description = source_message.text
    await message.chat.set_description(description=description)
