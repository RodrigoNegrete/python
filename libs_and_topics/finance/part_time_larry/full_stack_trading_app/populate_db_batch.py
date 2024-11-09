# pip install alpaca-trade-api
import sqlite3
import alpaca-trade-api as tradeapi

connection = sqlite3.connect('./part_time_larry/full_stack_trading_app/app.db')

cursor = connection.cursor()

# populate by batch
api = tradeapi.REST('api_key', 'api_secret', base_url='https://paper-api.alpaca.markets')
assets = api.list_assets()

## loop through assets and insert
# for asset in assets:
#     cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))

## troubleshoot exceptions
# for asset in assets:
#     try:
#         cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
#     except Exception as e:
#         print(asset.symbol)
#         print(e)

# we identify a bunch of duplicates and select VXX to be printed
# for asset in assets:
#     if symbol == 'VXX':
#     print(asset)

## we identify that there´s a column 'status' which can be active or inactive
## we rewrite the loop to filter status inactive
## we also identify a 'tradable' column and we filter that too
for asset in assets:
    if asset.status == 'active' and asset.tradable == 'True':
        cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))

connection.commit()

