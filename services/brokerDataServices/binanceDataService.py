import ccxt
from constans import BINANCE
from helpers.dateHelper import getTimeDifference
from models.brokerFundingRate import BrokerFundingRate


def fetchData(brokerData):
    binance = ccxt.binance()

    binance_funding_rates = binance.fetch_funding_rates()

    formatted_binance_funding_rates = []

    for binance_funding_rate in binance_funding_rates.values():

        formatted_binance_funding_rate = BrokerFundingRate(BINANCE,
                                                           binance_funding_rate["symbol"],
                                                           binance_funding_rate["fundingRate"],
                                                           binance_funding_rate["fundingDatetime"],
                                                           binance_funding_rate["markPrice"])

        formatted_binance_funding_rates.append(formatted_binance_funding_rate)

    brokerData.binanceData = formatted_binance_funding_rates
