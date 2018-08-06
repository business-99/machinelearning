#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
名称：
日期：2018/8/3 13:31
@author: Tim.Wells

服务概述：

"""

import tensorflow as tf
from sklearn import datasets, metrics

iris = datasets.load_iris()
x, y = iris.data, iris.target
x_train, y_train = x[:140], y[:140]
x_test, y_test = x[140:], y[140:]

# Extract the features from the training data
feats = tf.contrib.learn.infer_real_valued_columns_from_input(x_train)

# Building a 3-layer DNN with 50 units each.
classifier_tf = tf.contrib.learn.DNNClassifier(feature_columns=feats, hidden_units=[50, 50, 50], n_classes=3)

# Use the train data to train this classifier
classifier_tf.fit(x_train, y_train, steps=5000)

# Use the trained model to predict on the test data
predictions = list(classifier_tf.predict(x_test, as_iterable=True))
print(y_test)
print(predictions)
score = metrics.accuracy_score(y_test, predictions)

print(score)
