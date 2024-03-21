import ccxt
from constans import BITGET
from helpers.dateHelper import getTimeDifference
from models.brokerFundingRate import BrokerFundingRate


def fetchData(brokerData):
    binance = ccxt.binance()
    bitget = ccxt.bitget()

    symbols = binance.fetch_funding_rates().keys()

    formatted_bitget_funding_rates = []

    for symbol in symbols:
        bitget_funding_rate = bitget.fetch_funding_rate(symbol)
        try:

            formatted_bitget_funding_rate = BrokerFundingRate()
            formatted_bitget_funding_rate.broker = BITGET
            formatted_bitget_funding_rate.symbol = bitget_funding_rate["symbol"]
            formatted_bitget_funding_rate.fundingRate = bitget_funding_rate["fundingRate"]
            formatted_bitget_funding_rate.fundingDatetime = bitget_funding_rate["fundingDatetime"]
            formatted_bitget_funding_rate.timeLeft = getTimeDifference(bitget_funding_rate["fundingDatetime"])

            formatted_bitget_funding_rates.append(formatted_bitget_funding_rate)

        except Exception as e:
            print("Error processing symbol:", symbol, "Error:", e)

    brokerData.bitgetData = formatted_bitget_funding_rates
