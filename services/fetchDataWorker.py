from services.binanceDataService import fetchData as fetchBinanceData 
from models.brokerData import BrokerData
from services.comexDataService import fetch_funding_rates as fetchComexData
from services.gateioDataService import get_contracts_data as fetchGateioData

import threading


def start(timeout: int, brokerData: BrokerData):
    brokerData.binanceData = fetchBinanceData()
    brokerData.comexData = fetchComexData()
    brokerData.gateioData = fetchGateioData()

    print("Binance", brokerData.binanceData)
    print("Comex", brokerData.comexData)
    print("Gateio", brokerData.gateioData)

    threading.Timer(timeout, start, [timeout, brokerData]).start()
