# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 14:47:29 2022

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature

birddata = pd.read_csv("C:/Users/HP/Desktop/Python_Courses/Python_Research/bird_tracking.csv")

grouped_birds = birddata.groupby("bird_name")
mean_speeds = grouped_birds["speed_2d"].mean()
mean_altitudes = grouped_birds["altitude"].mean()
print(mean_speeds, mean_altitudes)

birddata.date_time = pd.to_datetime(birddata.date_time)
birddata["date"] = birddata.date_time.dt.date

grouped_bydates = birddata.groupby("date")
mean_altitudes_perday = grouped_bydates["altitude"].mean()
print(mean_altitudes_perday.head(30))

grouped_birdday = birddata.groupby(["bird_name", "date"])
mean_altitudes_perday = grouped_birdday["altitude"].mean()
mean_speeds_perday = grouped_birdday["speed_2d"].mean()

eric_daily_speed  = pd.Series(mean_speeds_perday["Eric"])
sanne_daily_speed = pd.Series(mean_speeds_perday["Sanne"])
nico_daily_speed  = pd.Series(mean_speeds_perday["Nico"])
eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()

print(mean_speeds_perday["Nico"].tail(30))