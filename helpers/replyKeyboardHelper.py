from aiogram.utils.keyboard import KeyboardButton


def getHomeReplyKeyboard():
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


def getSettingsReplyKeyboard():
    button_settings = KeyboardButton(text="⚖️ Минимальный спред")
    button_instructions = KeyboardButton(text="🗒️ Инструкция")
    button_information = KeyboardButton(text="🏠 В начало")
    button_row = [button_settings]
    button_row_2 = [button_instructions]
    button_row_3 = [button_information]
    return [button_row, button_row_2, button_row_3]


def getPaymentsReplyKeyboard():
    button_payment = KeyboardButton(text="1 месяц")
    button_trade = KeyboardButton(text="В начало")
    button_row = [button_payment]
    button_row_2 = [button_trade]
    return [button_row, button_row_2]


def getTradeReplyKeyboard():
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
