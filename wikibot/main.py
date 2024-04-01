import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

from wiki import get_wikipedia_info, clean_html

API_TOKEN = "7183361110:AAElyimVjnSif85KdsHdlS9J4NdYoVdotck"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang("uz")


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        result = wikipedia.summary(message.text)
        result2 = wikipedia.page(message.text)
        await message.reply(
            f"<b>Topilgan ma'lumotlar:</b>\n\n{result}\n\n<a href='{result2.url}'> more...</a>",
            parse_mode="html",
        )
    except:
        await message.reply(
            f"<b>{message.text} Haqida ma'lumot topilmadi.</b>", parse_mode="html"
        )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
