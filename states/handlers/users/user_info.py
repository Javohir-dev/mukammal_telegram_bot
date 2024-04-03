from aiogram import types
from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Regexp


from loader import dp
from states.personal_data import PersonalData

# https://ihateregex.io/
EMAIL = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
PHONE_NUMBER = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"


@dp.message_handler(Command("data"))
async def get_user_info(message: types.Message):
    await message.answer("Ism familiyangizni kiriting.")
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def get_user_info(message: types.Message, state: FSMContext):
    fullname = message.text.title()
    await state.update_data(fullname=fullname)
    await message.answer("Telefon raqamingizni kiriting.")
    await PersonalData.next()


# @dp.message_handler()
@dp.message_handler(Regexp(PHONE_NUMBER), state=PersonalData.phone_number)
async def get_user_info(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await message.answer("Emailingizni kiriting.")
    await PersonalData.next()


# @dp.message_handler()
@dp.message_handler(Regexp(EMAIL), state=PersonalData.email)
async def get_user_info(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer(
        "Ma'lumotlaringiz muvofaqiyatli saqlangi, quyida ularni ko'rishingiz mumkin."
    )

    data = await state.get_data()
    get_fullname = data.get("fullname")
    get_phone_number = data.get("phone_number")
    get_email = data.get("email")

    msg = f"<b>Ism familiya:</b> {get_fullname}\n"
    msg += f"<b>Telefon raqam:</b> {get_phone_number}\n"
    msg += f"<b>Email:</b> {get_email}"
    await message.answer(msg)
    await state.finish()
    # await state.reset_state(with_data=True)
