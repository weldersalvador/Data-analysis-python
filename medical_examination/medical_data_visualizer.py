import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')


mask = mask = df['weight'] / ((df['height'] / 100)**2) > 25
df['overweight'] = mask.astype(int)


mask_colesterol = df['cholesterol'] > 1
mask_gluc = df['gluc'] > 1
df['cholesterol'] = mask_colesterol.astype(int)
df['gluc'] = mask_gluc.astype(int)


def draw_cat_plot():
    df_cat = df[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight', 'cardio']]
    df_cat = pd.melt(df_cat, id_vars='cardio', 
                    var_name='variable', value_name='value')


    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)


    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)


    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    mask = (
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    )
    df_heat = df[mask]

    corr = df_heat.corr()

    mask = np.triu(np.ones(corr.shape)).astype(bool)

    fig, ax = plt.subplots(figsize = (10,6))

    sns.heatmap(corr, ax = ax,mask = mask,annot = True,fmt=".1f")


    fig.savefig('heatmap.png')
    return fig
