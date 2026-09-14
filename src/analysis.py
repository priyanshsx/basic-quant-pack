import pandas as pd 
import numpy as np 
import plotly.graph_objects as go 

# importing the raw csv file and creating a df from it 

while True:
    user_file = input(f"Please enter the name of the file you'd like to run the Quantitative Analysis Pack on: ")

    try:
        df = pd.read_csv(user_file, index_col='date', parse_dates=True)
    except FileNotFoundError:
        print(f"\nFile not found. Please ensure that the file is in the folder where this script runs from and ensure that you get the name exactly right.\n")

# calculating standard returns (concept to research: .pct_change())

# calculating the log returns (concept to research: np.log() and .shift()) 

# calculating the rolling volatility (concept to research: .rolling(), .std())

# calculating the 20D and 50D SMA (concept to research: .mean())

# calculating the cumulative return (concept to research: .cumprod())

# calculating the max drawdown 

# visualization engine (concept to research: plotly candlestick charts)

