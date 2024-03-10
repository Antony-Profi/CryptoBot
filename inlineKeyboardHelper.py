from aiogram import types

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
        [types.InlineKeyboardButton(text="🏦 Список бирж", callback_data="keyboard_listOf_exchanges")],
        [types.InlineKeyboardButton(text="🆘 Помощь", callback_data="keyboard_help")],
        [types.InlineKeyboardButton(text="🗒️ Инструкция", url="https://telegra.ph/Rabota-s-Dagger-Funding-Bot-12-05")],
        [types.InlineKeyboardButton(text="🏠 В начало", callback_data="keyboard_toTheBeginning")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def getInlineKeyboardForCallback(callback: types.CallbackQuery):
    callback_data = callback.data.split("_")[1]

    if callback_data == "settings":
        inlineKeyboard = getSettingsInlineKeyboard()
    elif callback_data == "payments":
        inlineKeyboard = getPaymentsInlineKeyboard()
    elif callback_data == "trade":
        inlineKeyboard = getTradeInlineKeyboard()
    elif callback_data == "information":
        inlineKeyboard = getInforamtionInlineKeyboard()
    elif callback_data == "toTheBeginning":
        inlineKeyboard = getHomeInlineKeyboard()

    return inlineKeyboard