import yfinance as yf
import pandas as pd
import datetime as dt

var = yf.Ticker('KO')
print(var.dividends)
