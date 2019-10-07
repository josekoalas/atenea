#Sumatorio doble

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
	s1 = 0
	for i in range(tv):
		s2 = 0
		for j in range(i+1):
			s2 += w[j]
		s1 += v[i] * s2
	print("Doble sumatorio:", s1)
	
	#Alternativa más eficiente
	s1 = 0
	s2 = 0
	for i in range(tv):
		s2 += w[i]
		s1 += v[i] * s2
	print("Doble sumatorio (Eficiente):", s1)
	
	#Alternativa vectorizada
	s1 = 0
	for i in range(tv):
		s1 += v[i] * sum(w[:i+1])
	print("Doble sumatorio (Vector):", s1)
else:
	print("Not same dimension")
