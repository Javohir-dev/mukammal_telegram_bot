from aiogram import types
from aiogram.dispatcher import filters

from loader import dp, bot


# @dp.message_handler(filters.Command("ban"), filters.AdminFilter())
@dp.message_handler(commands="ban", is_chat_admin=True)
async def hendle_for_only_admin(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id, text="Asalomu alaykoooom bratim, yaxshimisiz?"
    )
