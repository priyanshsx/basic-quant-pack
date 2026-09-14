import pandas as pd 
import numpy as np 
import plotly.graph_objects as go 

# importing the raw csv file and creating a df from it 

while True:
    user_file = input(f"Please enter the name of the file you'd like to run the Quantitative Analysis Pack on: ")

    try:
        df = pd.read_csv(user_file, index_col='date', parse_dates=True)
        break
    except FileNotFoundError:
        print(f"\nFile not found. Please ensure that the file is in the folder where this script runs from and ensure that you get the name exactly right.\n")

# daily returns 

df['daily_returns'] = df['close'].pct_change()

# moving averages

df['sma_20'] = df['close'].rolling(window=20).mean()
df['sma_50'] = df['close'].rolling(window=50).mean()

# calculating the log returns (concept to research: np.log() and .shift()) 
df['log_returns'] = np.log(df['close'] / df['close'].shift(1)) 

# rolling volatility for a 30-day period (annualized, for 365 trading days for crypto)

df['rolling_vol_annualized'] = df['log_returns'].rolling(window=30).std() * np.sqrt(365)

# calculating the cumulative return (concept to research: .cumprod())

df['cumulative_return'] = (1 + df['daily_returns']).cumprod() - 1 

# calculating the max drawdown 

df['cum_return_for_drawdown'] = (1 + df['daily_returns'].fillna(0)).cumprod()
df['running_max'] = df['cum_return_for_drawdown'].cummax()
df['drawdown'] = ((df['cum_return_for_drawdown'] - df['running_max']) / df['running_max'])
max_drawdown = df['drawdown'].min()

# saving the processed data as a new csv file 
df.to_csv('/home/priyansh/Documents/d/basic_quant_pack/processed/processed_data.csv')

# print info 
print(df.info())

# saving the processed file 
print(f"\nThe file is now saved as processed_data.csv in the folder: processed.")

# visualization engine (concept to research: plotly candlestick charts)

