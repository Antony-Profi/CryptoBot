import asyncio
import logging
import sys
from random import randint

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import Router
from aiogram import types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, callback_data
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.utils.keyboard import \
    ReplyKeyboardBuilder, \
    KeyboardButton, \
    ReplyKeyboardMarkup, \
    InlineKeyboardMarkup, \
    InlineKeyboardButton, \
    InlineKeyboardBuilder
from aiogram.utils.markdown import hbold


TOKEN = "TOKEN"
dp = Dispatcher()


# def keyboard():
#     builder = ReplyKeyboardBuilder()
#
#     builder.button(text="💵️ Оплата")
#     builder.button(text="📋️ Торговля")
#     builder.button(text="🗒️ Инструкция")
#     builder.button(text="📓️️ Информация")
#     builder.adjust(2, 1)
#     return builder.as_markup(resize_keyboard=True)


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    button_payment = KeyboardButton(text="💵️ Оплата")
    button_trade = KeyboardButton(text="📋️ Торговля")
    button_instructions = KeyboardButton(text="🗒️ Инструкция")
    button_information = KeyboardButton(text="📓️️ Информация")
    button_row = [button_payment, button_trade]
    button_row_2 = [button_instructions]
    button_row_3 = [button_information]
    markup = ReplyKeyboardMarkup(keyboard=[button_row, button_row_2, button_row_3], resize_keyboard=True)
    await message.answer(
        text=f"Hello, {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
        reply_markup=markup,
    )


# @dp.message(Command('keyboard'))
# async def command_keyboard_handler(message: Message):
#     await message.answer("Нажмите кнопку", reply_markup=keyboard())


@dp.message()
async def echo_handler(message: types.Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def start():
    bot = Bot(
        TOKEN,
        parse_mode=ParseMode.HTML,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())
