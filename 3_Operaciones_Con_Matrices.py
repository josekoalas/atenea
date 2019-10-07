import numpy as np

def get_input(t):
	try:
		i = float(input(t))
		return i
	except:
		print("Not a number")
		return 0

n = 0

while n < 2:
	print("---")
	n = int(get_input("Introduce el rango de la matriz: "))

def get_matrix():
	while True:
		try:
			print("---")
			m = input("Matriz (Separada por espacios): ")
			m = (np.float_(m.split())).reshape([n,n])
			print("---")
			print("Matriz:")
			print(m)
			return m
			break
		except:
			print("Los datos de entrada no coinciden con las dimensiones de la matriz")
			print("Pruebe de nuevo")
		
m = get_matrix()
s = np.sum(m)
t = np.trace(m)
st1 = np.sum(m - np.tril(m))
sim = np.all(m == m.T)

print("---")
print("Suma matriz:", s)
print("Traza matriz:", t)
print("Suma triángulo superior", st1)

if sim: print("Matriz simétrica")
else: print("Matriz no simétrica")
