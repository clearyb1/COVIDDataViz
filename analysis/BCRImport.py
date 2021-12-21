import pandas as pd
import numpy as np
import matplotlib as plt

#Get Data
url = "https://opendata-geohive.hub.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D"

df = pd.read_csv(url)

print(df.head())
print(df.columns)
#Drop unnecessary columns
df = df.drop(df.columns[[0,1,3,5,6,7,8,9,11,12,13,14,15]], axis=1)
# make column index
df.set_index('CountyName', inplace=True)
df.sort_index()
print(df.head())
#Select Dublin only
print(df.loc['Dublin',:])



