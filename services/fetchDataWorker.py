from ast import Mod
from models.brokerData import BrokerData
from services.brokerDataAnalyzer import analyzeBrokerData
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


def start(timeout: int, brokerData: BrokerData):
  runInParallel(fetchBinanceData(brokerData),
                fetchBybitData(brokerData),
                fetchCoinexData(brokerData),
                fetchGateioData(brokerData))

  brokerData.bunches = analyzeBrokerData(brokerData)

  threading.Timer(timeout, start, [timeout, brokerData]).start()
