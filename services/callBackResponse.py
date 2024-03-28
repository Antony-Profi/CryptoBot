from models.callbackResponse import CallbackResponse
from models.brokerData import BrokerData
from helpers.bunchFormatter import getBunchesFormattedMessages
from aiogram import types
from constans import KEYBOARD_KEYS, BUTTON_TEXT_BY_KEY
from models.bunch import Bunch
from helpers.inlineKeyboardHelper import \
    getSettingsInlineKeyboard, \
    getPaymentsInlineKeyboard, \
    getTradeInlineKeyboard, \
    getInforamtionInlineKeyboard, \
    getInlineKeyboardExchangeLists, \
    getTop20BunchesInlineKeyboard, \
    getInlineKeyboardMinSpread, \
    getHomeInlineKeyboard


def getCallbackResponse(callback: types.CallbackQuery, brokerData: BrokerData) -> CallbackResponse:
    callbackKey = callback.data.split("_")[1]

    if callbackKey == KEYBOARD_KEYS.SETTINGS.value:
        return CallbackResponse(
            BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.SETTINGS],
            getSettingsInlineKeyboard())
    elif callbackKey == KEYBOARD_KEYS.PAYMENTS.value:
        return CallbackResponse(
            BUTTON_TEXT_BY_KEY[KEYBOARD_KEYS.PAYMENTS],
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
