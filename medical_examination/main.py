import pandas as pd

df = pd.read_csv('medical_examination.csv')

mask = df['weight'] / ((df['height'] / 100)**2) > 25

print(mask)