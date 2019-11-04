#Calcular si los elementos de un vector son pares
import numpy as np

l = np.array([2, 3, 4, 5, 6, 7])

def pares(x):
    r = x % 2
    return r == 0

f = lambda x: x % 2 == 0

print("Lista", l)
print("Funcion", pares(l))
print("F. Lambda", f(l))

#Multiples elementos de entrada
g = lambda a, b, c: a+b+c
print("Suma", g(3, 5, 7))
