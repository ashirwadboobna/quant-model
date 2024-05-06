import matplotlib.pyplot as plt
import numpy as np

# Function to calculate intrinsic value of a call option (without premium)
def intrinsic_value(spot_price, strike_price):
    return np.maximum(spot_price - strike_price, 0)

# Function to calculate the payoff of a long call (with premium)
def long_call_payoff(spot_price, strike_price, premium):
    return intrinsic_value(spot_price, strike_price) - premium

# Function to calculate the payoff of a short call (with premium)
def short_call_payoff(spot_price, strike_price, premium):
    return premium - intrinsic_value(spot_price, strike_price)

# Function to create subplots for long and short call options, with intrinsic value indicated
def plot_long_and_short_call(strike_price, premium, spot_range=(0, 100)):
    spot_prices = np.linspace(spot_range[0], spot_range[1], 100)

    # Calculate intrinsic value and payoffs for long and short calls
    intrinsic = intrinsic_value(spot_prices, strike_price)
    long_call = long_call_payoff(spot_prices, strike_price, premium)
    short_call = short_call_payoff(spot_prices, strike_price, premium)
    short_intrinsic = -intrinsic  # Reverse of intrinsic for the short call

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    fig.suptitle('Long Call and Short Call Strategies')

    # Long Call subplot
    ax1.plot(spot_prices, intrinsic, 'b--', label='Intrinsic Value')
    ax1.plot(spot_prices, long_call, 'b', label='Long Call Payoff')
    ax1.axhline(0, color='black', linewidth=0.5)
    ax1.axvline(strike_price, color='gray', linestyle='--')
    ax1.set_title('Long Call Strategy')
    ax1.set_xlabel('XYZ Stock Price')
    ax1.set_ylabel('Profit/Loss')
    ax1.legend()
    ax1.grid(True)

    # Short Call subplot
    ax2.plot(spot_prices, short_intrinsic, 'b--', label='Intrinsic Value (Reversed)')
    ax2.plot(spot_prices, short_call, 'r', label='Short Call Payoff')
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(strike_price, color='gray', linestyle='--')
    ax2.set_title('Short Call Strategy')
    ax2.set_xlabel('XYZ Stock Price')
    ax2.set_ylabel('Profit/Loss')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Example usage: Define strike price, premium, and stock price range
strike_price = 50  # Example strike price for the long and short call
premium = 6.26  # Example premium based on the image provided
spot_range = (30, 70)  # Stock price range around the strike price

# Plot the graphs
plot_long_and_short_call(strike_price, premium, spot_range)

