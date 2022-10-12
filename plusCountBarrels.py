import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

df_hitterCount = pd.read_csv('data.csv')
df_hitterCount = df_hitterCount[['PlateLocSide', 'PlateLocHeight', 'Pitcher', 'Batter', 'Balls', 'Strikes', 'TaggedPitchType', 'ExitSpeed', 'PitchCall']]
df_hitterCount = df_hitterCount[(df_hitterCount['Strikes'] < 2) & (df_hitterCount['Balls'] >= 2)]
df_hitterCount = df_hitterCount[(df_hitterCount['PlateLocSide'] > -0.7) & (df_hitterCount['PlateLocSide'] < 0.7) & (df_hitterCount['PlateLocHeight'] < 3.6) & (df_hitterCount['PlateLocHeight'] > 1.5)]

col=[]

for i in range(0,len(df_hitterCount)):
    if df_hitterCount.iloc[i]['PitchCall'] == "StrikeCalled" and (df_hitterCount.iloc[i]['TaggedPitchType'] == "Sinker" or df_hitterCount.iloc[i]['TaggedPitchType'] == "Fastball"): 
        col.append('red')
    elif df_hitterCount.iloc[i]['PitchCall'] == "StrikeSwinging": 
        col.append('grey')
    elif df_hitterCount.iloc[i]['PitchCall'] == 'InPlay':
        col.append('blue')
    else:
        col.append('grey') 

plt.scatter(df_hitterCount['PlateLocSide'], df_hitterCount['PlateLocHeight'], c=col)

df_temp = df_hitterCount[df_hitterCount['PitchCall'] == 'InPlay']

annotations = []

for i in range(len(df_temp)):
    annotations.append(df_temp.iloc[i]['ExitSpeed'])

for i, label in enumerate(annotations): 
    plt.annotate(round(label, 2), (df_temp.iloc[i]['PlateLocSide']+0.05, df_temp.iloc[i]['PlateLocHeight']))
    plt.annotate(df_temp.iloc[i]['Batter'], (df_temp.iloc[i]['PlateLocSide']+0.05, df_temp.iloc[i]['PlateLocHeight']+0.1))
