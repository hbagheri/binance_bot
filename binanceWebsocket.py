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

# Instantiate a BinanceSocketManager, passing in the client that you instantiated
bm = BinanceSocketManager(client,user_timeout=10)

# This is our callback function. For now, it just prints messages as they come.
def handle_message(msg):
    print(msg)

# Start trade socket with 'ETHBTC' and use handle_message to.. handle the message.
conn_key = bm.start_trade_socket('BTCUSDT', handle_message)
# then start the socket manager
bm.start()

# let some data flow..
time.sleep(100)

# stop the socket manager
bm.stop_socket(conn_key)
