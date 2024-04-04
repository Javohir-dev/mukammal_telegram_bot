from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.pythonKeyboard import python

from loader import dp


@dp.message_handler(Text("⬅️ orqaga"))
async def handle_menu(message: Message):
    await message.answer("⬅️ orqaga qaytarildi.", reply_markup=menu)


@dp.message_handler(Text("🏠 Asosiy sahifa"))
async def handle_menu(message: Message):
    await message.answer("🏠 Asosiy sahifa", reply_markup=ReplyKeyboardRemove())
