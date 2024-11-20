import yfinance as yf
import pandas as pd

# Download Rivian stock data
rivian_data = yf.download('RIVN', start='2022-01-01', end='2023-11-01')

# Save to CSV
rivian_data.to_csv('rivian_stock_data.csv')

# Print the first few rows
print(rivian_data.head())
