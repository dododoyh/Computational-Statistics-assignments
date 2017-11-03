# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 18:42:55 2016

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


def multilinreg(X0,y0):
    m, n = shape(X0)    
    X = zeros((m,n))
    for i in range(0,m):
        for j in range(0,n):
            X[i,j] = X0[i,j]
    y = zeros((m,1))
    for i in range(0,m):
        y[i] = y0[i]            
            
    for j in range(1,n+1):
        v = house(X[range(j-1,m),j-1])
        temp2 = rowhouse(X[range(j-1,m)][:,range(j-1,n)], v)
        for k in range(j,m+1):
            for r in range(j,n+1):
                X[k-1, r-1] = temp2[k-j, r-j]
        beta = -2.*(v.T*y[range(j-1,m)])/(v.T*v)
        for k in range(j,m+1):
            y[k-1] = y[k-1] + beta*v[k-j]
    b = backsub(X,y)
    return b



# principal component analysis

from numpy import *
from matplotlib import pyplot
import scipy
import scipy.linalg

def pca_exp():

    x = mat(" \
    15    13; \
    16    11; \
    12    13; \
    14    12; \
    13    9; \
    15    14; \
    16    12; \
    21    16; \
    12    9; \
    11    8; \
    19    15; \
    14    13; \
    13    15; \
    14    13; \
    16    12; \
    17    16; \
    12    11; \
    16    9")

    #### Perform the PCA analysis ###
    m, n = shape(x) 

    # 1. Compute sample covariance
    C = cov(x.T)

    # 2. SVD on C
    U, S, Vh = linalg.svd(C)
    V = Vh.T

    # 3. select the first 2 columns of U
    U1 = U[:,0:2]

    # 4. Define Z 
    Z = x*U1;

    ## plot the raw data
    pyplot.figure(1)
    pyplot.plot(x[:,0], x[:,1], '.')
    pyplot.axis([5, 22, 5, 22])
    pyplot.axis('equal')
    pyplot.xlabel('First Trial (min)')
    pyplot.ylabel('Second Trial (min)');  

    
    ## plot the transformed data
    pyplot.figure(2)
    pyplot.plot(Z[:,0], Z[:,1], '.')
    pyplot.axis([-28, -10, -8, 6])
    pyplot.axis('equal')
    pyplot.xlabel('Principal Component 1')
    pyplot.ylabel('Principal Component 2')

    ## add the principal directions
    pyplot.figure(1)
    m_x = x.mean(axis=0)
    TP1 = array(2*sqrt(S[0])*mat([-U[0, 0], U[0, 0]])+m_x[0,0])
    TP2 = array(2*sqrt(S[0])*mat([-U[1, 0], U[1, 0]])+m_x[0,1])
    TP3 = array(2*sqrt(S[1])*mat([-U[0, 1], U[0, 1]])+m_x[0,0])
    TP4 = array(2*sqrt(S[1])*mat([-U[1, 1], U[1, 1]])+m_x[0,1])      
    pyplot.plot(TP1[0], TP2[0], 'g-')

    pyplot.show()

    ## compare the covariance and the total variance
    Cov_x = cov(x.T)
    Cov_Z = cov(Z.T)
    Total_var_x = trace(Cov_x)
    Total_var_Z = trace(Cov_Z)
    
    print('Cov_x ='+repr(Cov_x), 'Cov_Z ='+repr(Cov_Z))

    print('total_var_x = ' + repr(Total_var_x), 'total_var_z = ' + repr(Total_var_Z))
    print('total_var_x = %5.2f' %Total_var_x, 'total_var_Z = %5.2f' %Total_var_Z) 
    
