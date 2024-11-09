# api documentation
# https://python-binance.readthedocs.io/en/latest/binance.html
# https://binance-docs.github.io/apidocs/futures/en/#change-log

from binance.client import Client
import config
import csv

client = Client(config.api_key, config.api_secret)

prices = client.get_all_tickers()

# for price in prices:
#     print(price)


## 15 min candlestick
candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csv_file = open('15min.csv', 'w', newline='')
candlestick_writer = csv.writer(csv_file, delimiter=',')

for candlestick in candles:
    candlestick_writer.writerow(candlestick)

csv_file.close()
print(len(candles))

## historical candlestick every 5 mins for the interval
candles = client.get_historical_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_5MINUTE, start_str="1 Jan, 2017", end_str="1 Jan, 2018")

csv_file = open('2017to20185min.csv', 'w', newline='')
candlestick_writer = csv.writer(csv_file, delimiter=',')

for candlestick in candles:
    candlestick_writer.writerow(candlestick)

csv_file.close()
print(len(candles))