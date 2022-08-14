# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:01:37 2022

@author: HP
"""

import numpy as np, random, scipy.stats as ss, pandas as pd, sklearn.preprocessing as sp, sklearn.decomposition as sd, matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.neighbors import KNeighborsClassifier

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]

data = pd.read_csv("C:/Users/HP/Desktop/Python_Courses/Python_Research/wines.csv")
dummies = pd.get_dummies(data.color)
numeric_data = pd.concat([data, dummies], axis="columns")
numeric_data = numeric_data.drop(["color", "white","quality", "high_quality"], axis="columns")

scaled_data = sp.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns = numeric_data.columns)
pca = sd.PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)
print(principal_components.shape)

observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]
plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

 
np.random.seed(1)
n_rows = data.shape[0]
x = np.random.randint(0, 2, 1000)
y = np.random.randint(0 ,2, 1000)
def accuracy(predictions, outcomes):
    count = 0
    for i in range(len(outcomes)):
        if outcomes[i] == predictions[i]:
            count +=1
    return (count*100)/len(outcomes)
print(accuracy(x,y))
#accuracy(0, data["high_quality"])

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])
library_predictions = knn.predict(numeric_data)
print(accuracy(library_predictions, data["high_quality"]))

random.seed(123)
n_rows = data.shape[0]
print(n_rows)
selection = random.sample(range(n_rows), 10)
print(selection)
