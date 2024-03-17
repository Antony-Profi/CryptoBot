import ccxt
from enums import broker
from enums.broker import Broker
from constans import OKX


def fetchData():
    binance = ccxt.binance()
    okx = ccxt.okx()

    okx_funding_rates = binance.fetch_funding_rates()

    formatted_okx_funding_rates = []

    for okx_funding_rate in okx_funding_rates.values():
        # print(bybit_funding_rates)
        formatted_okx_funding_rate = {
            broker: OKX,
            "symbol": okx_funding_rate["symbol"],
            "fundingRate": okx_funding_rate["fundingRate"],
            "fundingDatetime": okx_funding_rate["fundingDatetime"]
        }
        formatted_okx_funding_rates.append(formatted_okx_funding_rate)

    return formatted_okx_funding_rates


data = fetchData()
print(data)
