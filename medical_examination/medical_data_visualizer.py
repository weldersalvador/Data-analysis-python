import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2

mask = mask = df['weight'] / ((df['height'] / 100)**2) > 25
df['overweight'] = mask.astype(int)

# 3

mask_colesterol = df['cholesterol'] > 1
mask_gluc = df['gluc'] > 1
df['cholesterol'] = mask_colesterol.astype(int)
df['gluc'] = mask_gluc.astype(int)

# 4

def draw_cat_plot():
    # 5
    df_cat = df[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight', 'cardio']]
    df_cat = pd.melt(df_cat, id_vars='cardio', 
                    var_name='variable', value_name='value')


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)


    # 8
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
