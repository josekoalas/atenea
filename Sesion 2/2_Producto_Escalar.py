#Numero entero n, producto escalar de n vectores de dimension d

def get_input(t):
	while(True):
		try:
			i = float(input(t))
			return i
			break
		except ValueError:
			print("Not a number!")
		
n = int(get_input("Introduce el número de términos: "))
d = int(get_input("Introduce la dimensión: "))

v = []
s = 0

for i in range(n):
	temp = []
	print("---")
	print("Vector " + str(i+1) + " :")
	
	for j in range(d):
		temp.append(get_input("Componente " + str(j+1) + " : "))
	
	v.append(temp)
	m = 1
	for k in range(len(temp)):
		m *= temp[k]
	s += m
	print("Suma parcial: " + str(s))

print("---")
print("Producto escalar: " + str(s))
print("Vectores:")
print(v)
