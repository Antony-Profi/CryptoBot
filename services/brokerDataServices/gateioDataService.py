import ccxt
from constans import GATEIO
from helpers.dateHelper import getTimeDifference
from models.brokerFundingRate import BrokerFundingRate


def fetchData(brokerData):
    gateio = ccxt.gateio()

    gateio_funding_rates = gateio.fetch_funding_rates()

    formatted_gateio_funding_rates = []

    for gateio_funding_rate in gateio_funding_rates.values():

        formatted_gateio_funding_rate = BrokerFundingRate()
        formatted_gateio_funding_rate.broker = GATEIO
        formatted_gateio_funding_rate.symbol = gateio_funding_rate["symbol"]
        formatted_gateio_funding_rate.markPrice = gateio_funding_rate["markPrice"]
        formatted_gateio_funding_rate.fundingRate = gateio_funding_rate["fundingRate"]
        formatted_gateio_funding_rate.fundingDatetime = gateio_funding_rate["fundingDatetime"]
        formatted_gateio_funding_rate.timeLeft = getTimeDifference(gateio_funding_rate["fundingDatetime"])

        formatted_gateio_funding_rates.append(formatted_gateio_funding_rate)

    brokerData.gateioData = formatted_gateio_funding_rates
