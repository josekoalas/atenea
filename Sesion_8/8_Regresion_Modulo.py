from numpy.linalg import *
from numpy import *
import matplotlib.pyplot as plt
from regresionlineal import *


a = loadtxt("datosregresion.txt")
x = a[0]
y = a[1]


[a, b, sa, sb, r] = rl(x, y)
print("y = {} + {}x".format(a, b))
print("sa = {}, sb = {}, r = {}".format(sa, sb, r))

plt.figure(1)
plt.clf
plt.plot(x, y, "b.", label="Pts")
xr = array([min(x), max(x)])
yr = a + b * xr
plt.plot(xr, yr, "r-", label="RL")
plt.legend()
plt.title("Regresion Lineal")
plt.show()


[a, b, sa, sb, r] = rlp(x, y, y/10)
print("y = {} + {}x".format(a, b))
print("sa = {}, sb = {}, r = {}".format(sa, sb, r))

plt.figure(2)
plt.clf
plt.plot(x, y, "b.", label="Pts")
xr = array([min(x), max(x)])
yr = a + b * xr
plt.plot(xr, yr, "r-", label="RLP")
plt.legend()
plt.title("Regresion Lineal Ponderada")
plt.show()
