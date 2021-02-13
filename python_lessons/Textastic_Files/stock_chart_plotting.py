import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt

share = pdr.get_data_yahoo('AAPL', start=dt.datetime(2015,1,1), end=dt.datetime.today())

print(share.head())
print("----------------------------------------------")

print(share.tail(10))
print("----------------------------------------------")

last10days = share['Adj Close']
print(last10days.tail(10))
print("----------------------------------------------")

print(last10days.tail(10).plot())
