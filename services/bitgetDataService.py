import ccxt
from enums import broker
from enums.broker import Broker
from constans import BITGET


def fetchData():
    binance = ccxt.binance()
    bitget = ccxt.bitget()

    bitget_funding_rates = binance.fetch_funding_rates()

    formatted_bitget_funding_rates = []

    for bitget_funding_rate in bitget_funding_rates.values():
        # print(bybit_funding_rates)
        formatted_bitget_funding_rate = {
            broker: BITGET,
            "symbol": bitget_funding_rate["symbol"],
            "fundingRate": bitget_funding_rate["fundingRate"],
            "fundingDatetime": bitget_funding_rate["fundingDatetime"]
        }
        formatted_bitget_funding_rates.append(formatted_bitget_funding_rate)

    return formatted_bitget_funding_rates


data = fetchData()
print(data)
