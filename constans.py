from enum import Enum


BINANCE = "🏦 BINANCE"
COMEX = "🏦 COMEX"
BITGET = "🏦 BITGET"
BYBIT = "🏦 BYBIT"
GATEIO = "🏦 GATEIO"
MEXC = "🏦 MEXC"
COINEX = "🏦 COINEX"
OKX = "🏦 OKX"
BITMART = "🏦 BITMART"

class KEYBOARD_KEYS(Enum):
    PREFIX = "keyboard_"
    SETTINGS="settings"
    PAYMENTS="payments"
    TRADING="trading"
    INSTRUCTION="instruction"
    INFORMATION="information"
    EXCHANGES_LIST="exchangesList"
    TOP_INTEREST_RATES="topInterestRates"
    MIN_SPREAD="minSpread"
    GO_HOME="goHome"


BUTTON_TEXT_BY_KEY = {
    KEYBOARD_KEYS.SETTINGS: "⚙️ Настройки",
    KEYBOARD_KEYS.PAYMENTS: "💵️ Оплата",
    KEYBOARD_KEYS.TRADING: "📋️ Торговля",
    KEYBOARD_KEYS.INFORMATION: "🗒️ Информация",
    KEYBOARD_KEYS.EXCHANGES_LIST: "📓️️ Список бирж",
    KEYBOARD_KEYS.TOP_INTEREST_RATES: "ТОП-20 процентных ставок",
    KEYBOARD_KEYS.MIN_SPREAD: "Выберите минимальный спред для получения актуальных связок:",
    KEYBOARD_KEYS.GO_HOME: "Главное меню",
    KEYBOARD_KEYS.INSTRUCTION: "Инструкция",
}





