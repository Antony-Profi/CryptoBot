import asyncio
import logging

from aiogram import Bot, F, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.keyboard import \
    ReplyKeyboardMarkup

from constans import KEYBOARD_KEYS
from helpers.bunchFormatter import getBunchesFormattedMessages
from services.callBackResponse import getCallbackResponse
from helpers.inlineKeyboardHelper import \
    getInforamtionInlineKeyboard, \
    getTradeInlineKeyboard, \
    getPaymentsInlineKeyboard, \
    getSettingsInlineKeyboard, \
    getHomeInlineKeyboard

from models.brokerData import BrokerData
from services.fetchDataWorker import start as startFetching


TOKEN = "6769635335:AAHnLfxRzsJh7RnSFkcHgDzxnSDeckC4XaA"
dp = Dispatcher()
brokerData = BrokerData()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    inlineKeyboard = getHomeInlineKeyboard()

    await message.answer(
        text="Главное меню",
        reply_markup=inlineKeyboard,
    )


@dp.message(Command("settings"))
async def command_settings(message: Message):
    inlineKeyboard = getSettingsInlineKeyboard()

    await message.answer(
        text="Настройки",
        reply_markup=inlineKeyboard,
    )


@dp.message(Command("payment"))
async def command_payment(message: Message):
    inlineKeyboard = getPaymentsInlineKeyboard()

    await message.answer(
        text="Оплата",
        reply_markup=inlineKeyboard,
    )


@dp.message(Command("deals"))
async def command_trade(message: Message):
    inlineKeyboard = getTradeInlineKeyboard()

    await message.answer(
        text="Торговля",
        reply_markup=inlineKeyboard,
    )


@dp.message(Command("info"))
async def command_info(message: Message):
    inlineKeyboard = getInforamtionInlineKeyboard()

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


@dp.callback_query(F.data.startswith(KEYBOARD_KEYS.PREFIX.value))
async def callbacks_num(callback: types.CallbackQuery):

    callbackResponse = getCallbackResponse(callback, brokerData)

    await callback.message.answer(
        text=callbackResponse.text,
        reply_markup=callbackResponse.replyMarkup,
    )


async def start():
    bot = Bot(
        TOKEN,
        parse_mode=ParseMode.HTML,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    startFetching(60, brokerData)

    print(brokerData.bunches)

    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())
