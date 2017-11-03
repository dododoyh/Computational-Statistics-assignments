#Using Newton-Raphson method to compute a root of the following function :f(x) = (0.9sin(x) − x)


from numpy import *
from matplotlib import pyplot

# define the function
f = lambda x: 0.9*sin(x)-x
# simple iteration
x0 = pi/4
x = zeros(1000)
x[0]=  x0
gx = f(x[0]) + x[0]
i = 0
while abs(x[i] - gx) > 1e-6:
    gx = x[i]
    x[i+1] = f(x[i]) + x[i]
    i = i + 1
pyplot.figure(1)
pyplot.plot(range(0,i+1), x[0:i+1], 'b-')
pyplot.show()

# Newton-Raphson
f = lambda x: 0.9*sin(x)-x
df = lambda x: 0.9*cos(x)-1
x0 = pi/4
x = zeros(1000)
x[0]=  x0
gx = x[0] - f(x[0])/df(x[0])
i = 0
while abs(x[i] - gx) > 1e-6:
    gx = x[i]
    x[i+1] = x[i]- f(x[i])/df(x[i])
    i = i + 1
pyplot.figure(1)
pyplot.plot(range(0,i+1), x[0:i+1], 'b-')
pyplot.show()
