from models.brokerData import BrokerData


def getBunchesFormattedMessages(brokerData: BrokerData):
    top20bunches = brokerData[:20]
    
    result = []
    
    for topBunch in top20bunches:
        result.append(formatBunch(topBunch))
    
    return result


def formatBunch(bunch):
    result = '<b>' + bunch["firstBrokerData"].symbol + '</b>' + '\n' + '\n'

    if bunch["firstBrokerData"].fundingRate > bunch["secondBrokerData"].fundingRate:
        result += formatFundingRateForShort(bunch["firstBrokerData"])
        result += formatFundingRateForLong(bunch["secondBrokerData"])
        result += formatSpreads(bunch["secondBrokerData"].fundingRate, bunch["firstBrokerData"].fundingRate, bunch["spread"])
    else:
        result += formatFundingRateForShort(bunch["secondBrokerData"])
        result += formatFundingRateForLong(bunch["firstBrokerData"])
        result += formatSpreads(bunch["firstBrokerData"].fundingRate, bunch["secondBrokerData"].fundingRate, bunch["spread"])

    return result + '\n' + '\n'


def formatFundingRateForShort(fundingRate):
    result = '🔴' + '\n' + 'Short:' + '\n'
    result += fundingRate.broker + ' ' + format(fundingRate.fundingRate, 'f') + '%' + '\n'
    result += '🕒 До начисления: ' + fundingRate.timeLeft + '\n'
    result += '💵 Цена: ' + format(fundingRate.markPrice, 'f') + '\n' + '\n'
    return result


def formatFundingRateForLong(fundingRate):
    result = '🟢' + '\n' + 'Long:' + '\n'
    result += fundingRate.broker + ' ' + format(fundingRate.fundingRate, 'f') + '%' + '\n'
    result += '🕒 До начисления: ' + fundingRate.timeLeft + '\n'
    result += '💵 Цена: ' + format(fundingRate.markPrice, 'f') + '\n' + '\n'
    return result


def formatSpreads(buyPrice, sellPrice, fundingSpread):
    buySellSpread = sellPrice-buyPrice/(buyPrice+sellPrice/2)
    result = "Спред:" + '\n' 

    result += "💱 Курсы: " + format(buySellSpread, 'f') + '%' + '\n'
    result += "⚖️ Ставки: " + format(fundingSpread * 100, 'f') + '%' + '\n'
    return result
