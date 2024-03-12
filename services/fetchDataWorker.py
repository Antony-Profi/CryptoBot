from services.binanceDataService import fetchData as fetchBinanceData 
from models.brokerData import BrokerData
from services.comexDataService import fetch_funding_rates as fetchComexData

import threading


def start(timeout: int, brokerData: BrokerData):
    brokerData.binanceData = fetchBinanceData()
    brokerData.comexData = fetchComexData()

    print(brokerData.binanceData)

    threading.Timer(timeout, start, [timeout, brokerData]).start()
