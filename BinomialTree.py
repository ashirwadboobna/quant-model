import numpy as np
'''parameters
   s0 = Initial Stock price
   k= Strike Price
   T= Time to maturity in years
   r= Risk free Interest Rate
   sigma = volatility
   N= Number of steps

'''
# Parameters
S0 = 100       # Initial stock price
K = 100        # Strike price
T = 1.0        # Time to maturity in years
r = 0.05       # Risk-free interest rate
sigma = 0.2    # Volatility
N = 3          # Number of steps

# Step size
dt = T / N    # In the model division is made

# Up and down factors
u = np.exp(sigma * np.sqrt(dt))
d = 1 / u

# Risk-neutral probability
q = (np.exp(r * dt) - d) / (u - d)

# Binomial tree construction
price_tree = np.zeros((N+1, N+1))
for i in range(N+1):
    for j in range(i+1):
        price_tree[j, i] = S0 * (u ** (i-j)) * (d ** j)

# Option value at maturity
option_tree = np.zeros((N+1, N+1))
option_tree[:, N] = np.maximum(np.zeros(N+1), price_tree[:, N] - K)

# Backward induction
for i in range(N-1, -1, -1):
    for j in range(i+1):
        option_tree[j, i] = np.exp(-r * dt) * (q * option_tree[j, i+1] + (1-q) * option_tree[j+1, i+1])

# Option value
option_value = option_tree[0, 0]

print("European Call Option Value:", option_value)
