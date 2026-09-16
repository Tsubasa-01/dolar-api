from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def dolar():
    try:
        r = requests.get('https://api.frankfurter.app/latest?from=USD&to=PEN', timeout=10).json()
        return jsonify({"compra": r['rates']['PEN'], "venta": r['rates']['PEN'], "fuente": "frankfurter"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
