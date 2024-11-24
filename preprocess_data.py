import pandas as pd
from sklearn.model_selection import train_test_split

# Manually specify column names to align with data
column_names = ['Date', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']

# Load the data, skipping the first three rows
data = pd.read_csv('rivian_stock_data.csv', skiprows=3, names=column_names)

# Set 'Date' as the index and convert it to datetime
data.set_index('Date', inplace=True)
data.index = pd.to_datetime(data.index)

# Trim the dataset to focus only on recent data (e.g., from July 2022 onwards)
data = data[data.index >= '2022-07-01']

# Print columns for debugging
print("Columns in the DataFrame:", data.columns)

# Add new features
data['Prev Close'] = data['Close'].shift(1)
data['5-day MA'] = data['Close'].rolling(window=5).mean()
data['Daily Return'] = data['Close'].pct_change()

# Drop rows with NaN values
data = data.dropna()

# Features (X) and target (y)
X = data[['Prev Close', '5-day MA', 'Daily Return']]
y = data['Close']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print shapes of the datasets
print(f"Training data size: {len(X_train)}")
print(f"Testing data size: {len(X_test)}")

# Print summary statistics of the 'Close' column
print("Summary statistics of Close price column:")
print(data['Close'].describe())
