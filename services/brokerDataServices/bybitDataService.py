import ccxt
from enums import broker
from enums.broker import Broker
from constans import BYBIT
from helpers.dateHelper import getHoursDifferenceWithCurrentDateTime


def fetchData(brokerData):
    bybit = ccxt.bybit()

    bybit_funding_rates = bybit.fetch_funding_rates()

    formatted_bybit_funding_rates = []

    for bybit_funding_rate in bybit_funding_rates.values():
        formatted_bybit_funding_rate = {
            "broker": BYBIT,
            "symbol": bybit_funding_rate["symbol"],
            "fundingRate": bybit_funding_rate["fundingRate"],
            "fundingDatetime": bybit_funding_rate["fundingDatetime"],
            "hoursLeft": getHoursDifferenceWithCurrentDateTime(bybit_funding_rate["fundingDatetime"]),
        }
        formatted_bybit_funding_rates.append(formatted_bybit_funding_rate)

    brokerData.bybitData = formatted_bybit_funding_rates
