import numpy as np

n = np.random.randint(3,15)

a = np.zeros([n, n])

for i in range(n):
    for j in range(n):
        if i == j:
            a[i, j] = np.log(((i+1) + 1) ** 3)
        if i > j:
            a[i, j] = np.sin((i ** 2) * (j + 1)) * np.sqrt((i + 1) ** 3)
        if i < j:
            a[i, j] = (i + 2) * j * (np.e ** -i)

print(np.round_(a, 1))

x = abs(float(input("x = ")))
y = a.flatten()

s = 0
c = 0

for i in range(len(y)):
    s += y[i]
    c += 1
    if s > x:
        s -= y[i]
        c -= 1
        break

print("x = {}, s = {}, número de terminos = {}".format(x, s, c))
