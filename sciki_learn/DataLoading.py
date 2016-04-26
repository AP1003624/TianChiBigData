# coding=utf8
# Create by 吴俊 on 2016/3/30

# Data Loading
import numpy as np
import urllib
import requests
# url with dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# download the file
raw_data = urllib.urlopen(url=url)
# print(raw_data)
# raw_data01 = requests.get(url = url)
# print(raw_data01.text)
# load the csv file as a numpy matrix
dataset = np.loadtxt(raw_data,delimiter=',')
# separate the data from the target attributes
# 前8个为属性，第九个是分类标号
x = dataset[:,0:7]
y = dataset[:,8]
print(x)
print(y)
