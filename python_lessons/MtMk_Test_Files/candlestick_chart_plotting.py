import pandas_datareader as pdr
import pandas as pd
import datetime as dt
import plotly.graph_objects as go

start = dt.datetime(2015,1,1)
end = dt.datetime.today()

share_aapl = pdr.get_data_yahoo('AAPL', start = start, end = end)

df = share_aapl

figure = go.Figure(
	data = [
		go.Candlestick(
			x = df.index,
			low = df['Low'],
			high = df['High'],
			close = df['Close'],
			open = df['Open'],
			increasing_line_color = 'green',
			decreasing_line_color = 'red'
			)
	]
)
figure.show()