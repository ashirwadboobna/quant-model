import matplotlib.pyplot as plt
import numpy as np

# Function to calculate intrinsic value of a put option (without premium)
def intrinsic_value_put(spot_price, strike_price):
    return np.maximum(strike_price - spot_price, 0)

# Function to calculate the payoff of a long put (with premium)
def long_put_payoff(spot_price, strike_price, premium):
    return intrinsic_value_put(spot_price, strike_price) - premium

# Function to calculate the payoff of a short put (with premium)
def short_put_payoff(spot_price, strike_price, premium):
    return premium - intrinsic_value_put(spot_price, strike_price)

# Function to create subplots for long and short put options, with intrinsic value indicated
def plot_long_and_short_put(strike_price, premium, spot_range=(0, 100)):
    spot_prices = np.linspace(spot_range[0], spot_range[1], 100)

    # Calculate intrinsic value and payoffs for long and short puts
    intrinsic_put = intrinsic_value_put(spot_prices, strike_price)
    long_put = long_put_payoff(spot_prices, strike_price, premium)
    short_put = short_put_payoff(spot_prices, strike_price, premium)
    short_intrinsic_put = -intrinsic_put  # Reverse of intrinsic for the short put

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    fig.suptitle('Long Put and Short Put Strategies')

    # Long Put subplot
    ax1.plot(spot_prices, intrinsic_put, 'b--', label='Intrinsic Value')
    ax1.plot(spot_prices, long_put, 'b', label='Long Put Payoff')
    ax1.axhline(0, color='black', linewidth=0.5)
    ax1.axvline(strike_price, color='gray', linestyle='--')
    ax1.set_title('Long Put Strategy')
    ax1.set_xlabel('XYZ Stock Price')
    ax1.set_ylabel('Profit/Loss')
    ax1.legend()
    ax1.grid(True)

    # Short Put subplot
    ax2.plot(spot_prices, short_intrinsic_put, 'b--', label='Intrinsic Value (Reversed)')
    ax2.plot(spot_prices, short_put, 'r', label='Short Put Payoff')
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(strike_price, color='gray', linestyle='--')
    ax2.set_title('Short Put Strategy')
    ax2.set_xlabel('XYZ Stock Price')
    ax2.set_ylabel('Profit/Loss')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Example usage: Define strike price, premium, and stock price range
strike_price = 50  # Example strike price for the long and short put
premium = 6.26  # Example premium for the put options
spot_range = (30, 70)  # Stock price range around the strike price

# Plot the graphs
plot_long_and_short_put(strike_price, premium, spot_range)
