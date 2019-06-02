# This program calculates the pip value given a trade

class Trade(object):
    NOTYPE = 0
    SHORT = 1
    LONG = 2
    currencyPair = ['EUR','USD'] # first element is Base Currency
    entryPrice = 1.3631   # BID price is rate at which the broker is willing to pay for the currency pair - i.e. your selling price
    exitPrice = 1.3681   # ASK price is the rate at which the broker is willing to sell - i.e. your buy price
    numberOfUnits = 100000 # number of units in the trade - 100000 is a standard lot
    tradeType = NOTYPE #or LONG
    pips = 0

    def __init__(self, baseCurrency, quoteCurrency, entry, type, units):
        self.currencyPair[0] = baseCurrency
        self.currencyPair[1] = quoteCurrency
        self.entryPrice = entry
        self.numberOfUnits = units
        if type in (Trade.LONG, Trade.SHORT):
            self.tradeType = type
        else:
            self.tradeType = Trade.NOTYPE


    def exit(self, exit):
        self.exitPrice = exit

    # Calculates the Pip value to our account currency whoch may not be the currencies being traded
    # Eg. we may trade 'EUR/USD' but our account currency could be AUD.
    # Using this function reuqires the exchannge rate between USD to AUD
    def calculateProfitLossHomeCurrency(self, homeCurrencyCode):

        homeAmtPerPip = self.calculatePipValue(homeCurrencyCode)

        if (self.tradeType == self.SHORT):
            pips = round(10000*(self.entryPrice - self.exitPrice))
        elif (self.tradeType == self.LONG):
            pips = round(10000*(self.exitPrice - self.entryPrice))
        else:
            pips = 0
        print(f"Pips: {pips}")
        return pips * homeAmtPerPip

    def calculatePipValue(self, homeCurrencyCode):
        # currently hardcoded, but exchange rate should be obtained from online later
        if homeCurrencyCode=='AUD':
            # exchange rate should be based on amount of home currency to $1 base currency of trade
            exchRateToHomeCurrency = 0.69348
        else:
            # Default to USD home currency
            exchRateToHomeCurrency = 1.000000

        quoteAmtPerPip = self.numberOfUnits * 0.0001
        homeAmtPerPip = quoteAmtPerPip / exchRateToHomeCurrency

        return homeAmtPerPip

    def getTradeTypeName(self, tradeTypeCode):
        if tradeTypeCode==self.LONG:
            return 'LONG'
        elif tradeTypeCode==self.SHORT:
            return 'SHORT'
        else:
            return 'NOTYPE (Error)'

####### Program Starts Here ########

newTrade = Trade('USD','AUD',0.69311, Trade.LONG, 100000)

exPrice = input("Please enter exit price: ")
newTrade.exit(float(exPrice))
print(f"Trade Details: {newTrade.currencyPair}, {newTrade.entryPrice}, {newTrade.exitPrice}, {newTrade.numberOfUnits}, {newTrade.getTradeTypeName(newTrade.tradeType)}")
print(f"Pip Value in Home Currency (AUD) is: {round(newTrade.calculatePipValue('AUD'),2)}")
print(f"Profit in home currency is: {round(newTrade.calculateProfitLossHomeCurrency('AUD'),2)}")
