from numpy.linalg import *
from numpy import *
import matplotlib.pyplot as plt

a = loadtxt("datosregresion.txt")
x = a[0]
y = a[1]

def rlPonderada(x, y, sy):
    N = len(x)
    w = float(1) / sy ** 2

    sw = sum(w)
    swy = sum(w*y)
    swx2 = sum(w*x**2)
    swx = sum(w*x)
    swxy = sum(w*x*y)

    d = det(array([[sw, swx], [swx, swx2]]))
    a = (swy * swx2 - swx * swxy) / d
    b = (sw * swxy - swx * swy) / d

    sa = sqrt(swx2 / d)
    sb = sqrt(sw / d)
    r = (sw * swxy - swx * swy) / sqrt(d * (sw * sum(w * y ** 2) - swy ** 2))
    return [a, b, sa, sb, r]

[a, b, sa, sb, r] = rlPonderada(x, y, y/10)
print("y = {} + {}x".format(a, b))
print("sa = {}, sb = {}, r = {}".format(sa, sb, r))

plt.figure(1)
plt.clf
plt.plot(x, y, "b.", label="Pts")
xr = array([min(x), max(x)])
yr = a + b * xr
plt.plot(xr, yr, "r-", label="RLP")
plt.legend()
plt.title("Regresion Lineal Ponderada")
plt.show()
