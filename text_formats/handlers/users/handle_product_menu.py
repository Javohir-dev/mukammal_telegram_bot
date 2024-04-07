from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import Text

from keyboards.inline.productsKeyboards import productMenu, coursesMenu, booksMenu
from keyboards.inline.callback_data import courses_callback, books_callback
from loader import dp, bot


@dp.message_handler(Text(contains="Mahsulotlar"))
async def bot_start(message: types.Message):
    await message.answer("Mahrulotni tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer("Mahrulotni tanlang", reply_markup=productMenu)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)


@dp.callback_query_handler(Text(equals="courses"))
async def handle_get_all_courses(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Kurslardan birini tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(Text(equals="books"))
async def handle_get_all_courses(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        f"Kitoblarda birini tanlang",
        reply_markup=booksMenu,
    )
    await call.answer(cache_time=60)


@dp.callback_query_handler(Text(equals="cancel"))
async def handle_get_all_courses(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Mahrulotni tanlang", reply_markup=productMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(courses_callback.filter(item_name="python"))
async def handle_buy_courses(call: types.CallbackQuery, callback_data: dict):
    await call.message.answer(f"Siz 🐍 Python BackEnd kursini tanladingiz.")

    await call.answer(cache_time=60)


@dp.callback_query_handler(books_callback.filter(item_name="python_book"))
async def handle_buy_courses(call: types.CallbackQuery, callback_data: dict):
    await call.message.answer("Buyurtmangiz qabul qilindi ✅")

    await call.answer(cache_time=60)
