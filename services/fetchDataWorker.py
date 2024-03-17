from models.brokerData import BrokerData
from services.brokerDataServices.binanceDataService import fetchData as fetchBinanceData
from services.brokerDataServices.commexDataService import fetchData as fetchComexData
from services.brokerDataServices.bitgetDataService import fetchData as fetchBitgetData
from services.brokerDataServices.bybitDataService import fetchData as fetchBybitData
from services.brokerDataServices.gateioDataService import fetchData as fetchGateioData
from services.brokerDataServices.mexcDataService import fetchData as fetchMexcData
from services.brokerDataServices.coinexDataService import fetchData as fetchCoinexData
from services.brokerDataServices.okxDataService import fetchData as fetchOkxData
from services.brokerDataServices.bitmartDataService import fetchData as fetchBitmartData
from multiprocessing import Process

import threading


def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()


def start(timeout: int, brokerData: BrokerData):
    runInParallel(fetchBinanceData(brokerData.binanceData),
                  fetchComexData(brokerData.commexData),
                  fetchBitgetData(brokerData.bitgetData),
                  fetchBybitData(brokerData.bybitData),
                  fetchGateioData(brokerData.gateioData),
                  fetchMexcData(brokerData.mexcData),
                  fetchCoinexData(brokerData.coinexData),
                  fetchOkxData(brokerData.okxData),
                  fetchBitmartData(brokerData.bitmartData))

    print("Binance", brokerData.binanceData)
    print("Comex", brokerData.commexData)
    print("Bitget", brokerData.bitgetData)
    print("Bybit", brokerData.bybitData)
    print("Gateio", brokerData.gateioData)
    print("Mexc", brokerData.mexcData)
    print("Coinex", brokerData.coinexData)
    print("Okx", brokerData.okxData)
    print("Bitmart", brokerData.bitmartData)

    threading.Timer(timeout, start, [timeout, brokerData]).start()
