class Bunch:
    
    def __init__(self, 
                symbol, 
                shortBroker, 
                shortFundingRate, 
                shortFundingRateExpirationDateTime, 
                shortMarkPrice,
                longBroker, 
                longFundingRate, 
                longFundingRateExpirationDateTime, 
                longMarkPrice,
                priceSpread,
                fundingSpread):
        self.symbol = symbol
        self.shortBroker = shortBroker
        self.shortFundingRate = shortFundingRate
        self.shortFundingRateExpirationDateTime = shortFundingRateExpirationDateTime
        self.shortMarkPrice = shortMarkPrice
        self.longBroker = longBroker
        self.longFundingRate = longFundingRate
        self.longFundingRateExpirationDateTime = longFundingRateExpirationDateTime
        self.longMarkPrice = longMarkPrice
        self.priceSpread = priceSpread
        self.fundingSpread = fundingSpread

    def getButtonLabel(self):
        return self.symbol + ": от " + str(self.fundingSpread * 100)



