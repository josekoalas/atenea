import numpy as np

def get_input(t):
	try:
		i = float(input(t))
		return i
	except:
		print("Not a number")
		return 0

def get_ecuation():
	while True:
		try:
			print("---")
			print("De la forma ax^n + bx^⁽n-1) + ... = t")
			e = input("Ecuación (Separada por espacios): ")
			e = np.float_(e.split())
			return e
			break
		except:
			print("Prueba de nuevo")


#Valores por defecto
a1 = "1 2 1 -3 -2 9 4 9 6" #SCD
a2 = "0 2 -2 1 -1 1 2 0 -1" #División por 0

b1 = "4 40 24"
b2 = "1 0 3"

a = (np.float_(a2.split())).reshape([3,3])
b = (np.float_(b2.split())).reshape([3,1])


v = input("Usar valores predeterminados? (Y/n)")
if (v == "n") or (v == "N"):
	givenValues = False
else:
	givenValues = True
	
if not(givenValues):
	n = int(get_input("Introduce el número de ecuaciones: "))
	for i in range(n):
		e = get_ecuation()
		if i == 0:
			a = e[:-1]
			b = e[-1:]
		else:
			a = np.vstack((a,e[:-1]))
			b = np.vstack((b,e[-1:]))
	
#print(a)
#print(b)
print("---")

#Rango de la matriz de coeficientes
ra = np.linalg.matrix_rank(a)
#Forma de la matriz de coeficientes
[ne, ni] = a.shape #Nº ecuaciones, Nº incognitas
#Matriz ampliada
A = np.hstack((a,b))
#Rango de la matriz ampliada
rA = np.linalg.matrix_rank(A)

if ra == rA :
	print("Sistema compatible")
	print("---")
	print(A)
	#Para cada incognita
	for i in range(ni):
		
		#Sistema de pivote para evitar / 0
		if A[i,i] == 0:
			m = np.max(np.abs(A[i+1:,i]))
			if m > 0:
				print("---")
				print(A)
				print("Pivote")
				pmax = (i+1) + np.argmax(np.abs(A[i+1:,i]))
				A[i], A[pmax] = A[pmax].copy(), A[i].copy()
				print(A)
				
		#Para cada ecuación
		for j in range(i+1, ne):
			l = A[j,i] / A[i,i]
			A[j] = A[j] - l * A[i]
		print("---")
		print(A)
		
	print("---")
	if ra == ni:
		print("Sistema compatible determinado")
		x = np.zeros(ni)
		for i in range(ni-1, -1, -1):
			x[i] = (A[i,-1] - sum(A[i, i+1:ni] * x[i+1:ni])) / A[i,i]
		print("Soluciones:", x)
	else:
		print("Sistema compatible indeterminado")
		
else:
	print("Sistema incompatible")
