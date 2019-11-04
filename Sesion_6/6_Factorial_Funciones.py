import math

#Obtener un numero entero positivo
def get_input(t):
	correct = False
	n = 0
	while(not correct):
		try:
			i = input(t)
			n = int(i)
			if n < 1:
				print("No puede ser un numero negativo")
			else:
				correct = True
		except:
			print("No es un numero entero")
	return n
	
	
#Funcion Factorial
def fact(x):
	y = 1
	if x > 1:
		for i in range(1, x+1):
			y *= i
	return y
	
	
#Llamada al programa
n = get_input("n = ")
t = input("¿Quieres visualizar todos los factoriales? (y/N) ")
if t.upper() == "Y":
	for i in range(1, n+1):
		print("Factorial de {} = {}".format(i, fact(i)))
else:
	print("Factorial de {} = {}".format(n, fact(n)))

