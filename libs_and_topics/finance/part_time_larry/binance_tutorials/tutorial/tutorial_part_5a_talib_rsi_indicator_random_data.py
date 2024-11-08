# ta-lib documentation
# https://github.com/mrjbq7/ta-lib

import talib
import numpy

# generate random array
close = numpy.random.random(100)
print(close)

# SMA - simple moving average
# moving average gets the last 30 elements by default, that´s why there are nan values 
moving_average = talib.SMA(close)
print(moving_average)

# get 10 day SMA
moving_average = talib.SMA(close, timeperiod=10)
print(moving_average)

# RSI
rsi = talib.RSI(close)
print(rsi)