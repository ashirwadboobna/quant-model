import yfinance as yf

# Define the ticker for which to fetch options data
ticker_symbol = 'AAPL'
ticker = yf.Ticker(ticker_symbol)

# Fetch the current stock price
current_price = ticker.history(period='1d')['Close'][0]

# Fetch available options expiration dates
expiries = ticker.options

# Function to classify options
def classify_option(strike, current_price, option_type):
    if option_type == 'call':
        if strike < current_price:
            return 'ITM'
        elif strike > current_price:
            return 'OTM'
        else:
            return 'ATM'
    elif option_type == 'put':
        if strike > current_price:
            return 'ITM'
        elif strike < current_price:
            return 'OTM'
        else:
            return 'ATM'
    return None

# Iterate through each expiry date to classify options
for expiry in expiries:
    calls = ticker.option_chain(expiry).calls
    puts = ticker.option_chain(expiry).puts

    # Classify calls
    calls['Classification'] = calls['strike'].apply(classify_option, current_price=current_price, option_type='call')

    # Classify puts
    puts['Classification'] = puts['strike'].apply(classify_option, current_price=current_price, option_type='put')

    # Print results for this expiry date
    print(f"Expiry Date: {expiry}")
    print("Calls:")
    print(calls[['strike', 'Classification']])
    print("Puts:")
    print(puts[['strike', 'Classification']])
