import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Get Data
url = "https://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D"

df = pd.read_csv(url)

print(df.head())
print(df.columns)


#Drop unnecessary columns
df = df.drop(df.columns[[0,1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
                        19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,
                        35,36,37,38,39,40]], axis=1)
print(df.shape)
print(df)

df.set_index('Date',inplace=True)
df.index = pd.to_datetime(df.index)
print(df)

#df.transpose()
#print(df)



#Visualisations

df.plot()
plt.xlabel('Date')
plt.ylabel('No of Cases')
plt.title('Confirmed COVID Cases')
plt.show()

#Animated Line https://towardsdatascience.com/learn-how-to-create-animated-graphs-in-python-fce780421afe
color = ['red']
fig = plt.figure()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('No of Cases')
plt.xlabel('Dates')

def buildmebarchart(i=int):
    plt.legend(df.columns)
    p = plt.plot(df[:i].index, df[:i].values) #note it only returns the dataset, up to the point i
    for i in range(0,1):
        p[i].set_color(color[i]) #set the colour of each curve
import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 10)
plt.show()

#Select Nov01-Dec 21 2020
df20=df['11/01/20' :'12/21/20']

#Animated Line https://towardsdatascience.com/learn-how-to-create-animated-graphs-in-python-fce780421afe
color = ['red']
fig = plt.figure()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('No of Cases')
plt.xlabel('Dates')

def buildmebarchart(i=int):
    plt.legend(df20.columns)
    p = plt.plot(df20[:i].index, df20[:i].values) #note it only returns the dataset, up to the point i
    for i in range(0,1):
        p[i].set_color(color[i]) #set the colour of each curve
import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 10)
plt.show()

#Select Nov01-Dec 21 2021
df21=df['11/01/21' :'12/21/21']

#I selected and ran these individually

#Animated Line https://towardsdatascience.com/learn-how-to-create-animated-graphs-in-python-fce780421afe
color = ['red']
fig = plt.figure()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('No of Cases')
plt.xlabel('Dates')

def buildmebarchart(i=int):
    plt.legend(df21.columns)
    p = plt.plot(df21[:i].index, df21[:i].values) #note it only returns the dataset, up to the point i
    for i in range(0,1):
        p[i].set_color(color[i]) #set the colour of each curve
import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 10)
plt.show()

#Combine Nov01-Dec 21 2020 & 2021 into same graph- non-contiguous date range

combined = pd.concat([df20, df21])

color = ['red']
fig = plt.figure()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('No of Cases')
plt.xlabel('Dates')

def buildmebarchart(i=int):
    plt.legend(combined.columns)
    p = plt.plot(combined[:i].index, combined[:i].values) #note it only returns the dataset, up to the point i
    for i in range(0,1):
        p[i].set_color(color[i]) #set the colour of each curve
import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 10)
plt.show()

#Saving this directly as a GIF/MP4 is beyond my ability (and time available)
