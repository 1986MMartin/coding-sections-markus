import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt

aapl = pdr.get_data_yahoo('AAPL', start=dt.datetime(2006,10,1), end=dt.datetime.today())

print(aapl.head())
print(aapl.tail(10))
