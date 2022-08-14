# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 16:44:02 2022

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering 

whisky = pd.read_csv("C:/Users/HP/Desktop/Python_Courses/Python_Research/whiskies.txt")
whisky["Region"] = pd.read_csv("C:/Users/HP/Desktop/Python_Courses/Python_Research/regions.txt")
flavors = whisky.iloc[:, 2:14]

corr_flavors = pd.DataFrame.corr(flavors)
corr_whisky = pd.DataFrame.corr(flavors.transpose())

plt.pcolor(corr_whisky)
plt.colorbar()

model = SpectralCoclustering(n_clusters=6,random_state=0)
model.fit(corr_whisky)
np.sum(model.rows_,axis=1)
np.sum(model.rows_,axis=0)
model.row_labels_

whisky["Group"] = pd.Series(model.row_labels_,index=whisky.index)
whisky = whisky.iloc[np.argsort(model.row_labels_)] #rearranges matrix along with indices
whisky = whisky.reset_index(drop=True) #changess matrix indices to start from 0-n


new_flavors = whisky.iloc[:, 2:14]
new_corr_whisky = pd.DataFrame.corr(new_flavors.transpose())

plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(new_corr_whisky)
plt.title("Rearranged")
plt.axis("tight")



