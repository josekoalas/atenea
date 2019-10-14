#Sumar numeros introducidos por teclado

continuar = True
n = 0
s = 0

print("---------------------------------")
print("Supersumatorio ^u^")
print("---------------------------------")
print(" ")

#Probar si es un numero racional
def is_number(s):
	try:
		float(s)
		return True
	except:
		return False

#Obtener entrada de usuario
def get_num(n):
	n = input("Introduce un número: ")
	if (is_number(n)):
		n = float(n)
		return(n)
	else:
		print("Test")
		continuar = False
		return(0)

#Bucle de entrada
while(continuar==True):
	get_num(n)
	s += n
	print("Suma parcial: " + str(s))
	print("---")



print("Suma finalizada")
print("Total: " + str(s))
