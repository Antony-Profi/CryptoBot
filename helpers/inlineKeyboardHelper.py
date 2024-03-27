from aiogram import types

from constans import KEYBOARD_KEYS, BUTTON_TEXT_BY_KEY
from helpers.bunchFormatter import getBunchesFormattedMessages
from models.brokerData import BrokerData
from models.bunch import Bunch
from models.callbackResponse import CallbackResponse


def getCallbackResponse(callback: types.CallbackQuery, brokerData: BrokerData) -> CallbackResponse: 
    callbackKey = callback.data.split("_")[1]
    
    if callbackKey == KEYBOARD_KEYS.SETTINGS.value:    
        return CallbackResponse(
            BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.SETTINGS],
             getSettingsInlineKeyboard())    
    elif callbackKey == KEYBOARD_KEYS.EXCHANGES_LIST.value:
        return CallbackResponse(
            BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.EXCHANGES_LIST],
             getPaymentsInlineKeyboard())  
    elif callbackKey == KEYBOARD_KEYS.TRADING.value:
        return CallbackResponse(
            BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.TRADING],
             getTradeInlineKeyboard())  
    elif callbackKey == KEYBOARD_KEYS.INFORMATION.value:
        return CallbackResponse(
            BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.INFORMATION],
             getInforamtionInlineKeyboard())  
    elif callbackKey == KEYBOARD_KEYS.EXCHANGES_LIST.value:
        return CallbackResponse(
            BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.EXCHANGES_LIST],
             getInlineKeyboardExchangeLists())  
    elif callbackKey == KEYBOARD_KEYS.TOP_INTEREST_RATES.value:
        return CallbackResponse(
            BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.TOP_INTEREST_RATES],
             getTop20BunchesInlineKeyboard(brokerData.bunches))  
    elif callbackKey == KEYBOARD_KEYS.MIN_SPREAD.value:
        return CallbackResponse(
            BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.MIN_SPREAD],
             getInlineKeyboardMinSpread())  
    elif callbackKey == KEYBOARD_KEYS.GO_HOME.value:
        return CallbackResponse(
            BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.GO_HOME],
             getHomeInlineKeyboard())  

def getHomeInlineKeyboard():
    buttons = [
        [types.InlineKeyboardButton(text=BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.SETTINGS], callback_data=str(KEYBOARD_KEYS.PREFIX.value + KEYBOARD_KEYS.SETTINGS.value)),
         types.InlineKeyboardButton(text=BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.PAYMENTS], callback_data=str(KEYBOARD_KEYS.PREFIX.value + KEYBOARD_KEYS.PAYMENTS.value))],
        [types.InlineKeyboardButton(text=BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.TRADING], callback_data=str(KEYBOARD_KEYS.PREFIX.value + KEYBOARD_KEYS.TRADING.value))],
        [types.InlineKeyboardButton(text=BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.INSTRUCTION], url="https://telegra.ph/Rabota-s-Dagger-Funding-Bot-12-05")],
        [types.InlineKeyboardButton(text=BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.INFORMATION], callback_data=str(KEYBOARD_KEYS.PREFIX.value + KEYBOARD_KEYS.INFORMATION.value))],
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
        [types.InlineKeyboardButton(text="📃 ТОП-20 процентных ставок", callback_data=str(KEYBOARD_KEYS.PREFIX.value + KEYBOARD_KEYS.TOP_INTEREST_RATES.value))],
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


def getTop20BunchesInlineKeyboard(bunches: list[Bunch]):
    buttons = []

    for bunch in bunches:
        buttons.append(
            [types.InlineKeyboardButton(text=bunch.getButtonLabel(), 
                                        callback_data=str(KEYBOARD_KEYS.PREFIX.value + KEYBOARD_KEYS.TOP_INTEREST_RATES.value + ":" + str(bunches.index(bunch))))],
        )

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