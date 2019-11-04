#Examen
import numpy as np

#Obtener un numero entero multiplo de 3 que pertenezca a [5, 20]
def int_input(t):
	correct = False
	n = 0
	while(not correct):
		try:
			n = int(input(t))
			if n >= 5 and n <= 20:
				if n%3 == 0:
					correct = True
				else:
					print("No es un multiplo de 3")
			else:
				print("No pertenece al intervalo [5, 20]")
		except:
			print("No es un numero entero")
	return n
	
n = int_input("n = ")



#Vector con n numeros enteros aleatorios del intervalo [20,50]
x = np.ones([n])
for i in range(n):
	x[i] = (np.random.randint(20,50))
print(x)



#Vector y barallado de x
y = x.copy()
np.random.shuffle(y)
print(y)

#Comprobar elementos iguais
n2 = 0
for i in range(len(x)):
	if x[i] == y[i]:
		n2 += 1



#Vector z de dimension n2 onde cada z[i] (i = 0,...,n-1) é:
z = np.ones([n2])
for i in range(n2):
	sx, sy = 0, 0
	for j in range(i):
		sx += x[j]
		sy += y[j]
	print(sx, sy)	
	if sx < sy:
		z[i] = (x[i] * y [n - i - 1])
	else:
		z[i] = (x[i] / (y[i] ** 2 + 1))
print(z)

		
		
#Exportar a saida.txt x, y, z, utilizando savetxt() de numpy
t = np.concatenate((x, y, z))
print(t)
np.savetxt("saida.txt", t)
	
	
		
