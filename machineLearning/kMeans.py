# https://www.kdnuggets.com/2018/09/iterative-initial-centroid-search-sampling-k-means-clustering.html
import numpy as np
import pandas as pd
from sklearn import preprocessing

# Read dataset
# data = pd.read_csv('3D_spatial_network.csv', header=None)
data = pd.read_csv("transactions.csv", header=None)

# Drop first column (not required)
# data.drop(labels=0, axis=1, inplace=True)

# Normalize data (min/max scaling)
data_arr = data.values
sc = preprocessing.MinMaxScaler()
data_sc = sc.fit_transform(data_arr)
data = pd.DataFrame(data_sc)

print(data)
