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

# Support Vector Machines
from sklearn import metrics
from sklearn.svm import SVC
# fit a svm neighbor model to the data
model = SVC()
model.fit(X,y)
print(model)
# make predictions
expected = y
predicted = model.predict(X)
# summarize the fit of the model
print(metrics.classification_report(expected,predicted))
print(metrics.confusion_matrix(expected,predicted))
