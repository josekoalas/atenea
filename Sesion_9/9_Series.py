#Suma de una serie
from matplotlib.pyplot import *

suma = 0
sumando = 1
n = 1
x, y, z = [], [], []

while sumando > 1e-5:
    suma += sumando
    x.append(n)
    y.append(suma)
    z.append(sumando)
    n += 1
    sumando = float(1) / n ** 2

print("Suma = {} en {} iteracións".format(suma, n))

figure(1)
clf()
subplot(2, 1, 1)
plot(x, y, "b-")
title("Suma")
subplot(212)

semilogy(x, z, "g-")
title("Sumandos")
show()
