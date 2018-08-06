#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
名称：
日期：2018/6/28 10:05
@author: Tim.Wells

服务概述：

"""
from sklearn import datasets
from sklearn import svm, metrics
import numpy as np
from sklearn.externals import joblib

iris = datasets.load_iris()
x, y = iris.data, iris.target
x_train, y_train = x[:140], y[:140]
x_test, y_test = x[140:], y[140:]

classifier_sk = svm.SVC()

# Use the train data to train this classifier

classifier_sk.fit(x_train, y_train)

# Use the trained model to predict on the test data

predictions = classifier_sk.predict(x_test)
print(y_test)
print(predictions)

score = metrics.accuracy_score(y_test, predictions)

print(score)
