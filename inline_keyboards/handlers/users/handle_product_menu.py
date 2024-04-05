from aiogram import types
from aiogram.dispatcher.filters.builtin import Text

from keyboards.inline.productsKeyboards import productMenu, coursesMenu, booksMenu
from loader import dp


@dp.message_handler(Text(contains="Mahsulotlar"))
async def bot_start(message: types.Message):
    await message.answer(f"Mahrulotni tanlang", reply_markup=productMenu)


@dp.callback_query_handler(Text(equals="courses"))
async def handle_get_all_courses(call: types.CallbackQuery):
    await call.message.answer(
        f"Kurslardan birini tanlang",
        reply_markup=coursesMenu,
    )
    await call.answer(cache_time=60)


@dp.callback_query_handler(Text(equals="books"))
async def handle_get_all_courses(call: types.CallbackQuery):
    await call.message.answer(
        f"Kitoblarda birini tanlang",
        reply_markup=booksMenu,
    )
    await call.answer(cache_time=60)
