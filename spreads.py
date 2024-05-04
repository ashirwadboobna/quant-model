import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the payoff of a call option
def call_payoff(strike_price, stock_prices, premium):
    return np.maximum(stock_prices - strike_price, 0) - premium

# Function to calculate the payoff of a put option
def put_payoff(strike_price, stock_prices, premium):
    return np.maximum(strike_price - stock_prices, 0) - premium

# Define option parameters
stock_prices = np.linspace(50, 150, 100)  # Example stock prices at expiration
strike1 = 100  # Lower strike
strike2 = 110  # Higher strike
call_premium1 = 5
call_premium2 = 3
put_premium1 = 4
put_premium2 = 6

# Bull Call Spread: Buy lower strike call, Sell higher strike call
bull_call_long = call_payoff(strike1, stock_prices, call_premium1)
bull_call_short = -call_payoff(strike2, stock_prices, call_premium2)
bull_call_spread = bull_call_long + bull_call_short

# Bear Put Spread: Buy higher strike put, Sell lower strike put
bear_put_long = put_payoff(strike2, stock_prices, put_premium2)
bear_put_short = -put_payoff(strike1, stock_prices, put_premium1)
bear_put_spread = bear_put_long + bear_put_short

# Straddle: Buy both a call and a put with the same strike
straddle_call = call_payoff(strike1, stock_prices, call_premium1)
straddle_put = put_payoff(strike1, stock_prices, put_premium1)
straddle = straddle_call + straddle_put

# Collar: Buy a lower strike put and sell a higher strike call
collar_put = put_payoff(strike1, stock_prices, put_premium1)
collar_call = -call_payoff(strike2, stock_prices, call_premium2)
collar = collar_put + collar_call

# Plot the payoffs
fig, ax = plt.subplots(2, 2, figsize=(12, 10))
ax[0, 0].plot(stock_prices, bull_call_spread, label='Bull Call Spread')
ax[0, 0].legend()
ax[0, 0].grid(True)
ax[0, 0].set_title('Bull Call Spread')
ax[0, 0].set_xlabel('Stock Price at Expiration')
ax[0, 0].set_ylabel('Profit / Loss')

ax[0, 1].plot(stock_prices, bear_put_spread, label='Bear Put Spread', color='red')
ax[0, 1].legend()
ax[0, 1].grid(True)
ax[0, 1].set_title('Bear Put Spread')
ax[0, 1].set_xlabel('Stock Price at Expiration')
ax[0, 1].set_ylabel('Profit / Loss')

ax[1, 0].plot(stock_prices, straddle, label='Straddle', color='green')
ax[1, 0].legend()
ax[1, 0].grid(True)
ax[1, 0].set_title('Straddle')
ax[1, 0].set_xlabel('Stock Price at Expiration')
ax[1, 0].set_ylabel('Profit / Loss')

ax[1, 1].plot(stock_prices, collar, label='Collar', color='orange')
ax[1, 1].legend()
ax[1, 1].grid(True)
ax[1, 1].set_title('Collar')
ax[1, 1].set_xlabel('Stock Price at Expiration')
ax[1, 1].set_ylabel('Profit / Loss')

plt.tight_layout()
plt.show()
