# Stock Price Prediction Project

## Introduction
I've been a bit obsessed with Rivian stock and was really curious about its trends. So, I decided to build this project for fun to explore AI and see if I could create a simple prediction model. It’s a machine learning-based approach that fetches historical stock data, processes it, trains a model, and visualizes predictions.

## How It Works
The project follows these steps:
1. **Fetch Data** - Collect historical stock prices.
2. **Preprocess Data** - Clean and prepare it for training.
3. **Train Model** - Use a simple Linear Regression model to predict prices.
4. **Visualize Results** - Compare actual vs. predicted stock prices.

## Tools & Libraries Used
- **Python** - The programming language for everything.
- **pandas** - Handles and processes stock data.
- **numpy** - Helps with numerical calculations.
- **scikit-learn** - Used to train the Linear Regression model.
- **matplotlib** - Creates visualizations of stock prices.
- **pickle** - Saves and loads the trained model.

## Project Structure
- `fetch_data.py` - Retrieves stock price data.
- `preprocess_data.py` - Cleans and processes the data.
- `train_model.py` - Trains a simple Linear Regression model.
- `visualize_data.py` - Generates plots for actual vs. predicted prices.
- `rivian_stock_data.csv` - The dataset used for training.
- `linear_regression_model.pkl` - The saved trained model.
- `requirements.txt` - Lists the required dependencies.

## Running the Project
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Fetch stock data:
   ```sh
   python fetch_data.py
   ```
3. Preprocess the data:
   ```sh
   python preprocess_data.py
   ```
4. Train the model:
   ```sh
   python train_model.py
   ```
5. Visualize predictions:
   ```sh
   python visualize_data.py
   ```

## Why I Built This
I’ve been following Rivian stock for a while and got curious about predicting its price movements. So, I used this as an opportunity to dive into AI and machine learning. It was a fun challenge to see how well a simple model could perform!

## Author
Srivathsav Velpuri

