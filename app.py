from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "per_page": 10,
        "page": 1
    }

    data = requests.get(url, params=params).json()

    return render_template("index.html", coins=data)

if __name__ == "__main__":
    app.run(debug=True)