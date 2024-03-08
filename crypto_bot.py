import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher

from aiogram.enums import ParseMode
# from routers import router as main_router


async def main():
    dp = Dispatcher()
    # dp.include_router(main_router)

    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token="6769635335:AAHnLfxRzsJh7RnSFkcHgDzxnSDeckC4XaA",
        parse_mode=ParseMode.HTML,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

