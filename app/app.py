from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "HOLA DESDE RENDER, Y AWS 25/04/2025 !!!!!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)