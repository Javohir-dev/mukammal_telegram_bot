from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


# https://t.me/ch_aiogrambot?start=kunuz
# ?startdan keyingi kunuz bo'lgan linkni bosgan foydalanuvchilarga quyidagi handler ishlaydi.
@dp.message_handler(CommandStart(deep_link="kunuz"))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Assalomu alaykum, {message.from_user.full_name}.\n"
    text += f"{args}dagi reklamani ko'rib kelganingizdan hursandmiz"
    await message.answer(text)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    # await message.answer(message.from_user)
