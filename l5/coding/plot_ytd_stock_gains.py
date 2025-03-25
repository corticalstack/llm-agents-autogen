# filename: plot_ytd_stock_gains.py

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Set the current date and the beginning of the year
current_date = "2024-12-10"
start_date = "2024-01-01"

# Fetch stock data
stock_symbols = ['NVDA', 'TSLA']
stocks = yf.download(stock_symbols, start=start_date, end=current_date)

# Assuming stock data includes 'Adj Close', calculate the percentage gain
ytd_gains = (stocks['Adj Close'].iloc[-1] / stocks['Adj Close'].iloc[0] - 1) * 100

# Plotting
plt.figure(figsize=(10, 6))
ytd_gains.plot(kind='bar', color=['green', 'blue'])
plt.title('YTD Stock Gains for NVDA and TSLA')
plt.ylabel('Percentage Gain (%)')
plt.xlabel('Stock')
plt.xticks(rotation=0)
plt.grid(True)

# Save the figure
plt.savefig('ytd_stock_gains.png')
plt.show()