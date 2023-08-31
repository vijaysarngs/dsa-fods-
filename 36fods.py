import pandas as pd
import numpy as np
data = pd.read_csv("C:/Users/vijay/OneDrive/Documents/stock_data.csv")
closing_prices = data['closing_price']

daily_returns = closing_prices.pct_change()

mean_return = np.mean(daily_returns)
std_deviation = np.std(daily_returns)

annualized_volatility = std_deviation * np.sqrt(252)

print(f"Mean Daily Return: {mean_return:.4f}")
print(f"Standard Deviation of Daily Returns: {std_deviation:.4f}")
print(f"Annualized Volatility: {annualized_volatility:.4f}")

if mean_return > 0:
    print("The stock tends to have positive average daily returns.")
else:
    print("The stock tends to have negative or near-zero average daily returns.")

if annualized_volatility < 0.2:
    print("The stock's volatility is relatively low.")
elif 0.2 <= annualized_volatility < 0.4:
    print("The stock's volatility is moderate.")
else:
    print("The stock's volatility is relatively high.")
