import pandas as pd
import matplotlib.pyplot as plt

# Load the data
column_names = ['Date', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
data = pd.read_csv('rivian_stock_data.csv', skiprows=3, names=column_names)

# Set 'Date' as the index and convert it to datetime
data.set_index('Date', inplace=True)
data.index = pd.to_datetime(data.index)

# Plot the historical closing prices
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Historical Closing Price of Rivian Stock')
plt.legend()
plt.savefig('historical_prices.png')
print("Historical prices plot saved as 'historical_prices.png'")
