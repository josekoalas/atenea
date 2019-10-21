#Factorial
import math

#Con factorial de Python
n = int(input("n = "))
for i in range(n+1):
    print("Factorial de {}= {}".format(i, math.factorial(i)))

#Creación Propia
def get_input(t):
	try:
		i = float(input(t))
		return i
	except:
		print("Not a number")
		return 0

def calc_factorial(n):
    f = 1
    if int(n) == n:
        if n > 1:
            for i in range(n):
                f *= i + 1
        else:
            print("No se puede calcular el factorial de un número menor que 1")
    else:
        print("No es un número entero")
    return f

n = int(get_input("n = "))
if n > 0: print(calc_factorial(n))
