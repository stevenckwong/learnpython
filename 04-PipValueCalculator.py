import ForexModule

newTrade = ForexModule.Trade('USD', 'AUD', 0.69311, ForexModule.Trade.LONG, 100000)

exPrice = input("Please enter exit price: ")
newTrade.exit(float(exPrice))
print(f"Trade Details: {newTrade.currencyPair}, {newTrade.entryPrice}, {newTrade.exitPrice}, {newTrade.numberOfUnits}, {newTrade.getTradeTypeName(newTrade.tradeType)}")
print(f"Pip Value in Home Currency (AUD) is: {round(newTrade.calculatePipValue('AUD'),2)}")
print(f"Profit in home currency is: {round(newTrade.calculateProfitLossHomeCurrency('AUD'),2)}")
