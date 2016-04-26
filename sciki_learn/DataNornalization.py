# coding=utf8
# Create by 吴俊 on 2016/3/30
import urllib
import numpy as np


url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url=url)
# print(raw_data)
dataset = np.loadtxt(raw_data,delimiter=',')
x = dataset[:,0:7]
y = dataset[:,8]

from sklearn import preprocessing
# normalize the data attributes
normalized_x = preprocessing.normalize(x)
print(normalized_x[:6])
# standardize the data attributes
standardized_x = preprocessing.scale(x)
print(standardized_x[:6])



