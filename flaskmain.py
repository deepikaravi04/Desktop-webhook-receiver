from flask import Flask, request

app = Flask(__name__)

# Route to handle incoming webhook requests
@app.route('/desktop_webhook', methods=['POST'])
def handle_webhook():
    # Extract the payload from the incoming request
    payload = request.json
    print(payload.get("symbol"))
    print(payload.get("action"))

    # Process the payload (replace this with your own logic)
    print("Received webhook payload:", payload)

    # Respond with a success message
    return 'Webhook received successfully', 200

if __name__ == '__main__':
    app.run(port=8000)
