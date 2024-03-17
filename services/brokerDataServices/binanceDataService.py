import ccxt
from enums import broker
from enums.broker import Broker
from constans import BINANCE


def fetchData(binanceData):
    binance = ccxt.binance()

    binance_funding_rates = binance.fetch_funding_rates()

    formatted_binance_funding_rates = []

    for binance_funding_rate in binance_funding_rates.values():
        # print(bybit_funding_rates)
        formatted_binance_funding_rate = {
            broker: BINANCE,
            "symbol": binance_funding_rate["symbol"],
            "fundingRate": binance_funding_rate["fundingRate"],
            "fundingDatetime": binance_funding_rate["fundingDatetime"]
        }
        formatted_binance_funding_rates.append(formatted_binance_funding_rate)

    binanceData = formatted_binance_funding_rates
