from models.brokerData import BrokerData


def getBunchesFormattedString(brokerData: BrokerData):
    top20bunches = brokerData[:20]
    
    result = ""
    
    for topBunch in top20bunches:
        result += formatBunch(topBunch)
    
    return result


def formatBunch(bunch):
    result = bunch["firstBrokerData"].symbol + '\n' + '\n'

    if bunch["firstBrokerData"].fundingRate > bunch["secondBrokerData"].fundingRate:
        result += formatFundingRateForShort(bunch["firstBrokerData"])
        result += formatFundingRateForLong(bunch["secondBrokerData"])
        # result += formatSpreads(bunch["secondBrokerData"].fundingRate, bunch["firstBrokerData"].fundingRate, bunch["spread"])
    else:
        result += formatFundingRateForShort(bunch["secondBrokerData"])
        result += formatFundingRateForLong(bunch["firstBrokerData"])
        # result += formatSpreads(bunch["firstBrokerData"].fundingRate, bunch["secondBrokerData"].fundingRate, bunch["spread"])

    return result + '\n' + '\n'


def formatFundingRateForShort(fundingRate):
    result = 'Short:' + '\n'
    result += fundingRate.broker + ' ' + str(fundingRate.fundingRate) + '\n'
    result += '🕒 До начисления: ' + fundingRate.timeLeft + '\n'
    result += '💵 Цена: ' + str(fundingRate.markPrice) + '\n' + '\n'
    return result


def formatFundingRateForLong(fundingRate):
    result = 'Long:' + '\n'
    result += fundingRate.broker + ' ' + str(fundingRate.fundingRate) + '\n'
    result += '🕒 До начисления: ' + fundingRate.timeLeft + '\n'
    result += '💵 Цена: ' + str(fundingRate.markPrice) + '\n'
    return result


def formatSpreads(buyPrice, sellPrice, fundingSpread):
    buySellSpread = sellPrice-buyPrice/(buyPrice+sellPrice/2)
    result = "Спред:" + '\n' 

    result += "💱 Курсы: " + str(buySellSpread) + '%' + '\n'
    result += "⚖️Ставки: " + str(fundingSpread) + '%' + '\n'
    # return result
