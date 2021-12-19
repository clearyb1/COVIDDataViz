# plot_web_api_realtime.py
"""
A live auto-updating plot of random numbers pulled from a web API
"""

import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np


url = "https://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D"

df = pd.read_csv(url)

print(df)
print(df.info())
print(df.columns)
print(df.sort_values("ConfirmedCovidCases"))
print(df["ConfirmedCovidCases"].mean())

df['month_year'] = pd.to_datetime(df['Date']).dt.to_period('M')
print(df.head())
print(df.pivot_table(values="ConfirmedCovidCases", index="month_year", aggfunc=[np.mean, np.median]))

# create the figure and axis objects
fig, ax = plt.subplots()

# plot the data and customize
x= ['Date']
y= ['ConfirmedCovidCases']

line = ax.plot(x,y)
ax.set_xlabel('Day Number')
ax.set_ylabel('Count')
ax.set_title('Cases')

# save and show the plot
#fig.savefig('static_plot.png')
plt.show()

# function to pull out a float from the requests response object
def pull_float(response):
    jsonr = response.json()
    strr = jsonr["Aged85up"][0]
    if strr:
        fltr = round(float(strr), 2)
        return fltr
    else:
        return None


# Create figure for plotting
#fig, ax = plt.subplots()
xs = []
ys = []

def animate(i, xs:list, ys:list):
    # grab the data from thingspeak.com
    response = requests.get(url)
    flt = pull_float(response)
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(flt)
    # Limit x and y lists to 10 items
    xs = xs[-10:]
    ys = ys[-10:]
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    # Format plot
    ax.set_ylim([0,255])
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.20)
    ax.set_title('Plot of random numbers from https://qrng.anu.edu.au')
    ax.set_xlabel('Date Time (hour:minute:second)')
    ax.set_ylabel('Random Number')

# Set up plot to call animate() function every 1000 milliseconds
#ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval=1000)

#plt.show()