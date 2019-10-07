#Medicion de tiempo

import time as t

def get_input(t):
	while(True):
		try:
			i = float(input(t))
			return i
			break
		except ValueError:
			print("Not a number!")

n = int(get_input("n = "))



#While + x = x + [i * i]
inicio = t.process_time() #Reemplaza a t.clock()

i = 0
x = []
while i < n:
	x += [i*i]
	i += 1

fin = t.process_time()
print("Opción a: %f" % (fin - inicio))



#While + append()
inicio = t.process_time() #Reemplaza a t.clock()

i = 0
y = []
while i < n:
	y.append(i*i)
	i += 1

fin = t.process_time()
print("Opción b: %f" % (fin - inicio))



#While + lista reservada
inicio = t.process_time() #Reemplaza a t.clock()

i = 0
z = [0] * n
while i < n:
	z[i] = i*i
	i += 1

fin = t.process_time()
print("Opción c: %f" % (fin - inicio))



#For + x = x + [i * i]
inicio = t.process_time() #Reemplaza a t.clock()

v = []
for i in range(n):
	v += [i*i]

fin = t.process_time()
print("Opción d: %f" % (fin - inicio))



#For + append()
inicio = t.process_time() #Reemplaza a t.clock()

w = []
for i in range(n):
	w.append(i*i)

fin = t.process_time()
print("Opción e: %f" % (fin - inicio))



#For + lista reservada
inicio = t.process_time() #Reemplaza a t.clock()

u = [0] * n
for i in range(n):
	u[i] = i*i

fin = t.process_time()
print("Opción f: %f" % (fin - inicio))
