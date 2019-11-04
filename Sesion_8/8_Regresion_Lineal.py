#Regresion Lineal
import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt("datosregresion.txt")
x = a[0]
y = a[1]


def regresion(x, y):
  N = len(x)
  sx = np.sum(x)
  sy = np.sum(y)
  sx2 = np.sum(x**2)
  sy2 = np.sum(y**2)
  sxy = np.sum(x*y)

  d = N * sx2 - sx ** 2
  b = (N * sxy - sx * sy) / d
  a = (sx2 * sy - sx * sxy) / d

  s = np.sqrt(sum(y - a - b * x) ** 2 / (N - 2))
  sa = s * np.sqrt(sx2 / d)
  sb = s * np.sqrt(N / d)

  r = (N * sxy - sx * sy) / np.sqrt(d * (N * sum(y ** 2) - sy ** 2))

  return [a, b, sa, sb, r]


[a, b, sa, sb, r] = regresion(x, y)
print("y = {} + {}x".format(a, b))
print("sa = {}, sb = {}, r = {}".format(sa, sb, r))

plt.figure(1)
plt.clf
plt.plot(x, y, "b.", label="Pts")
xr = np.array([min(x), max(x)])
yr = a + b * xr
plt.plot(xr, yr, "r-", label="RL")
plt.legend()
plt.title("Regresion Lineal")
plt.show()
