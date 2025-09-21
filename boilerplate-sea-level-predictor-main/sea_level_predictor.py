import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)

    # Create first line of best fit
    result = linregress(x,y)
    x = np.arange(1880,2051)
    y = result.slope*x + result.intercept
    plt.plot(x,y)
    # Create second line of best fit
    mask = df['Year'] >= 2000
    new_df = df[mask]
    x1 = new_df['Year']
    y1 = new_df['CSIRO Adjusted Sea Level']
    result2 = linregress(x1,y1)
    x1 = np.arange(2000,2051)
    y = result2.slope*x1 + result2.intercept
    plt.plot(x1,y)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()