import pprint


def getMaxSpreadBrokers(groupedBrokerData):
  maxSpread = 0
  maxSpreadBrokers = {}

  if len(groupedBrokerData) > 1:

    for firstBrokerData in groupedBrokerData:
      for secondBrokerData in groupedBrokerData:
        currentSpread = abs(firstBrokerData["fundingRate"] - secondBrokerData["fundingRate"])

        if currentSpread > maxSpread:
          maxSpread = currentSpread
          maxSpreadBrokers = {
            "symbol": firstBrokerData["symbol"],
            "firstBrokerData": firstBrokerData,
            "secondBrokerData": secondBrokerData,
            "spread": currentSpread,
          }

    if maxSpread > 0:
      return maxSpreadBrokers
    else:
      return None

  else:
    return None

  
def analyzeBrokerData(brokerData):
  flattenBrokerData = brokerData.binanceData\
                      + brokerData.bybitData\
                      + brokerData.coinexData\
                      + brokerData.gateioData

  groupedBrokerData = {}
  for brokerSymbolData in flattenBrokerData:
      t = groupedBrokerData.setdefault(brokerSymbolData['symbol'], [])
      t.append(brokerSymbolData)

  result = []

  for symbol in groupedBrokerData.keys():
    maxSpreadBrokers = getMaxSpreadBrokers(groupedBrokerData[symbol])

    if maxSpreadBrokers != None:
      result.append(maxSpreadBrokers)

  result.sort(key=lambda x: x["spread"], reverse=True)

  with open('../result.txt', 'w') as file: 
    file.write(pprint.pformat(result)) 
  
  print('done')

  return result
