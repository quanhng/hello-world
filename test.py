# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 23:53:55 2017

@author: QuanNguyen
"""

import numpy as np

A = np.array([[5,-2,3],[-3,9,1],[2,-1,-7]])
b = np.array([10,18,-21])
D = np.diag(A)
R = A - np.diagflat(D)

x=np.array([0,0,0])

for n in range(10):
    x = (b - np.dot(R,x)) / D
    print('Iteration ', n, x)