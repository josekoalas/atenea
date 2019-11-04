import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt("datosregresion.txt")
x = a[0]
y = a[1]


#Lineal
p = np.polyfit(x, y, 1)
print("y = {}x + {}".format(p[0], p[1]))
plt.figure(1)
plt.plot(x, y, "b.")
yr = np.polyval(p, x)
plt.plot(x, yr, "g-")
plt.show()


#Polinomico
p = np.polyfit(x, y, 2)
print("y = {}x + {}".format(p[0], p[1]))
plt.figure(2)
plt.plot(x, y, "b.")
yr = np.polyval(p, x)
plt.plot(x, yr, "g-")
plt.show()


#Interpolación lineal
plt.figure(3)
plt.plot(x, y, "b.")
xp = np.linspace(min(x), max(x), 20)
ye = np.interp(xp, x, y)
yr = np.polyval()
