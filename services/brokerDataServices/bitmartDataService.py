import ccxt
from constans import BITMART
from helpers.dateHelper import getTimeDifference
from models.brokerFundingRate import BrokerFundingRate


def fetchData(brokerData):
    binance = ccxt.binance()
    bitmart = ccxt.bitmart()

    symbols = binance.fetch_funding_rates().keys()

    formatted_bitmart_funding_rates = []

    for symbol in symbols:
        bitmart_funding_rate = bitmart.fetch_funding_rate(symbol)
        try:

            formatted_bitmart_funding_rate = BrokerFundingRate()
            formatted_bitmart_funding_rate.broker = BITMART
            formatted_bitmart_funding_rate.symbol = bitmart_funding_rate["symbol"]
            formatted_bitmart_funding_rate.fundingRate = bitmart_funding_rate["fundingRate"]
            formatted_bitmart_funding_rate.fundingDatetime = bitmart_funding_rate["fundingDatetime"]
            formatted_bitmart_funding_rate.timeLeft = getTimeDifference(bitmart_funding_rate["fundingDatetime"])

            formatted_bitmart_funding_rates.append(formatted_bitmart_funding_rate)
        except:
            continue
    brokerData.bitmartData = formatted_bitmart_funding_rates
