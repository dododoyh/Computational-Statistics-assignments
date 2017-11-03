
#use principal component analysis to reduce n to d and then solve for the coefficients b in linear regression
#Compute and plot the SSE for values of d ranging from 10 to 100 in the steps of 10

from numpy import *
from matplotlib import pyplot
import scipy
from mlr import *
from scipy import io
mat_contents = scipy.io.loadmat('hw4_1_data')
x = mat(mat_contents['X'])
y = mat(mat_contents['y'])
m, n = shape(x) 
C = cov(x.T)
U, S, Vh = linalg.svd(C)
U = mat(U)
i = 0
SSE = zeros((10,1))
for d in range(10,110,10):
    print(d)
    U1 = U[:,range(0,d)]
    X1 = x*U1
    b1 = multilinreg(X1,y)
    SSE[i] = linalg.norm(y-X1*b1)**2
    i = i+1
pyplot.plot(range(10,110,10),SSE)
