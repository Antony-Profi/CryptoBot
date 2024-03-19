import ccxt
from enums import broker
from enums.broker import Broker
from constans import COINEX
from helpers.dateHelper import getHoursDifferenceWithCurrentDateTime


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
            "hoursLeft": getHoursDifferenceWithCurrentDateTime(coinex_funding_rate["fundingDatetime"])
        }

        if formatted_coinex_funding_rate["hoursLeft"] >= 1:
            formatted_coinex_funding_rate["fundingRatePerHourRatio"] = coinex_funding_rate["fundingRate"] / \
                                                                      formatted_coinex_funding_rate["hoursLeft"]
        else:
            formatted_coinex_funding_rate["fundingRatePerHourRatio"] = 0

        formatted_coinex_funding_rates.append(formatted_coinex_funding_rate)

    brokerData.coinexData = formatted_coinex_funding_rates
