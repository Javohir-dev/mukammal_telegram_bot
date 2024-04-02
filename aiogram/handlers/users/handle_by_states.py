from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(commands="shop")
async def handle_command_shop(message: types.Message, state: FSMContext):
    await state.set_state("shop")
    await message.answer("Siz endi Shop holatidasiz.")


@dp.message_handler(state="shop")
async def handle_state_shop(message: types.Message, state: FSMContext):
    await message.answer("Siz endi oddiy holatdasiz.")
    await state.finish()
