# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:02:10 2022

@author: HP
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as ss
from matplotlib.colors import ListedColormap

def distance(p,i):
    return np.sqrt(np.sum(np.power((p-i), 2)))

def majority_vote(votes):
    vote_counts = {}
    for v in votes:
        if v not in vote_counts:
            vote_counts[v] = 1
        else:
            vote_counts[v] += 1
    max_count = max(vote_counts.values())
    winners = []
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)       
    return random.choice(winners)
    
def find_nearest_neighbours(points, p, k):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(points[i], p)
    ind = np.argsort(distances)
    return ind[0:k]

def knn_predict(points, p, outcomes, k=5):
    ind = find_nearest_neighbours(points, p, k)
    return majority_vote(outcomes[ind])

def generate_synth_data(n):
    points = np.concatenate((ss.norm(0,1).rvs((n,2)),ss.norm(1,1).rvs((n,2))), axis = 0)
    outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n)))
    return points, outcomes

def make_prediction_grid(limits, h, points, outcomes, k):
    (xmin, xmax, ymin, ymax) = limits
    xs = np.arange(xmin,xmax,h)
    ys = np.arange(ymin,ymax,h)
    xx, yy = np.meshgrid(xs, ys)
    prediction_grid = np.zeros(xx.shape)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(points, p, outcomes, k)
    return xx, yy, prediction_grid

def plot_prediction_grid(xx, yy, prediction_grid, points, outcomes):
    background_colormap = ListedColormap (["hotpink", "yellowgreen"])
    observation_colormap = ListedColormap (["red","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(points[:,0], points[:,1], c = outcomes, cmap = observation_colormap, s = 50)   
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    return plt.show()     
    
points, outcomes = generate_synth_data(50)
xx, yy, prediction_grid = make_prediction_grid((-2,2,-2,2), 0.5, points, outcomes, 5)
plot_prediction_grid(xx, yy, prediction_grid, points, outcomes)



