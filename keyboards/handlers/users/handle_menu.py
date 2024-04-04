from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.pythonKeyboard import python

from loader import dp


@dp.message_handler(Command("menu"))
async def handle_menu(message: Message):
    await message.answer("Kurslardan birini tanlang:", reply_markup=menu)


@dp.message_handler(Text("Python"))
async def handle_menu(message: Message):
    await message.answer(
        "Kurs uchun havola: https://praktikum.mohirdev.uz/dashboard/practicums/645264af69d972027cd02d52",
        reply_markup=python,
    )


@dp.message_handler(Text("Telegram Bot"))
async def handle_menu(message: Message):
    await message.answer(
        "Kurs uchun havola: https://praktikum.mohirdev.uz/dashboard/practicums/645264c869d972027cd033c3",
        reply_markup=menu,
    )


@dp.message_handler(Text("Django"))
async def handle_menu(message: Message):
    await message.answer(
        "Kurs uchun havola: https://praktikum.mohirdev.uz/dashboard/practicums/645264bf69d972027cd03180",
        reply_markup=menu,
    )


@dp.message_handler(Text("JavaScript"))
async def handle_menu(message: Message):
    await message.answer(
        "Kurs uchun havola: https://praktikum.mohirdev.uz/dashboard/practicums/645264b169d972027cd02dce/free",
        reply_markup=menu,
    )


@dp.message_handler(Text("Golang"))
async def handle_menu(message: Message):
    await message.answer(
        "Kurs uchun havola: https://praktikum.mohirdev.uz/dashboard/practicums/645264ca69d972027cd03491/free",
        reply_markup=menu,
    )
