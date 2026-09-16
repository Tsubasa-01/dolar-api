import requests
print("=== DOLAR HOY EN PERU ===")
r = requests.get("https://open.er-api.com/v6/latest/USD", timeout=10)
precio = r.json()['rates']['PEN']
print(f"1 Dólar = {precio} Soles")
print(f"10 Dólares = {precio*10:.2f} soles")
print(f"100 Dólares = {precio*100:.2f} soles")
