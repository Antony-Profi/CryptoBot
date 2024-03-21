import ccxt
from constans import GATEIO
from helpers.dateHelper import getTimeDifference


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
            "timeLeft": getTimeDifference(gateio_funding_rate["fundingDatetime"])
        }

        formatted_gateio_funding_rates.append(formatted_gateio_funding_rate)

    brokerData.gateioData = formatted_gateio_funding_rates
