#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from sklearn.datasets import load_boston
from sklearn import linear_model
boston = load_boston()
data = baston.data
target = boston.target
print(data.shape)
print(target.shape)

print('系数矩阵:\n',lineear_model.LinearRegression().fit(data,target).coef)