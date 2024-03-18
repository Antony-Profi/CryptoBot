import ccxt
from enums import broker
from enums.broker import Broker
from constans import BINANCE
from helpers.dateHelper import getHoursDifferenceWithCurrentDateTime


def fetchData(brokerData):
    binance = ccxt.binance()

    binance_funding_rates = binance.fetch_funding_rates()

    formatted_binance_funding_rates = []

    for binance_funding_rate in binance_funding_rates.values():

        formatted_binance_funding_rate = {
            "broker": BINANCE,
            "symbol": binance_funding_rate["symbol"],
            "fundingRate": binance_funding_rate["fundingRate"],
            "fundingDatetime": binance_funding_rate["fundingDatetime"],
            "hoursLeft": getHoursDifferenceWithCurrentDateTime(binance_funding_rate["fundingDatetime"]),
            "fundingRatePerHourRatio":
                binance_funding_rate["fundingRate"] / getHoursDifferenceWithCurrentDateTime(
                    binance_funding_rate["fundingDatetime"]
                )
        }
        formatted_binance_funding_rates.append(formatted_binance_funding_rate)

    brokerData.binanceData = formatted_binance_funding_rates
