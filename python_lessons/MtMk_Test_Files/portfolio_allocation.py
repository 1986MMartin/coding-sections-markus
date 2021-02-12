import pandas_datareader as pdr
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2020,1,1)
end = dt.datetime.today()

share_aapl = pdr.get_data_yahoo('AAPL', start = start, end = end)
share_atvi = pdr.get_data_yahoo('ATVI', start = start, end = end)
share_fb = pdr.get_data_yahoo('FB', start = start, end = end)
share_msft = pdr.get_data_yahoo('MSFT', start = start, end = end)
share_v = pdr.get_data_yahoo('V', start = start, end = end)

for stock_df in (share_aapl, share_atvi, share_fb, share_msft, share_v):
	stock_df['Normed Return'] = stock_df['Adj Close']/stock_df.iloc[0]['Adj Close']

for stock_df, allo in zip([share_aapl, share_atvi, share_fb, share_msft, share_v],[0.2,0.2,0.2,0.2,0.2]):
	stock_df['Allocation'] = stock_df['Normed Return']*allo

for stock_df in (share_aapl, share_atvi, share_fb, share_msft, share_v):
	stock_df['Position Value'] = stock_df['Allocation']*1500

print("---------------------------------------------------------------------------")

print("Share: AAPL")
print(share_aapl['Position Value'].tail(1)) 
print("---------------------------------------------------------------------------")

print("Share: ATVI")
print(share_atvi['Position Value'].tail(1)) 
print("---------------------------------------------------------------------------")

print("Share: FB")
print(share_fb['Position Value'].tail(1)) 
print("---------------------------------------------------------------------------")

print("Share: MSFT")
print(share_msft['Position Value'].tail(1)) 
print("---------------------------------------------------------------------------")

print("Share: V")
print(share_v['Position Value'].tail(1)) 
print("---------------------------------------------------------------------------")

print("Portfolio Sum:")
print(share_aapl['Position Value'].tail(1)+share_atvi['Position Value'].tail(1)+share_fb['Position Value'].tail(1)+share_msft['Position Value'].tail(1)+share_v['Position Value'].tail(1))
print("---------------------------------------------------------------------------")
