# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 19:02:52 2022

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature

birddata = pd.read_csv("C:/Users/HP/Desktop/Python_Courses/Python_Research/bird_tracking.csv")

bird_names = pd.unique(birddata.bird_name)
for bird in bird_names:
    indices = birddata.bird_name == bird
    xp = birddata.latitude[indices]
    yp = birddata.longitude[indices]
    plt.plot(xp,yp, ".", label = bird)
    plt.xlabel("latitude")
    plt.ylabel("longitude")
    plt.title("Bird Data")
plt.legend(loc= "upper left")

indices = birddata.bird_name == "Eric"
speed = birddata.speed_2d[indices]
plt.hist(speed, density = True, stacked = True, bins = np.linspace(0,30,20), edgecolor="black")
plt.xlabel("2D speed m/s")
plt.ylabel("frequency")

time_stamps = []
for k in range(len(birddata.date_time)):
    time = datetime.datetime.strptime(birddata.date_time[k][:-3], "%Y-%m-%d %H:%M:%S")
    time_stamps.append(time)
birddata["timestamp"] = pd.Series(time_stamps, index = birddata.index)  
  
indx = birddata.bird_name == "Eric"
times = birddata.timestamp[indx]
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time)/datetime.timedelta(days=1)

plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1))
plt.xlabel("observation")
plt.ylabel("elapsed time in days")

next_day = 1
inds = []
daily_mean_speed = []
for (i, d) in enumerate(elapsed_days):
    if d < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(birddata.speed_2d[inds]))
        next_day += 1
        inds = []

plt.plot(daily_mean_speed)
plt.xlabel("days")
plt.ylabel("mean 2d speed m/s")

proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=":")

bird_names = pd.unique(birddata.bird_name)
for bird in bird_names:
    indices = birddata.bird_name == bird
    x = birddata.latitude[indices]
    y = birddata.longitude[indices]
    ax.plot(x, y, ".", transform = ccrs.Geodetic(), label = bird)
    plt.xlabel("latitude")
    plt.ylabel("longitude")
    plt.title("Bird Data")
plt.legend(loc="upper left")

