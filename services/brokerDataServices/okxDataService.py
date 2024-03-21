import ccxt
from constans import OKX
from helpers.dateHelper import getTimeDifference
from models.brokerFundingRate import BrokerFundingRate


def fetchData(brokerData):
    binance = ccxt.binance()
    okx = ccxt.okx()

    symbols = binance.fetch_funding_rates().keys()

    formatted_okx_funding_rates = []

    for symbol in symbols:
        okx_funding_rate = okx.fetch_funding_rate(symbol)
        try:

            formatted_okx_funding_rate = BrokerFundingRate()
            formatted_okx_funding_rate.broker = OKX
            formatted_okx_funding_rate.symbol = okx_funding_rate["symbol"]
            formatted_okx_funding_rate.fundingRate = okx_funding_rate["fundingRate"]
            formatted_okx_funding_rate.fundingDatetime = okx_funding_rate["fundingDatetime"]
            formatted_okx_funding_rate.timeLeft = getTimeDifference(okx_funding_rate["fundingDatetime"])
            formatted_okx_funding_rates.append(formatted_okx_funding_rate)
        except:
            continue
    brokerData.okxData = formatted_okx_funding_rates
