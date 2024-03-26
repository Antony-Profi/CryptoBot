from aiogram import types

from helpers.bunchFormatter import getBunchesFormattedMessages
from models.brokerData import BrokerData


def getHomeInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text="⚙️ Настройки", callback_data="keyboard_settings"),
         types.InlineKeyboardButton(text="💵️ Оплата", callback_data="keyboard_payments")],
        [types.InlineKeyboardButton(text="📋️ Торговля", callback_data="keyboard_trade")],
        [types.InlineKeyboardButton(text="🗒️ Инструкция", url="https://telegra.ph/Rabota-s-Dagger-Funding-Bot-12-05")],
        [types.InlineKeyboardButton(text="📓️️ Информация", callback_data="keyboard_information")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def getSettingsInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text="⚖️ Минимальный спред", callback_data="keyboard_minSpread")],
        [types.InlineKeyboardButton(text="🗒️ Инструкция", url="https://telegra.ph/Rabota-s-Dagger-Funding-Bot-12-05")],
        [types.InlineKeyboardButton(text="🏠 В начало", callback_data="keyboard_toTheBeginning")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def getPaymentsInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text="1 месяц", callback_data="keyboard_oneMonth")],
        [types.InlineKeyboardButton(text="🏠 В начало", callback_data="keyboard_toTheBeginning")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def getTradeInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text="📃 ТОП-20 процентных ставок", callback_data="keyboard_TOP-20-interest-rates")],
        [types.InlineKeyboardButton(text="🗒️ Инструкция", url="https://telegra.ph/Rabota-s-Dagger-Funding-Bot-12-05")],
        [types.InlineKeyboardButton(text="🏠 В начало", callback_data="keyboard_toTheBeginning")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def getInforamtionInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text="🏦 Список бирж", callback_data="keyboard_listOfExchanges")],
        [types.InlineKeyboardButton(text="🆘 Помощь", callback_data="keyboard_help")],
        [types.InlineKeyboardButton(text="🗒️ Инструкция", url="https://telegra.ph/Rabota-s-Dagger-Funding-Bot-12-05")],
        [types.InlineKeyboardButton(text="🏠 В начало", callback_data="keyboard_toTheBeginning")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def getTop20BunchesInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text="◀️Назад", callback_data="keyboard_back"),
         types.InlineKeyboardButton(text="🔄️ Обновить", callback_data="keyboard_update")],
        [types.InlineKeyboardButton(text="🗒️ Инструкция", url="https://telegra.ph/Rabota-s-Dagger-Funding-Bot-12-05")],
        [types.InlineKeyboardButton(text="🏠 В начало", callback_data="keyboard_toTheBeginning")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def getInlineKeyboardMinSpread():
    buttons = [
        [types.InlineKeyboardButton(text="0.1%", callback_data="keyboard_listPercent"),
         types.InlineKeyboardButton(text="0.2%", callback_data="keyboard_listPercent"),
         types.InlineKeyboardButton(text="0.3%", callback_data="keyboard_listPercent")],
        [types.InlineKeyboardButton(text="0.4%", callback_data="keyboard_listPercent"),
         types.InlineKeyboardButton(text="0.5%", callback_data="keyboard_listPercent"),
         types.InlineKeyboardButton(text="0.6%", callback_data="keyboard_listPercent")],
        [types.InlineKeyboardButton(text="0.7%", callback_data="keyboard_listPercent"),
         types.InlineKeyboardButton(text="0.8%", callback_data="keyboard_listPercent"),
         types.InlineKeyboardButton(text="0.9%", callback_data="keyboard_listPercent")],
        [types.InlineKeyboardButton(text="🗒️ Инструкция", url="https://telegra.ph/Rabota-s-Dagger-Funding-Bot-12-05")],
        [types.InlineKeyboardButton(text="🏠 В начало", callback_data="keyboard_toTheBeginning")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def getInlineKeyboardExchangeLists():
    message = """
    
    1. [Binance](https://binance.com/)
    2. [CommEX](https://accounts.commex.com/ru/register?ref=JY6HUB2A)
    3. [Bitget](https://www.bitget.com/ru/referral/register?clacCode=G2C71BX7&from=%2Fru%2Fevents%2Freferral&source=events)
    4. [Bybit](https://www.bybit.com/invite?ref=49MMR8)
    5. [Gateio](https://www.gate.io/signup/AwREAwtW?ref_type=103)
    6. [MEXC](https://www.mexc.com/register?inviteCode=121iiH)
    7. [CoinEx](https://www.coinex.com/register?refer_code=9uqtv)
    8. [Poloniex](https://poloniex.com/signup?c=MBKWMYY7)
    9. [KuCoin](https://www.kucoin.com/r/rf/QBS7BEM5)
    10. [OKX](https://www.okx.com/join/55523872)
    11. [BitMart](https://www.bitmart.com/register-referral/en?r=VkvxNK)
    """
    buttons = [
        [types.InlineKeyboardButton(text="🗒️ Инструкция", url="https://telegra.ph/Rabota-s-Dagger-Funding-Bot-12-05")],
        [types.InlineKeyboardButton(text="🏠 В начало", callback_data="keyboard_toTheBeginning")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def getInlineKeyboardForCallback(callback: types.CallbackQuery):
    callback_data = callback.data.split("_")[1]

    if callback_data == "settings":
        return getSettingsInlineKeyboard()
    elif callback_data == "payments":
        return getPaymentsInlineKeyboard()
    elif callback_data == "trade":
        return getTradeInlineKeyboard()
    elif callback_data == "information":
        return getInforamtionInlineKeyboard()
    elif callback_data == "listOfExchanges":
        return getInlineKeyboardExchangeLists()
    # elif callback_data == "TOP-20-interest-rates":
    #     return getTop20BunchesInlineKeyboard()
    elif callback_data == "minSpread":
        return getInlineKeyboardMinSpread()
    elif callback_data == "toTheBeginning":
        return getHomeInlineKeyboard()


def getResponseMessagesForCallback(callback: types.CallbackQuery, brokerData: BrokerData):
    callback_data = callback.data.split("_")[1]

    if callback_data == "settings":
        return ["Настройки"]
    elif callback_data == "payments":
        return ["Оплата"]
    elif callback_data == "trade":
        return ["Торговля"]
    elif callback_data == "information":
        return ["Информация"]
    elif callback_data == "listOfExchanges":
        return ["Список бирж"]
    # elif callback_data == "TOP-20-interest-rates":
    #     return ["ТОП-20 процентных ставок:"]
    elif callback_data == "minSpread":
        return ["Выберите минимальный спред для получения актуальных связок:"]
    elif callback_data == "toTheBeginning":
        return ["Главное меню"]
    elif callback_data == "TOP-20-interest-rates":
        return getBunchesFormattedMessages(brokerData.bunches)
        
