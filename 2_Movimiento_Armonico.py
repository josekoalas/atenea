#Movemento armónico
import numpy as np
import matplotlib.pyplot as plt

omega = np.pi / 10
theta = np.pi / 2
b = 2.5

t = np.linspace(0, 100, 200)
x = b * np.sin(omega * t + theta)
v = b * omega * np.cos(omega * t + theta)
a = -b * omega**2 * np.sin(omega * t + theta)

plt.clf()

plt.plot(t, x, "r.-", label="x(t)")
plt.plot(t, v, "g.-", label="v(t)")
plt.plot(t, a, "b.-", label="a(t)")

plt.grid()
plt.xlabel('Tempo')
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))

plt.show()
