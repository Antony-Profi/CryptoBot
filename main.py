import asyncio
import datetime
import logging

from aiogram import Bot, F, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.keyboard import \
    ReplyKeyboardMarkup

from helpers.replyKeyboardHelper import getHomeReplyKeyboard
from helpers.inlineKeyboardHelper import \
    getInlineKeyboardForCallback, \
    getHomeInlineKeyboard, \
    getSettingsInlineKeyboard, \
    getPaymentsInlineKeyboard, \
    getTradeInlineKeyboard, \
    getInforamtionInlineKeyboard

from binance.client import Client

import ccxt

from models.brokerData import BrokerData
from services.fetchDataWorker import start as startFetching


TOKEN = "6769635335:AAHnLfxRzsJh7RnSFkcHgDzxnSDeckC4XaA"
dp = Dispatcher()
global brokerData


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    keyboard = getHomeReplyKeyboard()
    inlineKeyboard = getHomeInlineKeyboard()

    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await message.answer(
        text="Главное меню",
        reply_markup=inlineKeyboard,
    )


@dp.message(Command("settings"))
async def command_settings(message: Message):
    keyboard = getHomeReplyKeyboard()
    inlineKeyboard = getSettingsInlineKeyboard()

    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await message.answer(
        text="Настройки",
        reply_markup=inlineKeyboard,
    )


@dp.message(Command("payment"))
async def command_payment(message: Message):
    keyboard = getHomeReplyKeyboard()
    inlineKeyboard = getPaymentsInlineKeyboard()

    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await message.answer(
        text="Оплата",
        reply_markup=inlineKeyboard,
    )


@dp.message(Command("deals"))
async def command_trade(message: Message):
    keyboard = getHomeReplyKeyboard()
    inlineKeyboard = getTradeInlineKeyboard()

    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await message.answer(
        text="Торговля",
        reply_markup=inlineKeyboard,
    )


@dp.message(Command("info"))
async def command_info(message: Message):
    keyboard = getHomeReplyKeyboard()
    inlineKeyboard = getInforamtionInlineKeyboard()

    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await message.answer(
        text="Информация",
        reply_markup=inlineKeyboard,
    )


@dp.message()
async def echo_handler(message: types.Message):
    try:
        inlineKeyboard = getHomeInlineKeyboard()

        markup = ReplyKeyboardMarkup(keyboard=inlineKeyboard, resize_keyboard=True)
        await message.answer(
            text="test",
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
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())

    brokerData = BrokerData()
    startFetching(120, brokerData)
