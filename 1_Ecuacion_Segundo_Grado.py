#Resolver una ecuacion de segundo grado dados los coeficientes
#ax²+bx+c

import sys
import numpy as np

print("---------------------------------")
print("Ecualculadora ^u^")
print("---------------------------------")

#Probar si es un numero racional
def is_number(s):
  try:
    float(s)
    return True
  except:
    return False

#Obtener entrada de usuario
p = [0,0,0]
for i in range(0,3):
  p[i] = input("Introduce el " + str(i+1) + "º termino: ")
  if (is_number(p[i])):
    p[i] = float(p[i])
  else:
    print("Not a number")
    sys.exit()

#Resolucion de ecuacion
def solver(a,b,c):

  if (a == 0):
    if (b == 0):
      print("Sin solución")
      sys.exit()
    else:
      x1 = -(c / b)
      x2 = x1
  else:
    if (b == 0):
      if (c < 0):
        print("Solución no real")
        sys.exit()
      else:
        x1 = np.sqrt(c)
        x2 = -np.sqrt(c)
    else:
      if (b ** 2 < 4 * a * c):
        print("Solución no real")
        sys.exit()
      else:
        x1 = (-b + np.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - np.sqrt(b ** 2 - 4 * a * c)) / 2 * a

  return [x1, x2]

print("---")

s = solver(p[0], p[1], p[2])
print(s)

print("---")
