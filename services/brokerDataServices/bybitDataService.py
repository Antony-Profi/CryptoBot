import ccxt
from constans import BYBIT
from helpers.dateHelper import getTimeDifference
from models.brokerFundingRate import BrokerFundingRate


def fetchData(brokerData):
    bybit = ccxt.bybit()

    bybit_funding_rates = bybit.fetch_funding_rates()

    formatted_bybit_funding_rates = []

    for bybit_funding_rate in bybit_funding_rates.values():

        formatted_bybit_funding_rate = BrokerFundingRate(BYBIT,
                                                        bybit_funding_rate["symbol"], 
                                                        bybit_funding_rate["fundingRate"],
                                                        bybit_funding_rate["fundingDatetime"],
                                                        bybit_funding_rate["markPrice"])

        formatted_bybit_funding_rates.append(formatted_bybit_funding_rate)

    brokerData.bybitData = formatted_bybit_funding_rates
