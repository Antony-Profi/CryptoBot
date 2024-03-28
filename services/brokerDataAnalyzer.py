from models.bunch import Bunch


def analyzeBrokerData(brokerData):
  flattenBrokerData = flatBrokerData(brokerData)

  groupedBrokerData = groupBrokerDataBySymbol(flattenBrokerData)

  bunches = []

  for symbol in groupedBrokerData.keys():
    bunch = getBunchForSymbol(groupedBrokerData[symbol])

    if bunch != None and bunch.fundingSpread > 0.001:
      bunches.append(bunch)

  bunches.sort(key=lambda x: x.fundingSpread, reverse=True)

  bunches = bunches[:20]

  return bunches


def flatBrokerData(brokerData):
  return brokerData.binanceData\
        + brokerData.bybitData\
        + brokerData.coinexData\
        + brokerData.gateioData


def groupBrokerDataBySymbol(brokerData):
  groupedBrokerData = {}

  for brokerSymbolData in brokerData:
      t = groupedBrokerData.setdefault(brokerSymbolData.symbol, [])
      t.append(brokerSymbolData)
  
  return groupedBrokerData


def getBunchForSymbol(symbolFundingRates):

  if len(symbolFundingRates) <= 1:
    return None
  
  maxSpreadFundingRates = getMaxSpreadFundingRatesBySymbol(symbolFundingRates)

  if maxSpreadFundingRates == None:
    return None

  return createBunchFromMaxSpreadFundingRates(maxSpreadFundingRates)


def getMaxSpreadFundingRatesBySymbol(symbolFundingRates):
  resultFundingRateA = {}
  resultFundingRateB = {}
  maxSpread = 0

  for fundingRateA in symbolFundingRates:

    for fundingRateB in symbolFundingRates:
      currentSpread = abs(fundingRateA.fundingRate - fundingRateB.fundingRate)

      if currentSpread > maxSpread:
        maxSpread = currentSpread
        resultFundingRateA = fundingRateA
        resultFundingRateB = fundingRateB

  if maxSpread > 0:
    return [resultFundingRateA, resultFundingRateB]
  else:
    return None


def createBunchFromMaxSpreadFundingRates(maxSpreadFundingRates):
    maxSpreadFundingRates.sort(key=lambda x: x.fundingRate, reverse=True)

    shortFundingRate = maxSpreadFundingRates[0]
    longFundingRate = maxSpreadFundingRates[1]

    priceSpread = (shortFundingRate.markPrice - longFundingRate.markPrice) / shortFundingRate.markPrice
    fundingSpread = abs(shortFundingRate.fundingRate - longFundingRate.fundingRate)

    bunch: Bunch = Bunch(shortFundingRate.symbol,
                         shortFundingRate.broker,
                         shortFundingRate.fundingRate,
                         shortFundingRate.fundingRateExpirationDateTime,
                         shortFundingRate.markPrice,
                         longFundingRate.broker,
                         longFundingRate.fundingRate,
                         longFundingRate.fundingRateExpirationDateTime,
                         longFundingRate.markPrice,
                         priceSpread,
                         fundingSpread)
    return bunch
