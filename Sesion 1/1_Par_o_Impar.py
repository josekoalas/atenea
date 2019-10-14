# Dado un numero, determinar si es par o impar

import sys

print("---")

# Obtener entrada de usuario
n = input("Introduce un número: ")
if (n.isnumeric()):
    n = int(n)
    print("n = " + str(n))
else:
    print("Not a natural number")
    sys.exit()

# Par (Resto = 1 = True)
if (n % 2):
    print(str(n) + " es impar!")
# Impar
else:
    print(str(n) + " es par!")

print("---")
