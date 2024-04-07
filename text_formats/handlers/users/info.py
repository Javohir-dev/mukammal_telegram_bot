from aiogram import types

from loader import dp


@dp.message_handler(commands="info")
async def handle_get_info(message: types.Message):
    text: str = (
        f"<b>Assalomu alaykum <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a></b> \n\n"
    )
    text += "Buyruqlar: \n"
    text += "/start - Botni ishga tushirish\n"
    text += "/help - Yordam"

    await message.answer(text)
