'''
Alternative calculation
#%%
import numpy as np
import pandas as pd
import math
import QuantLib as ql
#%%
initialValue = ql.QuoteHandle(ql.SimpleQuote(100))
sigma = 0.2
today = ql.Date().todaysDate()
riskFreeTS = ql.YieldTermStructureHandle(ql.FlatForward(today, 0.05, ql.Actual365Fixed()))
volTS = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(today, ql.NullCalendar(), sigma, ql.Actual365Fixed()))
process = ql.BlackScholesProcess(initialValue, riskFreeTS, volTS)
process
# %%
'''


import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad



def n(x):
    '''pdf of standard normal distribution variable x'''
    return quad (lambda x: n(x), -20, d, limit= 50)[0]
