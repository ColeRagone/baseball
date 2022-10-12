import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

df = pd.read_csv('data.csv') 

df = df[['Pitcher', 'Batter','PitchCall', 'PlateLocHeight', 'PlateLocSide']]

rect = mpatches.Rectangle((-0.7,1.6),1.4,2.1, 
                        fill = False,
                        color = "black",
                        linewidth = 2)

plt.gca().add_patch(rect)

col=[]
for i in range(0,len(df)):
    if df.iloc[i]['PitchCall'] == "StrikeSwinging" or df.iloc[i]['PitchCall'] == "StrikeCalled":
        col.append('r')
    elif df.iloc[i]['PitchCall'] == 'InPlay':
            col.append('k')
    else:
        col.append('b') 

plt.scatter(df['PlateLocSide'], df['PlateLocHeight'], c = col)
plt.show()