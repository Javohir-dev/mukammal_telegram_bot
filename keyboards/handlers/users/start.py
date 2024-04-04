from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startKeyboard import start
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!")
    info: str = "Contact ma'lumotlaringiz va "
    info += "Yashash manzilingizni yuboring."
    await message.answer(info, reply_markup=start)
