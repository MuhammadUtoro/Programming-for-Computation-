# Double Integration - Double integration can be estimated using the same method as the 1-Dimensional integration 
# (using midpoint method). However there will be some adjustments on the code:
# Since we are dealing with the integration with respect to x and variable, therefore variables hx and hy for the step
# in x and y are needed. So are the nx and ny for the number of rectangle (iteration) and the iteration will be i for
# x-direction and j for y-direction
# the function will be 2x+y integrated from 0-2 in x and 2-3 in y

import numpy

def midpoint_double(f,a,b,c,d,nx,ny):
    hx = (b-a)/float(nx)
    hy = (d-c)/float(ny)
    sum = 0 # Set the variable to store the summary of the value
    for i in range(nx):
        for j in range(ny):
            xi = (a+hx/2)+i*hx # Iterate with respect to x
            yj = (c+hy/2)+j*hy # Iterate with respect to y
            sum += hx*hy*f(xi,yj)
    return sum

def f(x,y):
    return x**2 + y**2 # Define the function

sltn = midpoint_double(f,0,1,0,2,5,5)
print(sltn)