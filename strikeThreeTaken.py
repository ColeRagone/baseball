# analyze pitches with two strikes 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

df_twoStrikes = pd.read_csv('data.csv')
df_twoStrikes = df_twoStrikes[['Pitcher', 'Batter', 'Strikes', 'PitchCall', 'PlateLocHeight', 'PlateLocSide', 'TaggedPitchType']]
df_twoStrikes = df_twoStrikes[(df_twoStrikes['Strikes'] == 2) & (df_twoStrikes['PitchCall'] == 'StrikeCalled')]

col=[]
for i in range(0,len(df_twoStrikes)):
    if df_twoStrikes.iloc[i]['TaggedPitchType'] == "Curveball" or df_twoStrikes.iloc[i]['TaggedPitchType'] == "Slider":
        col.append('b')
    elif df_twoStrikes.iloc[i]['TaggedPitchType'] == 'ChangeUp':
            col.append('k')
    else:
        col.append('r') 

plt.scatter(df_twoStrikes['PlateLocSide'], df_twoStrikes['PlateLocHeight'], c=col)

rect = mpatches.Rectangle((-0.7,1.6),1.4,2.1, 
                        fill = False,
                        color = "black",
                        linewidth = 2)

plt.gca().add_patch(rect)

# add labels 

annotations = []
for i in range(len(df_twoStrikes)): 
    annotations.append(df_twoStrikes.iloc[i]['Batter'])

for i, label in enumerate(annotations):
    plt.annotate(label, (df_twoStrikes.iloc[i]['PlateLocSide'], df_twoStrikes.iloc[i]['PlateLocHeight']+0.1))

plt.show() 
