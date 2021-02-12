import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

share = pdr.get_data_yahoo('TSLA', start = dt.datetime(2017,1,1), end = dt.datetime.today())
share['100ma'] = share['Adj Close'].rolling(window=100, min_periods=0).mean()

print(share.head())
print("--------------------------------------------------------------------")

print(share.tail(10))
print("--------------------------------------------------------------------")

last10days = share['Adj Close'].tail(10)
print(last10days)
print("--------------------------------------------------------------------")

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)

ax1.plot(share.index, share['Adj Close'])
ax1.plot(share.index, share['100ma'])
ax2.bar(share.index, share['Volume'])
plt.show()

#ax1 = plt.

#last10days = share['Adj Close'].plot()
#plt.show(last10days)

#last10days = share['High'].tail(10).plot(grid=True)
#plt.show(last10days)