import ccxt
from enums import broker
from enums.broker import Broker
from constans import GATEIO


def fetchData():
    gateio = ccxt.gateio()

    gateio_funding_rates = gateio.fetch_funding_rates()

    formatted_gateio_funding_rates = []

    for gateio_funding_rate in gateio_funding_rates.values():
        # print(bybit_funding_rates)
        formatted_gateio_funding_rate = {
            broker: GATEIO,
            "symbol": gateio_funding_rate["symbol"],
            "fundingRate": gateio_funding_rate["fundingRate"],
            "fundingDatetime": gateio_funding_rate["fundingDatetime"]
        }
        formatted_gateio_funding_rates.append(formatted_gateio_funding_rate)

    return formatted_gateio_funding_rates


data = fetchData()
print(data)
