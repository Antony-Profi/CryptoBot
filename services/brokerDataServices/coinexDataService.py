import ccxt
from enums import broker
from enums.broker import Broker
from constans import COINEX


def fetchData(coinexData):
    coinex = ccxt.coinex()

    coinex_funding_rates = coinex.fetch_funding_rates()

    formatted_coinex_funding_rates = []

    for coinex_funding_rate in coinex_funding_rates.values():
        formatted_coinex_funding_rate = {
            broker: COINEX,
            "symbol": coinex_funding_rate["symbol"],
            "fundingRate": coinex_funding_rate["fundingRate"],
            "fundingDatetime": coinex_funding_rate["fundingDatetime"]
        }
        formatted_coinex_funding_rates.append(formatted_coinex_funding_rate)

    coinexData = formatted_coinex_funding_rates
