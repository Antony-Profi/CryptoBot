import asyncio
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
    getHomeInlineKeyboard

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

    mexc   = ccxt.mexc()
    # coinex   = ccxt.coinex()
    # gateio   = ccxt.gateio()
    bitget   = ccxt.bitget()
    # binance   = ccxt.binance()
    # bybit   = ccxt.bybit()
    
    okx   = ccxt.okx()
    bitmart   = ccxt.bitmart()

    

    # poloniex   = ccxt.poloniex() not working
    # kucoin   = ccxt.kucoin() not working

    binance_funding_rates = bybit.fetch_funding_rates()

    mexc_funding_rates = []

    # print(binance_funding_rates.keys())

    print(len(binance_funding_rates))

    # for funding_rate_key in binance_funding_rates.keys():
    #     try: 
    #         mexc_funding_rate = mexc.fetch_funding_rate(funding_rate_key)
    #         print(mexc_funding_rate)
    #         mexc_funding_rates.append(mexc.fetch_funding_rate(funding_rate_key))
    #     except:
    #         continue



    

    # logging.basicConfig(level=logging.INFO)
    # asyncio.run(start())
    # brokerData = BrokerData()
    # startFetching(10, brokerData)
