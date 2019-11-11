#Suma de una serie
from matplotlib.pyplot import *

suma = 0
niter = int(input("Numero máximo de iteraciones: "))
n = 1
x, y, z = [], [], []

for n in range(1, niter+1):
    sumando = n ** 2
    if sumando <= 1e-5:
        break
    suma = suma + sumando
    x.append(n)
    y.append(suma)
    z.append(sumando)

if n < niter:
    print("Suma = {} en {} iteracións".format(suma, n))
else:
    print("No converge en {} iteracións".format(n))

figure(1)
clf()
subplot(2, 1, 1)
plot(x, y, "b-")
title("Suma")
subplot(212)

semilogy(x, z, "g-")
title("Sumandos")
show()
