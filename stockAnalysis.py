import yfinance as yf
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import locale 
import pytz

# Define the stock symbol
symbol = "PHK"  # Replace with your desired stock symbol

# Retrieve dividend data from Yahoo Finance
stock = yf.Ticker(symbol)
dividends = stock.dividends
dividends = dividends.to_frame()
divDate = dividends.index = dividends.index.astype(str)

# Slice the index to include only the left 10 characters
divDate = [index[:10] for index in divDate]
dividends['payDate'] = divDate

# Write Dividend data to a spreadsheet
with pd.ExcelWriter('dividends.xlsx') as writer:
    dividends.to_excel(writer, sheet_name="Dividends",index=False)