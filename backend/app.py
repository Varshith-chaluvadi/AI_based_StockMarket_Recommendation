from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Stock Market Analysis Backend Running Successfully 🚀"

@app.route('/api/test')
def test_api():
    data = {
        "project": "AI Stock Market Analysis System",
        "status": "Backend API Working",
        "version": "1.0"
    }
    return jsonify(data)

@app.route('/api/stock/<symbol>')
def get_stock(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    data = {
        "symbol": symbol.upper(),
        "company": info.get("longName"),
        "currentPrice": info.get("currentPrice"),
        "marketCap": info.get("marketCap"),
        "currency": info.get("currency")
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)