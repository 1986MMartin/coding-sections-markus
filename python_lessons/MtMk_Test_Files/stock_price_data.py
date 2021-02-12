# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:55:57 2020

@author: Markus Martin
"""

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as style

style.use('pdf')

start = dt.datetime(2010, 1, 1)
end = dt.datetime.today()

df = web.DataReader('AAPL', 'yahoo', start, end)
print(df.head())
print(df.index)

