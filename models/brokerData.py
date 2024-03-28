from models.bunch import Bunch


class BrokerData:
    binanceData: dict[str, object]
    commexData: dict[str, object]
    bitgetData: dict[str, object]
    bybitData: dict[str, object]
    gateioData: dict[str, object]
    mexcData: dict[str, object]
    coinexData: dict[str, object]
    poloniexData: dict[str, object]
    kucoinData: dict[str, object]
    okxData: dict[str, object]
    bitmartData: dict[str, object]
    bunches: list[Bunch]
