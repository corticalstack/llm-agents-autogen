# filename: stock_data_plot.py

import yfinance as yf
import matplotlib.pyplot as plt

# Set the period for YTD 2024
start_date = '2024-01-01'
end_date = '2024-12-10'

# Download stock data for NVIDIA and Tesla
nvda_data = yf.download('NVDA', start=start_date, end=end_date)
tsla_data = yf.download('TSLA', start=start_date, end=end_date)

# Create a figure and plot both datasets
plt.figure(figsize=(10, 5))
plt.plot(nvda_data['Close'], label='NVDA Closing Price')
plt.plot(tsla_data['Close'], label='TSLA Closing Price')
plt.title('NVIDIA and Tesla Stock Prices YTD 2024')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()

# Save the figure
plt.savefig('stock_prices_YTD_plot.png')
plt.show()