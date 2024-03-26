#!/usr/bin/env python
# coding: utf-8

# In[6]:


import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
import pandas as pd


# In[2]:


# Define the Black-Scholes formula
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


# In[3]:


# Function to compute implied volatility
def implied_volatility(option_price, S, K, T, r):
    def difference(sigma): 
        return black_scholes_call(S, K, T, r, sigma) - option_price
    try:
        return brentq(difference, 0.01, 2.0)
    except ValueError:
        return np.nan


# In[10]:


# Fetch options data
ticker_name = 'AAPL'
ticker = yf.Ticker(ticker_name)
options_dates = ticker.options  # Get options expiration dates
options = ticker.option_chain(options_dates[0])  # Get options for the first expiration date


# In[12]:


# Calculate implied volatility for call options
call_data = options.calls
strike_prices = call_data['strike']
market_prices = call_data['lastPrice']
S = ticker.history(period="1d")['Close'][-1]  # Current stock price
T = (pd.to_datetime(options_dates[0]) - pd.Timestamp.now()).days / 365  # Time to expiration in years
r = 0.01  # Risk-free rate, assumption

implied_vols = [implied_volatility(market_price, S, K, T, r) for market_price, K in zip(market_prices, strike_prices)]


# In[11]:


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(strike_prices, implied_vols, marker='o')
plt.title(f'Implied Volatility Curve for {ticker_name}')
plt.xlabel('Strike Price')
plt.ylabel('Implied Volatility')
plt.grid(True)
plt.show()


# In[ ]:




