from flask import Flask, request

app = Flask(__name__)
from ib_insync import *

# Connect to IB TWS/IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Update host and port if necessary
print("hello")
ib.disconnect()

# Route to handle incoming webhook requests
@app.route('/desktop_webhook', methods=['POST'])
def handle_webhook():
    # Extract the payload from the incoming request
    payload = request.json
    print(payload.get("symbol"))
    print(payload.get("action"))
    # Define contract details
    contract = Stock(symbol=payload.get("symbol"), exchange='SMART', currency='USD')  # Replace with the symbol of the instrument you want to trade

    # Create a market order
    order = MarketOrder(payload.get("action").upper(), totalQuantity=1)  # BUY or SELL and specify quantity
    # Place the order
    trade = ib.placeOrder(contract, order)

    # Confirm order placement
    # print(trade)
    # Process the payload (replace this with your own logic)
    print("Received webhook payload:", payload)

    # Respond with a success message    
    return 'Webhook received successfully', 200

if __name__ == '__main__':
    app.run(port=8000)
