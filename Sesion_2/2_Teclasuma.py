#Sumar numeros por teclado

import sys

def get_input(t):
	while(True):
		try:
			i = float(input(t))
			return i
			break
		except ValueError:
			print("Not a number!")
		
n = int(get_input("Introduce el número de sumandos: "))

s = 0

for i in range(n):
	print("---")
	x = get_input("Sumando número " + str(i+1) + " :")
	s += x
	print("Suma parcial: " + str(s))

print("---")
print("Suma finalizada, resultado total:")
print(s)
