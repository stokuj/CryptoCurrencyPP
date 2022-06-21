import pandas as pd

import datetime as dt

from pandas import Series,DataFrame

import pandas_datareader.data as web

crypto_currency     = 'BTC'
against_currency    = 'USD'
data_source         = 'yahoo'
start = dt.datetime(2016,1,1)
end = dt.datetime.now()

df = web.DataReader(f'{crypto_currency}-{against_currency}', data_source, start, end)
df.to_csv("test.csv")
