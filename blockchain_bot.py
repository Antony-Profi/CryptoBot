from aiogram import Bot, Dispatcher, types
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()

token = os.getenv("TOKEN")

bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher(bot)


async def start_bot(message: types.Message):
    await bot.send_message("Бот успешно запущен!")


# dp.startup.register(start_bot)


async def start():
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
