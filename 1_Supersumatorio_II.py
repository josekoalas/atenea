#Probar si es un numero racional
def is_number(s):
  try:
    float(s)
    return True
  except:
    return False

#Obtener entrada de usuario
def get_num(t):
  n = input(t)
  if (is_number(n)):
    n = float(n)
    return(n)
  else:
    print("Not a number")
    sys.exit()

s = 0
n = int(get_num("Numero de terminos a sumar: "))

for i in range(n):
  x = get_num("Introduce el " + str(i+1) + "º numero: ")
  s += x
  print("i = " + str(i) + " x = " + str(x) + " Suma = " + str(s))

print("Suma total: " + str(s))
