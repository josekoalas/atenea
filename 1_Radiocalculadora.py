#Dado un radio, devolver:
#- Perimetro da circunferencia
#- Area do circulo
#- Volumen da esfera

import sys
import numpy as np

print("---------------------------------")
print("Radiocalculadora ^u^")
print("---------------------------------")

#Probar si es un numero racional
def is_number(s):
  try:
    float(s)
    return True
  except:
    return False

#Obtener entrada de usuario
r = input("Introduce un radio: ")
if (is_number(r)):
  print("r = " + r)
  r = float(r)
else:
  print("Not a number")
  sys.exit()

print("---")

#Perimetro
p = 2 * np.pi * r
print("Perimetro Circunferencia: " + str(p))

#Area Circulo
a = np.pi * (r ** 2)
print("Area Circulo: " + str(a))

#Volumen Esfera
v = 4 / 3 * np.pi * (r ** 3)
print("Volumen Esfera: " + str(v))

print("---")
