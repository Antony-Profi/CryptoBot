import ccxt
from enums import broker
from enums.broker import Broker
from constans import BITMART


def fetchData():
    binance = ccxt.binance()
    bitmart = ccxt.bitmart()

    bitmart_funding_rates = binance.fetch_funding_rates()

    formatted_bitmart_funding_rates = []

    for bitmart_funding_rate in bitmart_funding_rates.values():
        # print(bybit_funding_rates)
        formatted_bitmart_funding_rate = {
            broker: BITMART,
            "symbol": bitmart_funding_rate["symbol"],
            "fundingRate": bitmart_funding_rate["fundingRate"],
            "fundingDatetime": bitmart_funding_rate["fundingDatetime"]
        }
        formatted_bitmart_funding_rates.append(formatted_bitmart_funding_rate)

    return formatted_bitmart_funding_rates


data = fetchData()
print(data)
