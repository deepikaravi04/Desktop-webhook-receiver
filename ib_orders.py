from ib_insync import *

# Connect to IB TWS/IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Update host and port if necessary

# Define contract details
contract = Stock(symbol='AAPL', exchange='SMART', currency='USD')  # Replace with the symbol of the instrument you want to trade

# Create a market order
order = MarketOrder('BUY', totalQuantity=1)  # BUY or SELL and specify quantity

# Place the order
trade = ib.placeOrder(contract, order)

# Confirm order placement
print(trade)

# Disconnect from IB TWS/IB Gateway
ib.disconnect()
