

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
# divDateFormat = divDate.dt.tz.convert(pytz.UTC).dt.tz_localize(None)

# Slice the index to include only the left 10 characters
divDate = [index[:10] for index in divDate]
dividends['payDate'] = divDate


# Step 1: Remove the column you want to exclude
# dividends = dividends.drop('', axis=1)

# Step 2: Reorder the remaining two columns
# df = df[['B', 'A']]  # Adjust the column order as desired


# dividends['Dividends'] = dividends['Dividends'].dt.tz_convert(pytz.UTC).dt.tz_localize(None)

# dividends['Dividends'] = dividends['Dividends'].astype(str)
# dividends['Left'] = dividends['Dividends'].str.slice(stop=2)
# dividends['Right'] = dividends['Dividends'].str.slice(stop=20)
# print(dividends['Right'])


# dividends['Left'] = dividends['Dividends'].str.slice(stop=10)
# print(dividends['Left'])

# Display dividend payment history
# if len(dividends) > 0:
#     print("Dividend Payment History:")
#     print(dividends)
# else:
#     print("No dividend payment history available for the specified symbol.")


# # Convert datetime column to timezone-unaware format

with pd.ExcelWriter('dividends.xlsx') as writer:
    dividends.to_excel(writer, sheet_name="Dividends",index=False)