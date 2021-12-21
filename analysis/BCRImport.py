import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Get Data
url = "https://opendata-geohive.hub.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D"

df = pd.read_csv(url)

print(df.head())
print(df.columns)
#Select D counties Dublin Donegal only 'dfd'
df=df.loc[
    df['CountyName'].isin(['Dublin','Donegal'])]
print(df.head())

df.transpose()
print(df)

#Drop unnecessary columns
df = df.drop(df.columns[[0,1,3,5,6,7,8,9,11,12,13,14,15]], axis=1)
print(df.shape)
df.set_index('TimeStamp',inplace=True)
df.index = pd.to_datetime(df.index)
print(df)

#Visualisations

df.plot()
plt.xlabel('Date')
plt.ylabel('No of Cases')
plt.title('Cumulative Confirmed COVID Cases Dublin & Donegal')
plt.show()

#Select Dublin only
df=df.loc[
    df['CountyName'].isin(['Dublin'])]

df.plot()
plt.xlabel('Date')
plt.ylabel('No of Cases')
plt.title('Cumulative Confirmed COVID Cases Dublin')
plt.show()