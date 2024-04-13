from pyngrok import ngrok


# Set up a HTTP tunnel on port 8000
public_url = ngrok.connect(8000, "http")

print("Public URL:", public_url)
# Keep the tunnel open until interrupted
try:
    input("Press Enter to exit...")
except KeyboardInterrupt:
    ngrok.disconnect(public_url)
