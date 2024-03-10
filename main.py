import asyncio
import logging

from aiogram import Bot, F, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message 
from aiogram.utils.keyboard import \
    KeyboardButton, \
    ReplyKeyboardMarkup

from inlineKeyboardHelper import \
    getInlineKeyboardForCallback, \
    getHomeInlineKeyboard


TOKEN = "6769635335:AAHnLfxRzsJh7RnSFkcHgDzxnSDeckC4XaA"
dp = Dispatcher()



def getHomeKeyboard():
    button_settings = KeyboardButton(text="⚙️ Настройки")
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
    inlineKeyboard = getInlineKeyboardForCallback(callback)

    await callback.message.answer(
        text="test",
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
