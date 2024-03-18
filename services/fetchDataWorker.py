from ast import Mod
from models.brokerData import BrokerData
from services.brokerDataServices.binanceDataService import fetchData as fetchBinanceData
from services.brokerDataServices.commexDataService import fetchData as fetchCommexData
from services.brokerDataServices.bitgetDataService import fetchData as fetchBitgetData
from services.brokerDataServices.bybitDataService import fetchData as fetchBybitData
from services.brokerDataServices.gateioDataService import fetchData as fetchGateioData
from services.brokerDataServices.mexcDataService import fetchData as fetchMexcData
from services.brokerDataServices.coinexDataService import fetchData as fetchCoinexData
from services.brokerDataServices.okxDataService import fetchData as fetchOkxData
from services.brokerDataServices.bitmartDataService import fetchData as fetchBitmartData
from multiprocessing import Process
import pprint


import threading

global brokerData


def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

    return p
  
def getMaxSpreadBrokers(groupedBrokerData):
  maxSpread = 0
  maxSpreadBrokers = {}

  if len(groupedBrokerData) > 1:

    for firstBrokerData in groupedBrokerData:
      for secondBrokerData in groupedBrokerData:
        currentSpread = abs(firstBrokerData["fundingRatePerHourRatio"] - secondBrokerData["fundingRatePerHourRatio"])

        if currentSpread > maxSpread:
          maxSpread = currentSpread
          maxSpreadBrokers = {
            "symbol": firstBrokerData["symbol"],
            "firstBroker": firstBrokerData["broker"],
            "secondBroker": secondBrokerData["broker"],
            "firstBrokerHoursLeft": firstBrokerData["hoursLeft"],
            "secondBrokerHoursLeft": secondBrokerData["hoursLeft"],
            "spread": currentSpread,
          }

    if maxSpread > 0:
      return maxSpreadBrokers
    else:
      return None

  else:
    return None

  
def analyzeBrokerData(brokerData):
  flattenBrokerData = brokerData.binanceData + brokerData.bybitData

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

def start(timeout: int, brokerData: BrokerData):
  runInParallel(fetchBinanceData(brokerData),
                fetchBybitData(brokerData))
  
  result = analyzeBrokerData(brokerData)
  
  threading.Timer(timeout, start, [timeout, brokerData]).start()
