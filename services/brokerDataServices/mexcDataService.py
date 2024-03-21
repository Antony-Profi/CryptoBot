import ccxt
from constans import MEXC
from helpers.dateHelper import getTimeDifference
from models.brokerFundingRate import BrokerFundingRate


def fetchData(brokerData):
    binance = ccxt.binance()
    mexc = ccxt.mexc()

    symbols = binance.fetch_funding_rates().keys()

    formatted_mexc_funding_rates = []

    for symbol in symbols:
        mexc_funding_rate = mexc.fetch_funding_rate(symbol)
        try:

            formatted_mexc_funding_rate = BrokerFundingRate()
            formatted_mexc_funding_rate.broker = MEXC
            formatted_mexc_funding_rate.symbol = mexc_funding_rate["symbol"]
            formatted_mexc_funding_rate.fundingRate = mexc_funding_rate["fundingRate"]
            formatted_mexc_funding_rate.fundingDatetime = mexc_funding_rate["fundingDatetime"]
            formatted_mexc_funding_rate.timeLeft = getTimeDifference(mexc_funding_rate["fundingDatetime"])

            formatted_mexc_funding_rates.append(formatted_mexc_funding_rate)
        except:
            continue
    brokerData.mexcData = formatted_mexc_funding_rates
