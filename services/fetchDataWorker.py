from models.brokerData import BrokerData
from services.binanceDataService import fetchData as fetchBinanceData
from services.comexDataService import fetch_funding_rates as fetchComexData
from services.bitgetDataService import fetchData as fetchBitgetData
from services.bybitDataService import fetchData as fetchBybitData
from services.gateioDataService import get_contracts_data as fetchGateioData
from services.mexcDataService import fetchData as fetchMexcData
from services.coinexDataService import fetchData as fetchCoinexData
from services.okxDataService import fetchData as fetchOkxData
from services.bitmartDataService import fetchData as fetchBitmartData

import threading


def start(timeout: int, brokerData: BrokerData):
    brokerData.binanceData = fetchBinanceData()
    brokerData.comexData = fetchComexData()
    brokerData.bitgetData = fetchBitgetData()
    brokerData.bybitData = fetchBybitData()
    brokerData.gateioData = fetchGateioData()
    brokerData.mexcData = fetchMexcData()
    brokerData.coinexData = fetchCoinexData()
    brokerData.okxData = fetchOkxData()
    brokerData.bitmartData = fetchBitmartData()

    print("Binance", brokerData.binanceData)
    print("Comex", brokerData.comexData)
    print("Bitget", brokerData.bitgetData)
    print("Bybit", brokerData.bybitData)
    print("Gateio", brokerData.gateioData)
    print("Mexc", brokerData.mexcData)
    print("Coinex", brokerData.coinexData)
    print("Okx", brokerData.okxData)
    print("Bitmart", brokerData.bitmartData)

    threading.Timer(timeout, start, [timeout, brokerData]).start()
