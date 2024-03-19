import ccxt
from enums import broker
from enums.broker import Broker
from constans import GATEIO
from helpers.dateHelper import getHoursDifferenceWithCurrentDateTime


def fetchData(brokerData):
    gateio = ccxt.gateio()

    gateio_funding_rates = gateio.fetch_funding_rates()

    formatted_gateio_funding_rates = []

    for gateio_funding_rate in gateio_funding_rates.values():

        formatted_gateio_funding_rate = {
            "broker": GATEIO,
            "symbol": gateio_funding_rate["symbol"],
            "fundingRate": gateio_funding_rate["fundingRate"],
            "fundingDatetime": gateio_funding_rate["fundingDatetime"],
            "hoursLeft": getHoursDifferenceWithCurrentDateTime(gateio_funding_rate["fundingDatetime"])
        }

        if formatted_gateio_funding_rate["hoursLeft"] >= 1:
            formatted_gateio_funding_rate["fundingRatePerHourRatio"] = formatted_gateio_funding_rate["fundingRate"] / \
                                                                        formatted_gateio_funding_rate["hoursLeft"]
        else:
            formatted_gateio_funding_rate["fundingRatePerHourRatio"] = 0

        formatted_gateio_funding_rates.append(formatted_gateio_funding_rate)

    brokerData.gateioData = formatted_gateio_funding_rates
