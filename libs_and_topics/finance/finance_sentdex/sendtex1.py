import datetime as dt
import matplotlib.pyplot as pyplot
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2015,1,1)
end = dt.datetime(2020,1,1)

df = web.DataReader('TSLA', 'yahoo', start, end)

## print a number of records passed as argument
# print(df.head(5))

df.to_csv('tesla.csv')
