import requests
import matplotlib.pyplot as plt
from datetime import datetime
#%%
# Your FRED API Key
api_key = #use your api key

# FRED series IDs for Treasury yields you want to include in the curve
series_ids = {
    '1-Month': 'DGS1MO',
    '3-Month': 'DGS3MO',
    '6-Month': 'DGS6MO',
    '1-Year': 'DGS1',
    '2-Year': 'DGS2',
    '5-Year': 'DGS5',
    '10-Year': 'DGS10',
    '30-Year': 'DGS30',
}
#%%
# Function to fetch data from FRED
def fetch_fred_series(series_id):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"
    response = requests.get(url)
    data = response.json()['observations']
    # Extract the latest value
    latest_data = data[-1]
    value = latest_data['value']
    if value == '.':
        value = 0
    return float(value)

# Prepare data for plotting
maturities = []
rates = []

for maturity, series_id in series_ids.items():
    rate = fetch_fred_series(series_id)
    maturities.append(maturity)
    rates.append(rate)

# Convert string maturities to numerical values (for plotting purposes)
numerical_maturities = [1/12, 3/12, 6/12, 1, 2, 5, 10, 30]  # Example conversion

# Plotting the curve
plt.figure(figsize=(10, 6))
plt.plot(numerical_maturities, rates, marker='o')
plt.title('Interest Rate Curve')
plt.xlabel('Maturity (Years)')
plt.ylabel('Yield (%)')
plt.xticks(numerical_maturities, maturities)
plt.grid(True)
plt.show()

