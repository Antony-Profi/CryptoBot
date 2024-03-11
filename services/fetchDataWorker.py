from services.binanceDataService import fetchData as fetchBinanceData 
from models.brokerData import BrokerData

import threading

def start(timeout: int, brokerData: BrokerData):
    brokerData.binanceData = fetchBinanceData()
    #brokerData.commexData = ....

    print(brokerData.binanceData)

    threading.Timer(timeout, start, [timeout, brokerData]).start()
    
