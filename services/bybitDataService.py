import ccxt
from enums import broker
from enums.broker import Broker
from constans import BYBIT


def fetchData():
    bybit = ccxt.bybit()

    bybit_funding_rates = bybit.fetch_funding_rates()

    formatted_bybit_funding_rates = []

    for bybit_funding_rate in bybit_funding_rates.values():
        # print(bybit_funding_rates)
        formatted_bybit_funding_rate = {
            broker: BYBIT,
            "symbol": bybit_funding_rate["symbol"],
            "fundingRate": bybit_funding_rate["fundingRate"],
            "fundingDatetime": bybit_funding_rate["fundingDatetime"]
        }
        formatted_bybit_funding_rates.append(formatted_bybit_funding_rate)

    return formatted_bybit_funding_rates


data = fetchData()
print(data)
