# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 21:07:27 2016

@author: Hui
"""
#Write a python program to implement K-means clustering algorithm on the given datasets with k = 5
#display all observations along with their labels in a plot
#plot the evolution of the sum of squared error versus the iteration index

from numpy import *
from matplotlib import pyplot
import time
import scipy 

pyplot.close("all") 
mat_contents = scipy.io.loadmat('hw7_1_data2.mat') 
X = mat(mat_contents['Yn']) 
X=X.T 
[N,I]=shape(X)        
pyplot.ion() 
pyplot.ﬁgure(1) 
pyplot.plot(X[:,0], X[:,1], 'b.')   
K = 5      
C = X[0:K,:]  
E = 1  
m = 0
itr_max = 20 
min_dis = zeros((itr_max,N)) 
ind = zeros((itr_max, N)) 
ss = zeros((itr_max)) 
CC = zeros((K, I, itr_max)) 
CC[:,:,0] = C 
while (E > 1e-3):
    for n in range(0,N):
        dis = sqrt(sum(array(ones((K,1))*X[n] - C)**2, axis=1))
        min_dis[m,n] = amin(dis)
        ind[m,n] = argmin(dis)

    for k in range(0,K):
        C[k,:] = mean(X[ind[m,:] == k,:], axis=0)
        
    CC[:,:,m+1] = C

    E = linalg.norm(CC[:,:,m+1] - CC[:,:,m])
    ss[m] = sum(min_dis[m,:]**2)
    
    pyplot.figure(m+2)
    #pyplot.clf()
    cr = 'brgyk'
    for k in range(0,K):
        pyplot.plot(X[ind[m,:]==k,0], X[ind[m,:]==k,1], '.', \
                    color = cr[k], markersize = 10)
        pyplot.plot(C[k,0], C[k,1], 'o', color = cr[k], markersize = 15)
    
    m = m+1

pyplot.figure(m+2)
pyplot.plot(range(0,m), ss[0:m])

pyplot.show()
