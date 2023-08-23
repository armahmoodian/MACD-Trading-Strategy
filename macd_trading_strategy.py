import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib

# Get user input for stock symbol and time frame
stock_symbol = input("Enter the stock symbol (e.g., AAPL): ")
time_frame = input("Enter the time frame (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Fetch historical data using yfinance
data = yf.download(stock_symbol, start=start_date, end=end_date, interval=time_frame)

# Calculate MACD
data['MACD'], data['Signal'], _ = talib.MACD(data['Close'], fastperiod=96, slowperiod=208, signalperiod=9)

# Calculate crossover signals
data['Crossover'] = np.where(data['MACD'] > data['Signal'], 1, -1)

# Trading strategy based on MACD crossovers
current_position = 'None'
trades = []

for index, row in data.iterrows():
    if row['Crossover'] == 1 and current_position != 'Buy':
        current_position = 'Buy'
        trades.append('Buy')
    elif row['Crossover'] == -1 and current_position != 'Sell':
        current_position = 'Sell'
        trades.append('Sell')
    else:
        trades.append('Hold')

data['Trade'] = trades

# Drop rows with missing data
data.dropna(subset=['Close', 'Trade'], inplace=True)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Price')
plt.scatter(data[data['Trade'] == 'Buy'].index, data[data['Trade'] == 'Buy']['Close'],
            marker='^', color='g', label='Buy', linewidths=3)
plt.scatter(data[data['Trade'] == 'Sell'].index, data[data['Trade'] == 'Sell']['Close'],
            marker='v', color='r', label='Sell', linewidths=3)
plt.title(f'MACD Crossover Based Trade Suggestions for {stock_symbol} ({time_frame})')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
