import asyncio
import logging

from aiogram import Bot, F, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.keyboard import \
    KeyboardButton, \
    ReplyKeyboardMarkup

from replyKeyboardHelper import getHomeReplyKeyboard
from inlineKeyboardHelper import \
    getInlineKeyboardForCallback, \
    getHomeInlineKeyboard, \
    getSettingsInlineKeyboard


TOKEN = "6769635335:AAHnLfxRzsJh7RnSFkcHgDzxnSDeckC4XaA"
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    keyboard = getHomeReplyKeyboard()
    inlineKeyboard = getHomeInlineKeyboard()

    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await message.answer(
        text="Меню",
        reply_markup=inlineKeyboard,
    )


@dp.message()
async def echo_handler(message: types.Message):
    try:
        inlineKeyboard = getHomeInlineKeyboard()

        markup = ReplyKeyboardMarkup(keyboard=inlineKeyboard, resize_keyboard=True)
        await message.answer(
            text="Настройки",
            reply_markup=markup,
        )
    except TypeError:
        await message.answer("Nice try!")


@dp.callback_query(F.data.startswith("keyboard_"))
async def callbacks_num(callback: types.CallbackQuery):
    inlineKeyboard = getInlineKeyboardForCallback(callback)

    await callback.message.answer(
        text="Ответ",
        reply_markup=inlineKeyboard,
    )


async def start():
    bot = Bot(
        TOKEN,
        parse_mode=ParseMode.HTML,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())
