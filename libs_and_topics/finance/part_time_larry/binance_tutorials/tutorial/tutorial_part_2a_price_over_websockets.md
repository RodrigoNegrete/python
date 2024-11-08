# connect to wscat for bitcoin and "trade method"
# run on terminal
wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade
# result
{"e":"trade","E":1623082284258,"s":"BTCUSDT","t":895012545,"p":"36042.82000000","q":"0.00037900","b":6348773535,"a":6348773545,"T":1623082284257,"m":true,"M":true}

# you can check the timestamps at unixtimestamp.com

# get candlestick line for 5 mins for bitcoin
wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m
# result
{"e":"kline","E":1623082595213,"s":"BTCUSDT","k":{"t":1623082500000,"T":1623082799999,"s":"BTCUSDT","i":"5m","f":895015855,"L":895017111,"o":"35945.39000000","c":"35986.00000000","h":"35990.73000000","l":"35928.00000000","v":"66.97808600","n":1257,"x":false,"q":"2408073.23320454","V":"40.12095200","Q":"1442593.55078514","B":"0"}}

# save result to file
example 1
wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee ./part_time_larry/binance_tutorials/dataset.text
example 2
wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee dataset.text