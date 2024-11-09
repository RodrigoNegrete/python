# ta-lib documentation
# https://github.com/mrjbq7/ta-lib

import talib
import numpy

# read data
my_data = numpy.genfromtxt('15min.csv', delimiter=',')
print(my_data)

# get closing price which if the fourth index
close = my_data[:,4]
print(close)

# RSI - relative strength index
rsi = talib.RSI(close)
print(rsi)