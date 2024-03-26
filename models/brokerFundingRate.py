class BrokerFundingRate:
    def __init__(self, broker, symbol, fundingRate, fundingRateExpirationDateTime, markPrice):
        self.broker = broker
        self.symbol = symbol
        self.fundingRate = fundingRate
        self.fundingRateExpirationDateTime = fundingRateExpirationDateTime
        self.markPrice = markPrice
