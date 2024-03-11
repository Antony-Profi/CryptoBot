import asyncio
import logging

from aiogram import Bot, F, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.keyboard import \
    KeyboardButton, \
    ReplyKeyboardMarkup

from helpers.replyKeyboardHelper import getHomeReplyKeyboard
from helpers.inlineKeyboardHelper import \
    getInlineKeyboardForCallback, \
    getHomeInlineKeyboard, \
    getSettingsInlineKeyboard

from binance.client import Client


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
    inlineKeyboardResponse = getInlineKeyboardForCallback(callback)

    await callback.message.answer(
        text=inlineKeyboardResponse.reponseText,
        reply_markup=inlineKeyboardResponse.inlineKeyboard,
    )


async def start():
    bot = Bot(
        TOKEN,
        parse_mode=ParseMode.HTML,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    # asyncio.run(start())
    
    client = Client();
    info = client.futures_mark_price()

    print(info)
