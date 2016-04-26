# coding=utf8
# Create by 吴俊 on 2016/4/4

import urllib
import numpy as np
# Data Loading
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url=url)
dataset = np.loadtxt(raw_data,delimiter=',')
X = dataset[:,0:7]
y = dataset[:,8]

# Feature Selection
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(X,y)
# display the relative importance of each attribute
print(model.feature_importances_)

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
# create the RFE model and select 3 attributes
rfe = RFE(model,3)
rfe = rfe.fit(X,y)
# summarize the selection of the attributes
print(rfe.support_)
print(rfe.ranking_)



