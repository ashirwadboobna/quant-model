#%%
import numpy as np
import pandas as pd
import stat as stat
import yfinance as yf 
import matplotlib.pyplot as plt
#%%

# Download historical data for selected stocks
tickers = ['AAPL']
data = yf.download(tickers, start='2015-01-01', end='2021-01-01')['Adj Close']

# Calculate daily returns
returns = data.pct_change().dropna()

returnsframe =pd.DataFrame(returns)

print (returnsframe)

values = returnsframe.describe()
print(values)


data1 = np.random.normal(loc=0, scale=1, size=1000)
#%%

#%%
plt.plot(returnsframe, color ="black", linestyle='dashed')
# %%
plt.hist(returnsframe,bins= 200, color ="black",density=True)

# %%
standard_normal_var = np.random.normal(size=1)

standard_normal_var
# %%
import statistics as st


# %%
mean1 = returnsframe.mean()
std= returnsframe.std()
value = pd.DataFrame(data)

print(mean1, std)
# %%
import math  
# %%
tstep= 0.01
randnumbers = value*(1+mean1*tstep+ std*standard_normal_var*math.sqrt(tstep))

randnumbers
# %%
plt.hist(randnumbers, bins= 300)
# %%
#plt.plot(randnumbers)

newreturns = randnumbers.pct_change().dropna()
nreturns = pd.DataFrame(newreturns)



plt.hist(nreturns, color= 'black', bins= 300)
# %%
