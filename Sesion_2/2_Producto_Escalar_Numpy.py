#Numero entero n, producto escalar de n vectores de dimension d (Numpy)

import numpy as np

a = input("Vector v (Separado por espacios): ").split()
v = np.float_(a)
a = input("Vector w (Separado por espacios): ").split()
w = np.float_(a)

print("v =", v)
print("w =", w)

tv = len(v)
tw = len(w)

if tv == tw:
	print("Producto escalar NP: ", np.dot(v, w))
	
	s = 0
	for i in range(tv):
		s += v[i] * w[i]
	print("Producto escalar PY: ", s)
		
else:
	print("Not same dimension")
