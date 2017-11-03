# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:14:48 2016

@author: Hui
"""

from numpy import *

def backsub(X, y):
    l = shape(X)  
    n = l[1]
    b = zeros((n,1))
    b[n-1, 0] = y[n-1, 0]/X[n-1, n-1]
    for j in range(n-1,0,-1):
        b[j-1,0] = (y[j-1,0] - dot(X[j-1, range(j,n)], b[range(j,n),0]))/X[j-1, j-1]
    return b


def house(x):
    m = size(x)
    mu = linalg.norm(x)
    v = zeros((m,1))
    for i in range(0,m):
        v[i,0] = x[i]
    if mu != 0:
        c = x[0] + sign(x[0])*mu
        for i in range(1,m):
            v[i,0] = v[i,0]/c
    v[0] = 1
    v = mat(v)
    return v


def rowhouse(X,v):
    X = mat(X)
    v = mat(v)
    beta = -2./(v.T * v)
    w = (X.T*v)*beta
    X = X + v*w.T
    return X


