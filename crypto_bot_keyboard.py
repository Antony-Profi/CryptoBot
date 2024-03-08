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


TOKEN = "6769635335:AAHnLfxRzsJh7RnSFkcHgDzxnSDeckC4XaA"
dp = Dispatcher()

def getSettingsInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text="Минимальный спред", callback_data="keyboard_minSpread")],
        [types.InlineKeyboardButton(text="🗒️ Инструкция", callback_data="keyboard_instruction")]
        [types.InlineKeyboardButton(text="В начало", callback_data="keyboard_toTheBeginning")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)

def getPaymentsInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text="1 месяц", callback_data="test")],
        [types.InlineKeyboardButton(text="В начало", callback_data="test")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)

def getTradeInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text="ТОП-20 процентных ставок", callback_data="test")],
        [types.InlineKeyboardButton(text="Ставки на Фьючерсах", callback_data="test")]
        [types.InlineKeyboardButton(text="Ставки на Фьючерсы-Спот", callback_data="test")]
        [types.InlineKeyboardButton(text="Инструкция", callback_data="test")]
        [types.InlineKeyboardButton(text="В начало", callback_data="test")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)

def getHomeInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text="⚙️Настройки", callback_data="⚙️Настройки")],
        [types.InlineKeyboardButton(text="💵️ Оплата", callback_data="test")],
        [types.InlineKeyboardButton(text="📋️ Торговля", callback_data="test")],
        [types.InlineKeyboardButton(text="🗒️ Инструкция", callback_data="test")],
        [types.InlineKeyboardButton(text="📓️️ Информация", callback_data="test")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)

def getSettingsKeyboard():
    button_settings = KeyboardButton(text="Минимальный спред")
    button_instructions = KeyboardButton(text="🗒️ Инструкция")
    button_information = KeyboardButton(text="В начало")
    button_row = [button_settings]
    button_row_2 = [button_instructions]
    button_row_3 = [button_information]
    return [button_row, button_row_2, button_row_3]


def getPaymentsKeyboard():
    button_payment = KeyboardButton(text="1 месяц")
    button_trade = KeyboardButton(text="В начало")
    button_row = [button_payment]
    button_row_2 = [button_trade]
    return [button_row, button_row_2]


def getTradeKeyboard():
    button_payment = KeyboardButton(text="ТОП-20 процентных ставок")
    button_trade = KeyboardButton(text="Ставки на Фьючерсах")
    button_trade_2 = KeyboardButton(text="Ставки на Фьючерсы-Спот")
    button_trade_3 = KeyboardButton(text="Инструкция")
    button_trade_4 = KeyboardButton(text="В начало")
    button_row = [button_payment]
    button_row_2 = [button_trade]
    button_row_3 = [button_trade_2]
    button_row_4 = [button_trade_3]
    button_row_5 = [button_trade_4]
    return [button_row, button_row_2, button_row_3, button_row_4, button_row_5]


def getHomeKeyboard():
    button_settings = KeyboardButton(text="⚙️Настройки")
    button_payment = KeyboardButton(text="💵️ Оплата")
    button_trade = KeyboardButton(text="📋️ Торговля")
    button_instructions = KeyboardButton(text="🗒️ Инструкция")
    button_information = KeyboardButton(text="📓️️ Информация")
    button_row = [button_settings, button_payment]
    button_row_2 = [button_trade]
    button_row_3 = [button_instructions]
    button_row_4 = [button_information]
    return [button_row, button_row_2, button_row_3, button_row_4]


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    keyboard = getHomeKeyboard()
    inlineKeyboard = getHomeInlineKeyboard()

    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await message.answer(
        text="test",
        reply_markup=inlineKeyboard,
    )


@dp.message()
async def echo_handler(message: types.Message):
    try:
        if message.text == "⚙️Настройки":
            keyboard = getSettingsKeyboard()
            inlineKeyboard = getSettingsInlineKeyboard()
        elif message.text == "💵️ Оплата":
            inlineKeyboard = getPaymentsInlineKeyboard()
            keyboard = getPaymentsKeyboard()
        elif message.text == "📋️ Торговля":
            inlineKeyboard = getTradeInlineKeyboard()
            keyboard = getTradeKeyboard()
        elif message.text == "В начало":
            inlineKeyboard = getHomeInlineKeyboard()
            keyboard = getHomeKeyboard()

        markup = ReplyKeyboardMarkup(keyboard=inlineKeyboard, resize_keyboard=True)
        await message.answer(
            reply_markup=markup,
        )
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
