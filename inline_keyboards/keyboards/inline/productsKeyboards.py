from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import courses_callback, books_callback


productMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="📚 Kitoblar", callback_data="books"),
        ],
        [
            InlineKeyboardButton(text="🔗 Mohirdev", url="https://new.mohirdev.uz"),
        ],
        [
            InlineKeyboardButton(
                text="🔍 Qidiruv",
                switch_inline_query_current_chat="",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📤 Ulashish",
                switch_inline_query="Zo'r bot ekan 👍",
            ),
        ],
    ]
)

coursesMenu = InlineKeyboardMarkup(row_width=2)
python = InlineKeyboardButton(
    text="🐍 Python BackEnd",
    callback_data=courses_callback.new(item_name="python"),
)
# python = InlineKeyboardButton(text="🐍 Python", callback_data="courses:python")
coursesMenu.add(python)
django = InlineKeyboardButton(text="🗄 Django", callback_data="courses:django")
coursesMenu.add(django)
golang = InlineKeyboardButton(text="💎 Golang", callback_data="courses:golang")
coursesMenu.add(golang)
back_button = InlineKeyboardButton(text="🔙 Orqaga", callback_data="cancel")
main_button = InlineKeyboardButton(text="Asosiy menu 🏠", callback_data="main")
coursesMenu.add(back_button, main_button)

books = {
    "Python dasturlash asoslari": "python_book",
    "Atom odatlar": "atom_odatlar_book",
    "Iboti Islomiya": "ibodati_islomiya_book",
    "Diqqat": "diqqat_book",
}

booksMenu = InlineKeyboardMarkup(row_width=2)
for key, value in books.items():
    booksMenu.add(
        InlineKeyboardButton(
            text=key,
            callback_data=books_callback.new(item_name=value),
        )
    )
booksMenu.add(back_button, main_button)
