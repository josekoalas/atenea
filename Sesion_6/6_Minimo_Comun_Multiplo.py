#Minimo Comun Multiplo

#Obtener numero entero positivo
def int_input(t):
	correct = False
	n = 0
	while(not correct):
		try:
			n = int(input(t))
			if n < 1:
				print("No puede ser un numero negativo")
			else:
				correct = True
		except:
			print("No es un numero entero")
	return n
	
#Lista de numeros primos hasta el numero indicado
def primes(n):
    if n < 2:
        return []
    else:
        pl = [2] #Lista de primos
        for i in range(3, n):
            isPrime = True
            for j in pl:
            	#Eliminar aquellos mayores que la mitad por eficiencia
                if j > n ** 0.5:
                    break
                #Eliminar si ya está en la lista o es multiplo
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                pl.append(i)
        return pl
        
#Elige los factores de entre la lista de primos hasta ese numero
def factors(n):
	fl = []
	for p in primes(n):
		while n%p==0:
			fl.append(p)
			n=n//p
			if n < 2:
				return fl
                
        
#Dividir en factores y exponentes
def order_factors(f):
	n = []
	e = []
	for i in f:
		if i in n:
			ind = n.index(i)
			e[ind] += 1
		else:
			n.append(i)
			e.append(1)
	return (n, e)


#Calcular MCD (Maximo Comun Divisor)
def mcd(a, b):
	#for i in range(len(n1)):
		#if a[i][0] in b[:][0]
	
	
	
	return m


#Obtener numeros FIX THIS
a = int_input("A = ")
f = factors(a)
if f == None:
	f = ([a], [1])
fa = order_factors(f)
fb = order_factors(factors(int_input("B = ")))
print(fa, fb, fb[:][0])















