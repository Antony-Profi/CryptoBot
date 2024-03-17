import ccxt
from enums import broker
from enums.broker import Broker
from constans import MEXC


def fetchData():
    binance = ccxt.binance()
    mexc = ccxt.mexc()

    mexc_funding_rates = binance.fetch_funding_rates()

    formatted_mexc_funding_rates = []

    for mexc_funding_rate in mexc_funding_rates.values():
        # print(bybit_funding_rates)
        formatted_mexc_funding_rate = {
            broker: MEXC,
            "symbol": mexc_funding_rate["symbol"],
            "fundingRate": mexc_funding_rate["fundingRate"],
            "fundingDatetime": mexc_funding_rate["fundingDatetime"]
        }
        formatted_mexc_funding_rates.append(formatted_mexc_funding_rate)

    return formatted_mexc_funding_rates


data = fetchData()
print(data)
