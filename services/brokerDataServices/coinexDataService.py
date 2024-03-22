import ccxt
from constans import COINEX
from helpers.dateHelper import getTimeDifference
from models.brokerFundingRate import BrokerFundingRate


def fetchData(brokerData):
    coinex = ccxt.coinex()

    coinex_funding_rates = coinex.fetch_funding_rates()

    formatted_coinex_funding_rates = []

    for coinex_funding_rate in coinex_funding_rates.values():
        formatted_coinex_funding_rate = BrokerFundingRate()
        formatted_coinex_funding_rate.broker = COINEX
        formatted_coinex_funding_rate.symbol = coinex_funding_rate["symbol"]
        formatted_coinex_funding_rate.markPrice = coinex_funding_rate["markPrice"]
        formatted_coinex_funding_rate.fundingRate = coinex_funding_rate["fundingRate"]
        formatted_coinex_funding_rate.fundingDateTime = coinex_funding_rate["fundingDatetime"]
        formatted_coinex_funding_rate.timeLeft = getTimeDifference(coinex_funding_rate["fundingDatetime"])

        formatted_coinex_funding_rates.append(formatted_coinex_funding_rate)

    brokerData.coinexData = formatted_coinex_funding_rates
