from numpy import *
from matplotlib.pyplot import *

p = loadtxt("posicion.dat")

def derivadaFuncion(fx):
    n = len(fx)
    df = zeros(n-1)
    for i in range(n-1):
        df[i] = fx[i+1] - fx[i]
    return df

v = derivadaFuncion(p)
figure(1)
clf()
subplot(311)
plot(p, "b-")
title("Posicion")
grid(True)
subplot(312)
plot(v, "g-")
title("Velocidade")
grid(True)
subplot(313)
plot(ediff1d(p), "r-")
title("Velocidad NP")
grid(True)
show()
