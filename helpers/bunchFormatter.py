from models.brokerData import BrokerData


def getBunchesFormattedMessages(brokerData: BrokerData):
    top20bunches = brokerData[:20]
    
    result = []
    
    for topBunch in top20bunches:
        result.append(formatBunch(topBunch))
    
    return result


def formatBunch(bunch):
    result = '<b>' + bunch.symbol + '</b>' + '\n' + '\n'

    if bunch.shortFundingRate > bunch.longFundingRate:
        result += formatFundingRateForShort(bunch)
        result += formatFundingRateForLong(bunch)
        # result += formatSpreads(bunch.secondBrokerData.fundingRate, bunch.firstBrokerData.fundingRate, bunch.spread)
    else:
        result += formatFundingRateForShort(bunch)
        result += formatFundingRateForLong(bunch)
        # result += formatSpreads(bunch.secondBrokerData.fundingRate, bunch.firstBrokerData.fundingRate, bunch.spread)

    return result + '\n' + '\n'


def formatFundingRateForShort(bunch):
    result = '🔴 ' + 'Short:' + '\n'
    result += bunch.shortBroker + ' ' + format(bunch.shortFundingRate * 100, 'f') + '%' + '\n'
    result += '🕒 До начисления: ' + bunch.shortFundingRateExpirationDateTime + '\n'
    result += '💵 Цена: ' + format(bunch.shortMarkPrice, 'f') + '\n' + '\n'
    return result


def formatFundingRateForLong(bunch):
    result = '🟢 ' + 'Long:' + '\n'
    result += bunch.longBroker + ' ' + format(bunch.longFundingRate * 100, 'f') + '%' + '\n'
    result += '🕒 До начисления: ' + bunch.longFundingRateExpirationDateTime + '\n'
    result += '💵 Цена: ' + format(bunch.longMarkPrice, 'f') + '\n' + '\n'
    
    return result


def formatSpreads(buyPrice, sellPrice, fundingSpread):
    buySellSpread = sellPrice - buyPrice / (buyPrice + sellPrice / 2)
    result = "Спред:" + '\n'

    result += "💱 Курсы: " + format(buySellSpread, 'f') + '%' + '\n'
    result += "⚖️ Ставки: " + format(fundingSpread * 100, 'f') + '%' + '\n'
    
    return result
