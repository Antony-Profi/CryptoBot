from aiogram import types
from models.inlineKeyboardResponse import InlineKeyboardResponse


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
        [types.InlineKeyboardButton(text="📃 ТОП-20 процентных ставок", callback_data="keyboard_TOP-20_interest_rates")],
        [types.InlineKeyboardButton(text="🔄️ Связки на Фьючерсах", callback_data="keyboard_Links_onFutures")],
        [types.InlineKeyboardButton(text="🔀 Связки на Фьючерсы-Спот", callback_data="keyboard_Bundles_onFutures-Spot")],
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
    buttons = [
        [types.InlineKeyboardButton(text="🗒️ Инструкция", url="https://telegra.ph/Rabota-s-Dagger-Funding-Bot-12-05")],
        [types.InlineKeyboardButton(text="🏠 В начало", callback_data="keyboard_toTheBeginning")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def getInlineKeyboardForCallback(callback: types.CallbackQuery):
    callback_data = callback.data.split("_")[1]

    inlineKeyboardResponse = InlineKeyboardResponse();

    if callback_data == "settings":
        inlineKeyboardResponse.reponseText = "Настройки";
        inlineKeyboardResponse.inlineKeyboard = getSettingsInlineKeyboard()
    elif callback_data == "payments":
        inlineKeyboardResponse.inlineKeyboard = getPaymentsInlineKeyboard()
    elif callback_data == "trade":
        inlineKeyboardResponse.inlineKeyboard = getTradeInlineKeyboard()
    elif callback_data == "information":
        inlineKeyboardResponse.inlineKeyboard = getInforamtionInlineKeyboard()
    elif callback_data == "listOfExchanges":
        inlineKeyboardResponse.inlineKeyboard = getInlineKeyboardExchangeLists()
    elif callback_data == "minSpread":
        inlineKeyboardResponse.reponseText = "Выберите минимальный спред для получения актуальных связок:";
        inlineKeyboardResponse.inlineKeyboard = getInlineKeyboardMinSpread()
    elif callback_data == "toTheBeginning":
        inlineKeyboardResponse.inlineKeyboard = getHomeInlineKeyboard()

    return inlineKeyboardResponse