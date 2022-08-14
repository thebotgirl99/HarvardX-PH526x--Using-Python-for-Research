# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:38:03 2022

@author: HP
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("movie.csv", index_col=0)

df['profitable'] = df.revenue > df.budget
df['profitable'] = df['profitable'].astype(int)
regression_target = 'revenue'
classification_target = 'profitable'
df['profitable'].value_counts()

df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna(how="any")
df.shape

list_genres = df.genres.apply(lambda x: x.split(","))
genres = []
for row in list_genres:
    row = [genre.strip() for genre in row]
    for genre in row:
        if genre not in genres:
            genres.append(genre)
for genre in genres:
    df[genre] = df['genres'].str.contains(genre).astype(int)

continuous_covariates = ['budget', 'popularity', 'runtime', 'vote_count', 'vote_average']
outcomes_and_continuous_covariates = continuous_covariates + [regression_target, classification_target]
plotting_variables = ['budget', 'popularity', regression_target]
axes = pd.plotting.scatter_matrix(df[plotting_variables], alpha=0.15, \
       color=(0,0,0), hist_kwds={"color":(0,0,0)}, facecolor=(1,0,0))
plt.show()
print(df[outcomes_and_continuous_covariates].skew())
for covariate in ['budget', 'popularity', 'runtime', 'vote_count', 'revenue']:
    df[covariate] = df[covariate].apply(lambda x: np.log10(1+x))
print(df[outcomes_and_continuous_covariates].skew())
df.to_csv("movies_clean.csv")