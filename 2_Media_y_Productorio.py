#Media e productorio

import sys

def get_input(t):
	while(True):
		try:
			i = float(input(t))
			return i
			break
		except ValueError:
			print("Not a number!")
		
n = int(get_input("Introduce el número de términos: "))

s = 0
p = 1

for i in range(n):
	print("---")
	x = get_input("Número " + str(i+1) + " :")
	s += x
	p *= x
	print("Suma parcial: " + str(s))
	print("Producto parcial: " + str(p))

print("---")
print("Suma final: " + str(s))
print("Producto final: " + str(p))
