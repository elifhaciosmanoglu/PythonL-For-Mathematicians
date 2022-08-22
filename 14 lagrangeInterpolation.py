import numpy as np
# Reading number of unknowns
n = int(input('Enter number of data points: '))
# Making numpy array of n & n x n size and initializing to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n))
# Reading data points
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))
# Reading interpolation point
xk = float(input('Enter interpolation point: '))
# Set interpolated value initially to zero
yk = 0
# Implementing Lagrange Interpolation
for i in range(n):
    k = 1
    for j in range(n):
        if i != j:
            k = k * (xk - x[j])/(x[i] - x[j])
    yk = yk + k * y[i]    
# Displaying output
print('Interpolated value at %.3f is %.3f.' % (xk, yk))
