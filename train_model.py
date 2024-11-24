import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load the preprocessed data
column_names = ['Date', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
data = pd.read_csv('rivian_stock_data.csv', skiprows=3, names=column_names)

# Set 'Date' as the index and convert it to datetime
data.set_index('Date', inplace=True)
data.index = pd.to_datetime(data.index)

# Add features
data['Prev Close'] = data['Close'].shift(1)
data['5-day MA'] = data['Close'].rolling(window=5).mean()
data['Daily Return'] = data['Close'].pct_change()

# Drop rows with NaN values
data = data.dropna()

# Define features (X) and target (y)
X = data[['Prev Close', '5-day MA', 'Daily Return']]
y = data['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Plot the results and save as an image
plt.scatter(y_test, y_pred, color='blue', label='Predicted Prices')
plt.scatter(y_test, y_test, color='green', label='Actual Prices')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs. Predicted Stock Prices")
plt.legend()  # Add legend to differentiate actual and predicted points
plt.savefig('actual_vs_predicted_colored.png')  # Save the plot as an image
print("Plot saved as 'actual_vs_predicted_colored.png'")


# Save the model for future use
import joblib
joblib.dump(model, 'linear_regression_model.pkl')
