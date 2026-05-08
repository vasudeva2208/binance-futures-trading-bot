from binance.client import Client
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

client = Client(API_KEY, API_SECRET)

# Binance Futures Testnet URL
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# Sync local time with Binance server
server_time = client.get_server_time()
system_time = int(time.time() * 1000)

client.timestamp_offset = server_time['serverTime'] - system_time