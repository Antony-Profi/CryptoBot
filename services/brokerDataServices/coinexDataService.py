import ccxt
from constans import COINEX
from helpers.dateHelper import getTimeDifference


def fetchData(brokerData):
    coinex = ccxt.coinex()

    coinex_funding_rates = coinex.fetch_funding_rates()

    formatted_coinex_funding_rates = []

    for coinex_funding_rate in coinex_funding_rates.values():
        formatted_coinex_funding_rate = {
            "broker": COINEX,
            "symbol": coinex_funding_rate["symbol"],
            "fundingRate": coinex_funding_rate["fundingRate"],
            "fundingDatetime": coinex_funding_rate["fundingDatetime"],
            "timeLeft": getTimeDifference(coinex_funding_rate["fundingDatetime"]),
        }

        formatted_coinex_funding_rates.append(formatted_coinex_funding_rate)

    brokerData.coinexData = formatted_coinex_funding_rates
