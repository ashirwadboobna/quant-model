import numpy as np
import matplotlib.pyplot as plt

class PutCallParity:
    def __init__(self, S, K, r, T):
        self.S = S  # Current stock price
        self.K = K  # Strike price
        self.r = r  # Risk-free interest rate
        self.T = T  # Time to maturity in years

    def call_payoff(self, asset_prices):
        """Calculate call payoff at different asset prices at expiration."""
        return np.maximum(asset_prices - self.K, 0)

    def put_payoff(self, asset_prices):
        """Calculate put payoff at different asset prices at expiration."""
        return np.maximum(self.K - asset_prices, 0)

    def plot_payoffs(self):
        """Plot the payoffs of call and put options at expiration along with the combined parity."""
        asset_prices = np.linspace(0, 2 * self.K, 100)
        call_payoffs = self.call_payoff(asset_prices)
        put_payoffs = self.put_payoff(asset_prices)

        # Calculating combined portfolio payoff: Long Call + Short Put + Bond (K * e^(-rT))
        bond_value = self.K * np.exp(-self.r * self.T)
        combined_payoff = call_payoffs - put_payoffs + bond_value

        plt.figure(figsize=(10, 5))
        plt.plot(asset_prices, call_payoffs, label='Call Payoff')
        plt.plot(asset_prices, put_payoffs, label='Put Payoff')
        plt.plot(asset_prices, combined_payoff, label='Combined Portfolio (C - P + Ke^-rT)', linestyle='--')
        plt.xlabel('Asset Price at Expiration ($)')
        plt.ylabel('Payoff ($)')
        plt.title('Put-Call Parity Payoff Profiles')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(self.K, color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage:
# Create an instance of PutCallParity
parity_model = PutCallParity(S=100, K=100, r=0.05, T=1)

# Plot the payoff profiles
parity_model.plot_payoffs()
