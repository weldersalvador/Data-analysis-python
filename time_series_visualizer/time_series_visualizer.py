import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import time
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.index = df['date']
df = df.drop(['date'],axis = 1)
df.index = pd.to_datetime(df.index)
# Clean data
mask = ((df['value']) >= (df['value'].quantile(0.025))) & ((df['value']) <= df['value'].quantile(0.975))
df = df[mask]


def draw_line_plot():
    # Draw line plot
    axes = df.plot(title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019'
        ,xlabel = 'Date',ylabel = 'Page Views',color = 'red')
    fig = axes.get_figure()
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = pd.Categorical(
        df_bar.index.strftime('%B'),
        categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September'
        , 'October','November','December']
    )  
    df_bar = df_bar.groupby(['month','year'])['value'].mean().reset_index()
    # Draw bar plot
    
    pivot = df_bar.pivot(index = 'year',columns = 'month',values = 'value')
    axes = pivot.plot(kind = 'bar',xlabel = 'Years',ylabel= 'Average Page Views',
        title = 'Accesses per month',figsize=(12,6))
    fig = axes.get_figure()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,axes = plt.subplots(1,2,figsize=(25,8))
    f1 = sns.boxplot(data = df_box, x= 'year',y='value',palette='Set3',ax = axes[0],fliersize = 2)
    f1.set_xlabel("Year")
    f1.set_ylabel("Page Views")
    f1.set_title("Year-wise Box Plot (Trend)")
    f2 = sns.boxplot(data = df_box,x = 'month',y = 'value',palette = 'Set2',ax = axes[1],fliersize = 2)
    f2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'
        , 'Oct','Nov','Dec'])
    f2.set_ylabel("Page Views")
    f2.set_xlabel("Month")
    f2.set_title("Month-wise Box Plot (Seasonality)")
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
