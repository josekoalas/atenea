import numpy as np

tries = 10

def get_input(t):
	try:
		i = int(input(t))
		return i
	except ValueError:
		print("Not a number!")

for i in range(tries):
    print("---")
    n = get_input("Introduce el rango de la matriz: ")
    if (n > 2):
        break

print("---")
a = np.zeros([n,n])

for i in range(n):
	for j in range(n):
		a[i,j] = float(get_input("Introduce el rango de la matriz: "))
