from numpy import *
f = loadtxt("forza.dat")

def integral(fx):
    n = len(fx)
    px = zeros(n)

    for i in range(1,n):
        
