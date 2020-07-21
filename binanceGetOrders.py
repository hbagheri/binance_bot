#!/media/hassan/MyData/python/binance_old/Binance/bin/python3.7 
from binance.client import Client # Import the Binance Client
from binance.websockets import BinanceSocketManager # Import the Binance Socket Manager
from datetime import datetime
import time

# Although fine for tutorial purposes, your API Keys should never be placed directly in the script like below. 
# You should use a config file (cfg or yaml) to store them and reference when needed.
PUBLIC = 'O0YToIRWZm9kh0RUwkIPIkYNcQ2kFsFVpWc30AygzrvrdoMTgta9AFlpc8Ofwkr3'
SECRET = '3BaK72PQqadzW6nMyRHBGWA3nlcDQb886x7toZQCY1ipHz8YqzyLcwLuupXq6jHi'

# Instantiate a Client 
client = Client(api_key=PUBLIC, api_secret=SECRET)

#orders = client.get_all_orders(symbol='BTCUSDT', requests_params={'timeout': 5})
#depth = client.get_order_book(symbol='BTCUSDT')
#trades = client.get_recent_trades(symbol='BTCUSDT')
#trades = client.get_historical_trades(symbol='BNBBTC')
#candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_30MINUTE)
orders = client.get_open_orders(symbol='BTCUSDT')
#balance = client.get_asset_balance(asset='BNB')

print (orders)
orders = client.get_all_orders(symbol='BTCUSDT', limit=3000)
totalBtc=0.01+0.00899082+0.0425
cummulativeQuoteQty=45.45+80+140.84+188+163.5+410.360926
exchange=0
totalBitTrade=0
#print (orders)
for order in orders:
    if order['status'] == 'FILLED':
        if(order['side'] == 'SELL'):
            sign = 1
        else:
            sign = -1
        totalBtc +=  sign*float(order['executedQty'])
        cummulativeQuoteQty += sign*float(order['cummulativeQuoteQty'])
        exchange += float(order['executedQty']) * 0.00097 *float( order['price'])
        totalBitTrade +=float(order['executedQty'])
        print("symbol:{} | price:{} | Value:{} | cust:{} | {} | frunshit:{} |".format(order['symbol'],
                                                     order['price'],
                                                     order['executedQty'],
                                                     sign * float(order['cummulativeQuoteQty']),
                                                     order['side'],
                                                     float(order['executedQty']) * 0.00075 *float( order['price'])
                                                     ))
                                                     
print("Totall BTC:{},ern:{} {}".format(totalBtc,cummulativeQuoteQty,totalBitTrade))
