from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


# @dp.message_handler(filters.IDFilter(chat_id=923160199))
@dp.message_handler(chat_id=923160199, text="Bobom aytdi.")
async def handle_by_user_id(message: types.Message):
    await message.answer(
        "Seni bobong tanlab ketgan.\n$10 bersang yashirib ketgan humchani joyini aytaman."
    )
